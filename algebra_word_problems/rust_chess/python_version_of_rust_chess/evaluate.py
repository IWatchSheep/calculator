"""Lists 1 and 2 (Steps 8 through 11): the present game only."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence

from board import KING, Board, Move
from exchange import Exchange, evaluate as exchange_evaluate
from strategies import NAMES, Ctx, TurnInfo, read_all, score_now, stage_rank


@dataclass
class List1Row:
    id: int
    name: str
    flags: int
    score: int


def sort_rows(rows: List[List1Row]) -> None:
    rows.sort(key=lambda a: (stage_rank(a.score), -a.score, a.name))


def list1(b: Board, white: bool, window: Sequence[TurnInfo]) -> List[List1Row]:
    ctx = Ctx(b=b, white=white, window=list(window))
    rows: List[List1Row] = []
    for i, r in enumerate(read_all(ctx)):
        f = r.flags()
        score = score_now(f)
        if score == 0:
            continue
        rows.append(List1Row(id=i, name=NAMES[i], flags=f, score=score))
    sort_rows(rows)
    return rows


@dataclass
class List2Row:
    strategy: str
    mv: Move
    san: str
    piece: int
    victim: int
    from_: int
    victim_sq: int
    exchange: Exchange


def list2(b: Board, white: bool, window: Sequence[TurnInfo]) -> List[List2Row]:
    if b.white_to_move != white:
        return []
    ctx = Ctx(b=b, white=white, window=list(window))
    readings = read_all(ctx)
    captures = [m for m in b.legal_moves() if b.is_capture(m)]
    rows: List[List2Row] = []
    for i, r in enumerate(readings):
        if score_now(r.flags()) == 0:
            continue
        for m in captures:
            vs = b.captured_sq(m)
            if abs(b.sq[vs]) == KING:
                continue
            frm = getattr(m, "from_", None)
            if frm is None:
                frm = getattr(m, "from")
            if frm in r.participants and vs in r.targets:
                rows.append(
                    List2Row(
                        strategy=NAMES[i],
                        mv=m,
                        san=b.san(m),
                        piece=b.sq[frm],
                        victim=b.captured_piece(m),
                        from_=frm,
                        victim_sq=vs,
                        exchange=exchange_evaluate(b, m),
                    )
                )
    rows.sort(
        key=lambda a: (
            -a.exchange.net(),
            -a.exchange.gain,
            a.exchange.loss,
            a.strategy,
            a.san,
            a.victim_sq,
        )
    )
    return rows
