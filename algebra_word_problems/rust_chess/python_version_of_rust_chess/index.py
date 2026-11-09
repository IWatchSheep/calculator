"""Step 15: one entry per distinct position, and Step 12: how a result becomes proven."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from board import (
    BISHOP,
    KNIGHT,
    QUEEN,
    Board,
    Move,
    piece_value,
)
from normalize import Cat, Normalized, normalize, relative_move, similar_key


@dataclass(frozen=True)
class Status:
    """Proven result for a position or edge goal."""

    kind: str  # "unknown" | "win" | "draw"
    dist: int = 0

    @staticmethod
    def unknown() -> Status:
        return Status("unknown")

    @staticmethod
    def win(d: int) -> Status:
        return Status("win", int(d))

    @staticmethod
    def draw() -> Status:
        return Status("draw")

    def text(self) -> str:
        if self.kind == "unknown":
            return "-"
        if self.kind == "win":
            return f"W{self.dist}"
        return "D"

    @staticmethod
    def parse(s: str) -> Status:
        if s == "D":
            return Status.draw()
        if s.startswith("W"):
            try:
                d = int(s[1:])
            except ValueError:
                d = 0
            return Status.win(d)
        return Status.unknown()

    def is_proven(self) -> bool:
        return self.kind != "unknown"

    def is_win(self) -> bool:
        return self.kind == "win"

    def is_draw(self) -> bool:
        return self.kind == "draw"


@dataclass
class Counts:
    played: int = 0
    wins: int = 0
    draws: int = 0
    losses: int = 0

    def add(self, o: Counts) -> None:
        self.played += o.played
        self.wins += o.wins
        self.draws += o.draws
        self.losses += o.losses

    def results(self) -> int:
        return self.wins + self.draws + self.losses

    def win_rate(self) -> float:
        r = self.results()
        if r == 0:
            return 0.0
        return self.wins / r


@dataclass
class Cont:
    count: int = 0
    gain: int = 0
    loss: int = 0


@dataclass
class Edge:
    from_: int
    idx: int
    to: int
    goal: Optional[Status] = None
    counts: dict[str, Counts] = field(default_factory=dict)
    pairs: list[int] = field(default_factory=lambda: [0] * 20)
    conts: dict[tuple[str, str, str], Cont] = field(default_factory=dict)

    @staticmethod
    def new(from_: int, idx: int, to: int, goal: Optional[Status]) -> Edge:
        return Edge(from_=from_, idx=idx, to=to, goal=goal)


@dataclass
class Node:
    key: str
    cat: Cat
    white_to_move: bool
    legal: list[str]
    edges: list[Optional[int]]
    status: Status
    terminal: bool
    preds: list[int] = field(default_factory=list)

    def fully_tried(self) -> bool:
        return self.terminal or all(e is not None for e in self.edges)

    def attacker_to_move(self) -> bool:
        return self.white_to_move


def pair_bit(d: int, f: int) -> int:
    """The bit of one (destination stages, later stages) pair."""
    return 1 << (((d & 7) * 8) + (f & 7))


class GameResult:
    WhiteWin = "white-wins"
    BlackWin = "black-wins"
    Draw = "draw"
    DrawByRule = "draw-by-rule"
    Stopped = "stopped"

    @staticmethod
    def text(r: str) -> str:
        return r

    @staticmethod
    def parse(s: str) -> str:
        if s in (
            GameResult.WhiteWin,
            GameResult.BlackWin,
            GameResult.Draw,
            GameResult.DrawByRule,
            GameResult.Stopped,
        ):
            return s
        return GameResult.Stopped


@dataclass
class SavedMove:
    uci: str
    flags: list[int]  # length 20


@dataclass
class GameRecord:
    id: int
    bank: str
    start: Board
    moves: list[SavedMove]
    result: str


def _status_rank_changed(old: Status, new: Status) -> bool:
    return old != new


class Index:
    def __init__(self) -> None:
        self.nodes: list[Node] = []
        self.edges: list[Edge] = []
        self.by_key: dict[str, int] = {}
        self.merged: list[int] = []
        self._merged_set: set[int] = set()
        # similar-position counts: "simkey|relmove" -> bank -> Counts
        self.similar: dict[str, dict[str, Counts]] = {}

    @staticmethod
    def new() -> Index:
        return Index()

    def is_merged(self, id_: int) -> bool:
        return id_ in self._merged_set

    def lookup(self, key: str) -> Optional[int]:
        return self.by_key.get(key)

    def node_for(self, n: Normalized) -> int:
        key = n.key()
        existing = self.by_key.get(key)
        if existing is not None:
            return existing
        b = n.board
        legal = [m.uci() for m in b.legal_moves()]
        terminal, status = terminal_status(b, n.cat, len(legal) == 0)
        id_ = len(self.nodes)
        self.nodes.append(
            Node(
                key=key,
                cat=n.cat,
                white_to_move=b.white_to_move,
                legal=legal,
                edges=[None] * len(legal),
                status=status,
                terminal=terminal,
                preds=[],
            )
        )
        self.by_key[key] = id_
        return id_

    def edge_value(self, e: int) -> Status:
        edge = self.edges[e]
        if edge.goal is not None:
            return edge.goal
        return self.nodes[edge.to].status

    def evaluate(self, id_: int) -> Status:
        n = self.nodes[id_]
        if n.terminal or not n.cat.proof_family():
            return n.status
        vals: list[Optional[Status]] = [
            self.edge_value(e) if e is not None else None for e in n.edges
        ]
        all_tried = all(v is not None for v in vals)
        if n.attacker_to_move():
            best_win = None
            for v in vals:
                if v is not None and v.is_win():
                    if best_win is None or v.dist < best_win:
                        best_win = v.dist
            if best_win is not None:
                derived = Status.win(best_win + 1)
            elif all_tried and all(v == Status.draw() for v in vals):
                derived = Status.draw()
            else:
                derived = Status.unknown()
        elif any(v == Status.draw() for v in vals):
            derived = Status.draw()
        elif all_tried and all(v is not None and v.is_win() for v in vals):
            worst = 0
            for v in vals:
                if v is not None and v.is_win() and v.dist > worst:
                    worst = v.dist
            derived = Status.win(worst + 1)
        else:
            derived = Status.unknown()
        # A proven status is never taken back; only a win's distance can shrink.
        old = n.status
        if old.is_draw():
            return Status.draw()
        if old.is_win():
            if derived.is_win():
                return Status.win(min(old.dist, derived.dist))
            return Status.win(old.dist)
        return derived

    def propagate(self, seeds: list[int]) -> list[int]:
        queue: deque[int] = deque(seeds)
        queued: set[int] = set(seeds)
        touched: list[int] = []
        while queue:
            id_ = queue.popleft()
            queued.discard(id_)
            touched.append(id_)
            old = self.nodes[id_].status
            new = self.evaluate(id_)
            if _status_rank_changed(old, new):
                self.nodes[id_].status = new
                for p in list(self.nodes[id_].preds):
                    if p not in queued:
                        queued.add(p)
                        queue.append(p)
        return touched

    def closed_region(
        self, start: int, reaches_open: set[int]
    ) -> Optional[list[int]]:
        stack = [start]
        seen: set[int] = {start}
        order: list[int] = []
        while stack:
            v = stack.pop()
            if v in reaches_open:
                return None
            n = self.nodes[v]
            order.append(v)
            if n.terminal or (n.status.is_proven() and v != start):
                continue
            if not n.fully_tried():
                return None
            for e in n.edges:
                if e is None:
                    continue
                edge = self.edges[e]
                if edge.goal is not None:
                    continue
                if edge.to not in seen:
                    seen.add(edge.to)
                    stack.append(edge.to)
        return order

    def close_draws(self, touched: list[int]) -> None:
        pending = list(touched)
        while True:
            cands: list[int] = []
            seen: set[int] = set()
            for t in pending:
                if t not in seen:
                    seen.add(t)
                    cands.append(t)
                for p in self.nodes[t].preds:
                    if p not in seen:
                        seen.add(p)
                        cands.append(p)
            reaches_open: set[int] = set()
            newly: list[int] = []
            for c in cands:
                n = self.nodes[c]
                if not n.cat.proof_family() or n.status.is_proven():
                    continue
                region = self.closed_region(c, reaches_open)
                if region is None:
                    reaches_open.add(c)
                else:
                    for v in region:
                        nv = self.nodes[v]
                        if nv.cat.proof_family() and nv.status == Status.unknown():
                            nv.status = Status.draw()
                            newly.append(v)
            if not newly:
                break
            seeds: list[int] = []
            for v in newly:
                seeds.extend(self.nodes[v].preds)
            pending = self.propagate(seeds)
            pending.extend(newly)

    def recheck(self, ids: list[int]) -> None:
        touched = self.propagate(ids)
        self.close_draws(touched)

    def add_test_node(
        self, key: str, cat: Cat, white_to_move: bool, legal: int
    ) -> int:
        id_ = len(self.nodes)
        self.nodes.append(
            Node(
                key=key,
                cat=cat,
                white_to_move=white_to_move,
                legal=[f"m{i}" for i in range(legal)],
                edges=[None] * legal,
                status=Status.unknown(),
                terminal=legal == 0,
                preds=[],
            )
        )
        self.by_key[key] = id_
        return id_

    def add_test_edge(
        self, from_: int, idx: int, to: int, goal: Optional[Status]
    ) -> int:
        e = len(self.edges)
        self.edges.append(Edge.new(from_, idx, to, goal))
        self.nodes[from_].edges[idx] = e
        if from_ not in self.nodes[to].preds:
            self.nodes[to].preds.append(from_)
        return e

    def merge(self, g: GameRecord) -> None:
        if g.id in self._merged_set:
            return
        boards: list[Board] = [g.start]
        moves: list[Move] = []
        for sm in g.moves:
            b = boards[-1]
            m = b.parse_move(sm.uci)
            if m is None:
                raise ValueError(f"game {g.id}: illegal move {sm.uci}")
            moves.append(m)
            boards.append(b.make(m))
        # Check the whole game before the index changes at all.
        norms = [normalize(b) for b in boards]
        for i in range(len(moves)):
            nm = norms[i].t.mv(moves[i]).uci()
            if not any(x.uci() == nm for x in norms[i].board.legal_moves()):
                raise ValueError(
                    f"game {g.id}: move {nm} is missing from its legal-move listing"
                )
        path: list[int] = []
        for i in range(len(moves)):
            b = boards[i]
            nb = norms[i]
            from_ = self.node_for(nb)
            to = self.node_for(norms[i + 1])
            nm = nb.t.mv(moves[i]).uci()
            try:
                idx = self.nodes[from_].legal.index(nm)
            except ValueError as exc:
                raise ValueError(
                    f"game {g.id}: move {nm} missing from its listing"
                ) from exc
            existing = self.nodes[from_].edges[idx]
            if existing is not None:
                e = existing
            else:
                goal = edge_goal(nb, moves[i], b)
                e = len(self.edges)
                self.edges.append(Edge.new(from_, idx, to, goal))
                self.nodes[from_].edges[idx] = e
                if from_ not in self.nodes[to].preds:
                    self.nodes[to].preds.append(from_)
            if nb.cat.folded():
                perspective_white = not nb.t.flip
            else:
                perspective_white = b.white_to_move
            add = Counts(played=1)
            if g.result == GameResult.Stopped:
                pass
            elif g.result in (GameResult.Draw, GameResult.DrawByRule):
                add.draws = 1
            elif g.result == GameResult.WhiteWin:
                if perspective_white:
                    add.wins = 1
                else:
                    add.losses = 1
            elif g.result == GameResult.BlackWin:
                if perspective_white:
                    add.losses = 1
                else:
                    add.wins = 1
            bank_counts = self.edges[e].counts.setdefault(g.bank, Counts())
            bank_counts.add(add)
            for k in range(20):
                later = g.moves[i + 2].flags[k] if i + 2 < len(g.moves) else 0
                self.edges[e].pairs[k] |= pair_bit(g.moves[i].flags[k], later)
            gain = 0
            loss = 0
            for j in range(i, min(i + 3, len(moves))):
                bj = boards[j]
                mj = moves[j]
                v = 0
                if bj.is_capture(mj):
                    v += piece_value(bj.captured_piece(mj))
                if mj.promo != 0:
                    v += piece_value(mj.promo) - 100
                if (j - i) % 2 == 0:
                    gain += v
                else:
                    loss += v
            if gain != 0 or loss != 0:
                reply = (
                    nb.t.mv(moves[i + 1]).uci() if i + 1 < len(moves) else "-"
                )
                next_ = (
                    nb.t.mv(moves[i + 2]).uci() if i + 2 < len(moves) else "-"
                )
                c = self.edges[e].conts.setdefault((g.bank, reply, next_), Cont())
                c.count += 1
                c.gain = gain
                c.loss = loss
            sk = similar_key(nb)
            if sk is not None:
                rm = relative_move(nb.board, nb.t.mv(moves[i]))
                sim = self.similar.setdefault(f"{sk}|{rm}", {})
                simc = sim.setdefault(g.bank, Counts())
                simc.add(add)
            path.append(from_)
            path.append(to)
        path.reverse()
        seeds: list[int] = []
        seen: set[int] = set()
        for p in path:
            if p not in seen:
                seen.add(p)
                seeds.append(p)
        touched = self.propagate(seeds)
        self.close_draws(touched)
        self.merged.append(g.id)
        self._merged_set.add(g.id)

    def proven_counts(self) -> tuple[int, int, int]:
        w = 0
        d = 0
        for n in self.nodes:
            if n.status.is_win():
                w += 1
            elif n.status.is_draw():
                d += 1
        return len(self.nodes), w, d

    def to_text(self) -> str:
        parts: list[str] = ["FORMING-CHESS-INDEX 2\n"]
        for g in self.merged:
            parts.append(f"G\t{g}\n")
        for n in self.nodes:
            legal = "-" if not n.legal else ",".join(n.legal)
            parts.append(
                f"N\t{n.key}\t{n.cat.code()}\t{n.status.text()}\t"
                f"{'T' if n.terminal else '-'}\t{legal}\n"
            )
        for i, e in enumerate(self.edges):
            goal = e.goal.text() if e.goal is not None else "-"
            parts.append(f"E\t{e.from_}\t{e.idx}\t{e.to}\t{goal}\n")
            pairs = [
                f"{k}:{m:x}" for k, m in enumerate(e.pairs) if m != 0
            ]
            if pairs:
                parts.append(f"P\t{i}\t{','.join(pairs)}\n")
            for bank in sorted(e.counts.keys()):
                c = e.counts[bank]
                parts.append(
                    f"C\t{i}\t{bank}\t{c.played}\t{c.wins}\t{c.draws}\t{c.losses}\n"
                )
            for key in sorted(e.conts.keys()):
                bank, r, nx = key
                c = e.conts[key]
                parts.append(
                    f"K\t{i}\t{bank}\t{r}\t{nx}\t{c.count}\t{c.gain}\t{c.loss}\n"
                )
        for k in sorted(self.similar.keys()):
            banks = self.similar[k]
            for bank in sorted(banks.keys()):
                c = banks[bank]
                parts.append(
                    f"S\t{k}\t{bank}\t{c.played}\t{c.wins}\t{c.draws}\t{c.losses}\n"
                )
        return "".join(parts)

    def save(self, path: Path | str) -> None:
        path = Path(path)
        if path.parent.parts:
            path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".tmp")
        tmp.write_text(self.to_text(), encoding="utf-8", newline="\n")
        tmp.replace(path)

    @staticmethod
    def load(path: Path | str) -> Index:
        path = Path(path)
        try:
            text = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            return Index.new()
        return Index.from_text(text)

    @staticmethod
    def from_text(text: str) -> Index:
        ix = Index.new()
        lines = text.splitlines()
        if not lines:
            return ix
        if lines[0] != "FORMING-CHESS-INDEX 2":
            raise ValueError(f'unknown index format "{lines[0]}"')
        for n, line in enumerate(lines[1:], start=2):
            f = line.split("\t")
            if not f or f[0] == "":
                continue
            want = {
                "G": 2,
                "N": 6,
                "E": 5,
                "P": 3,
                "C": 7,
                "K": 8,
                "S": 7,
            }.get(f[0])
            if want is None:
                continue
            if len(f) < want:
                raise ValueError(
                    f"index line {n}: short {f[0]} line "
                    f"({len(f)} fields, need {want})"
                )

            def num(i: int) -> int:
                try:
                    return int(f[i])
                except ValueError as exc:
                    raise ValueError(f"index line {n}: field {i}: {exc}") from exc

            def intv(i: int) -> int:
                try:
                    return int(f[i])
                except ValueError as exc:
                    raise ValueError(f"index line {n}: field {i}: {exc}") from exc

            kind = f[0]
            if kind == "G":
                id_ = num(1)
                ix.merged.append(id_)
                ix._merged_set.add(id_)
            elif kind == "N":
                legal = [] if f[5] == "-" else f[5].split(",")
                id_ = len(ix.nodes)
                ix.by_key[f[1]] = id_
                ix.nodes.append(
                    Node(
                        key=f[1],
                        cat=Cat.from_code(f[2]),
                        white_to_move="|w|" in f[1],
                        edges=[None] * len(legal),
                        legal=legal,
                        status=Status.parse(f[3]),
                        terminal=f[4] == "T",
                        preds=[],
                    )
                )
            elif kind == "E":
                from_ = num(1)
                idx = num(2)
                to = num(3)
                goal = None if f[4] == "-" else Status.parse(f[4])
                e = len(ix.edges)
                ix.edges.append(Edge.new(from_, idx, to, goal))
                if from_ >= len(ix.nodes):
                    raise ValueError(f"index line {n}: edge from unknown node")
                node = ix.nodes[from_]
                if idx >= len(node.edges):
                    raise ValueError(f"index line {n}: edge index out of range")
                node.edges[idx] = e
                if to >= len(ix.nodes):
                    raise ValueError(f"index line {n}: edge to unknown node")
                tn = ix.nodes[to]
                if from_ not in tn.preds:
                    tn.preds.append(from_)
            elif kind == "P":
                e = num(1)
                if e >= len(ix.edges):
                    raise ValueError(f"index line {n}: pairs for unknown edge")
                edge = ix.edges[e]
                for part in f[2].split(","):
                    if ":" not in part:
                        raise ValueError(f"index line {n}: bad pair field")
                    k_s, m_s = part.split(":", 1)
                    try:
                        k = int(k_s)
                    except ValueError as exc:
                        raise ValueError(
                            f"index line {n}: bad template number"
                        ) from exc
                    try:
                        m = int(m_s, 16)
                    except ValueError as exc:
                        raise ValueError(
                            f"index line {n}: bad pair mask"
                        ) from exc
                    if k >= len(edge.pairs):
                        raise ValueError(
                            f"index line {n}: template out of range"
                        )
                    edge.pairs[k] = m
            elif kind == "C":
                e = num(1)
                c = Counts(
                    played=num(3), wins=num(4), draws=num(5), losses=num(6)
                )
                if e >= len(ix.edges):
                    raise ValueError(f"index line {n}: count for unknown edge")
                ix.edges[e].counts[f[2]] = c
            elif kind == "K":
                e = num(1)
                c = Cont(count=num(5), gain=intv(6), loss=intv(7))
                if e >= len(ix.edges):
                    raise ValueError(
                        f"index line {n}: continuation for unknown edge"
                    )
                ix.edges[e].conts[(f[2], f[3], f[4])] = c
            elif kind == "S":
                c = Counts(
                    played=num(3), wins=num(4), draws=num(5), losses=num(6)
                )
                ix.similar.setdefault(f[1], {})[f[2]] = c
        return ix

    def edge_counts(self, e: int, bank: Optional[str] = None) -> Counts:
        c = Counts()
        for b, x in self.edges[e].counts.items():
            if bank is None or bank == b:
                c.add(x)
        return c


def terminal_status(b: Board, cat: Cat, no_moves: bool) -> tuple[bool, Status]:
    if cat == Cat.DeadDraw:
        return True, Status.draw()
    if cat == Cat.Kqk:
        if no_moves:
            if b.in_check(b.white_to_move) and not b.white_to_move:
                return True, Status.win(0)
            return True, Status.draw()
        if not b.white_to_move:
            qsq = next((s for s in range(64) if b.sq[s] == QUEEN), 0)
            capturable = any(m.to == qsq for m in b.legal_moves())
            return True, Status.draw() if capturable else Status.win(0)
        return True, Status.win(0)
    if cat in (Cat.Kpk, Cat.Krk):
        if no_moves:
            if b.in_check(b.white_to_move) and not b.white_to_move:
                return True, Status.win(0)
            return True, Status.draw()
        return False, Status.unknown()
    # Cat.Other
    return no_moves, Status.unknown()


def edge_goal(nb: Normalized, real_move: Move, _real: Board) -> Optional[Status]:
    """Promotion goal in KPK (Step 12)."""
    if nb.cat != Cat.Kpk or real_move.promo == 0:
        return None
    m = nb.t.mv(real_move)
    after = nb.board.make(m)
    replies = after.legal_moves()
    if not replies:
        if after.in_check(after.white_to_move):
            return Status.win(0)
        return Status.draw()
    if m.promo in (BISHOP, KNIGHT):
        return Status.draw()
    if any(r.to == m.to for r in replies):
        return Status.draw()
    return Status.win(0)


def goal_after(before: Board, m: Move, after: Board) -> Optional[str]:
    """Is a position, reached in a game, the end of a king-and-pawn drill by a goal?"""
    from normalize import categorize

    nb = normalize(before)
    if nb.cat == Cat.Kpk:
        g = edge_goal(nb, m, before)
        if g is not None:
            if g.is_win():
                return GameResult.BlackWin if nb.t.flip else GameResult.WhiteWin
            return GameResult.Draw
    cat = categorize(after)
    if cat == Cat.DeadDraw:
        return GameResult.Draw
    if not after.legal_moves():
        if after.in_check(after.white_to_move):
            return (
                GameResult.BlackWin
                if after.white_to_move
                else GameResult.WhiteWin
            )
        return GameResult.Draw
    return None
