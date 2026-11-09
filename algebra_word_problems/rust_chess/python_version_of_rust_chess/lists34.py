"""Lists 3 and 4 (Steps 12 and 13): made from the position index, never by looking ahead."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from board import Board, Move
from index import Counts, Index
from normalize import Cat, normalize, relative_move, similar_key
from strategies import (
    F_COMPLETION,
    F_FOUNDATION,
    F_PROGRESS,
    NAMES,
    stage_rank,
)


@dataclass(frozen=True)
class RowKind:
    """Proven / tried / similar / never-tried classification for a List 3 row."""

    kind: str  # "proven_win" | "proven_draw" | "tried" | "similar" | "never_tried"
    dist: int = 0

    @staticmethod
    def proven_win(n: int) -> RowKind:
        return RowKind("proven_win", int(n))

    @staticmethod
    def proven_draw() -> RowKind:
        return RowKind("proven_draw")

    @staticmethod
    def tried() -> RowKind:
        return RowKind("tried")

    @staticmethod
    def similar() -> RowKind:
        return RowKind("similar")

    @staticmethod
    def never_tried() -> RowKind:
        return RowKind("never_tried")


@dataclass
class List3Row:
    mv: Move
    san: str
    kind: RowKind
    counts: Counts
    notes: list[tuple[str, int]]
    order: int


@dataclass
class List3:
    rows: list[List3Row]
    cat: Cat
    pawn_side_to_move: bool
    position_known: bool


def played_score(d: int, f: int) -> int:
    """The List 3 score of one strategy from played moves (Step 14.1 rule 8)."""
    # Parentheses required: in Python, comparisons bind tighter than bitwise &.
    if (d & F_COMPLETION) != 0:
        return 100
    if (d & F_FOUNDATION) != 0 and (d & F_PROGRESS) != 0:
        if (f & F_COMPLETION) != 0:
            return 75
        return 60
    if (d & F_FOUNDATION) != 0:
        if (f & (F_PROGRESS | F_COMPLETION)) != 0:
            return 45
        return 30
    if (d & F_PROGRESS) != 0:
        return 30
    return 0


def best_played_score(mask: int) -> int:
    """The highest score that any one game's pair earns (Step 12): pairs are never split."""
    best = 0
    for b in range(64):
        if ((mask >> b) & 1) == 1:
            s = played_score(b // 8, b % 8)
            if s > best:
                best = s
    return best


def list3(ix: Index, b: Board, bank: Optional[str] = None) -> List3:
    n = normalize(b)
    node = ix.lookup(n.key())
    family = n.cat.proof_family()
    pawn_side_to_move = family and n.board.white_to_move
    sim_key = similar_key(n)
    rows: list[List3Row] = []
    for order, m in enumerate(b.legal_moves()):
        nm = n.t.mv(m)
        nu = nm.uci()
        san = b.san(m)
        edge = None
        if node is not None:
            nd = ix.nodes[node]
            try:
                i = nd.legal.index(nu)
            except ValueError:
                i = None
            if i is not None:
                edge = nd.edges[i]
        if edge is not None:
            counts = ix.edge_counts(edge, bank)
            if family:
                ev = ix.edge_value(edge)
                if ev.is_win():
                    kind = RowKind.proven_win(ev.dist + 1)
                elif ev.is_draw():
                    kind = RowKind.proven_draw()
                else:
                    kind = RowKind.tried()
            else:
                kind = RowKind.tried()
            ed = ix.edges[edge]
            notes: list[tuple[str, int]] = []
            for k in range(20):
                s = best_played_score(ed.pairs[k])
                if s > 0:
                    notes.append((NAMES[k], s))
            notes.sort(key=lambda a: (stage_rank(a[1]), -a[1], a[0]))
            rows.append(
                List3Row(
                    mv=m, san=san, kind=kind, counts=counts, notes=notes, order=order
                )
            )
        else:
            counts = Counts()
            kind = RowKind.never_tried()
            if sim_key is not None:
                rm = relative_move(n.board, nm)
                banks = ix.similar.get(f"{sim_key}|{rm}")
                if banks is not None:
                    for bk, c in banks.items():
                        if bank is None or bank == bk:
                            counts.add(c)
                    if counts.played > 0:
                        kind = RowKind.similar()
            rows.append(
                List3Row(
                    mv=m,
                    san=san,
                    kind=kind,
                    counts=counts,
                    notes=[],
                    order=order,
                )
            )
    _sort_list3(rows, family, pawn_side_to_move)
    return List3(
        rows=rows,
        cat=n.cat,
        pawn_side_to_move=pawn_side_to_move,
        position_known=node is not None,
    )


def _group(kind: RowKind, family: bool, pawn_side: bool) -> int:
    never = kind.kind in ("never_tried", "similar")
    if not family:
        return 1 if never else 0
    if pawn_side:
        if kind.kind == "proven_win":
            return 0
        if kind.kind == "tried":
            return 1
        if kind.kind == "proven_draw":
            return 3
        return 2
    if kind.kind == "proven_draw":
        return 0
    if kind.kind == "tried":
        return 2
    if kind.kind == "proven_win":
        return 3
    return 1


def _sort_list3(rows: list[List3Row], family: bool, pawn_side: bool) -> None:
    def key(a: List3Row):
        ga = _group(a.kind, family, pawn_side)
        if a.kind.kind == "proven_win":
            dist_key = a.kind.dist if pawn_side else -a.kind.dist
        else:
            dist_key = 0
        if a.kind.kind == "tried":
            rate = a.counts.win_rate()
            rate_key = -rate if (not family or pawn_side) else rate
        else:
            rate_key = 0.0
        return (ga, dist_key, rate_key, a.order)

    rows.sort(key=key)


@dataclass
class List4Row:
    mv: Move
    san: str
    reply: str
    next: str
    count: int
    gain: int
    loss: int
    bank: str

    def net(self) -> int:
        return self.gain - self.loss


def list4(ix: Index, b: Board, bank: Optional[str] = None) -> list[List4Row]:
    """List 4: captures and promotions that past games actually played, in the
    move and the full turn after it. Each different continuation is one row."""
    n = normalize(b)
    id_ = ix.lookup(n.key())
    if id_ is None:
        return []
    node = ix.nodes[id_]
    rows: list[List4Row] = []
    for m in b.legal_moves():
        nu = n.t.mv(m).uci()
        try:
            i = node.legal.index(nu)
        except ValueError:
            continue
        e = node.edges[i]
        if e is None:
            continue
        after = b.make(m)
        merged: dict[tuple[str, str], tuple[int, int, int, str]] = {}
        for (bk, r, nx), c in ix.edges[e].conts.items():
            if bank is not None and bank != bk:
                continue
            reply_real = None if r == "-" else after.parse_move(n.t.move_text(r))
            reply_san = after.san(reply_real) if reply_real is not None else "-"
            if reply_real is not None and nx != "-":
                a2 = after.make(reply_real)
                nm = a2.parse_move(n.t.move_text(nx))
                next_san = a2.san(nm) if nm is not None else "-"
            else:
                next_san = "-"
            key = (reply_san, next_san)
            if key not in merged:
                merged[key] = (0, c.gain, c.loss, bk)
            count, gain, loss, bank_name = merged[key]
            count += c.count
            if bank_name != bk:
                bank_name = "all"
            merged[key] = (count, gain, loss, bank_name)
        for (reply, next_), (count, gain, loss, bk) in merged.items():
            rows.append(
                List4Row(
                    mv=m,
                    san=b.san(m),
                    reply=reply,
                    next=next_,
                    count=count,
                    gain=gain,
                    loss=loss,
                    bank=bk,
                )
            )
    rows.sort(key=lambda a: (-a.net(), -a.gain, a.loss, a.san, a.reply, a.next))
    return rows
