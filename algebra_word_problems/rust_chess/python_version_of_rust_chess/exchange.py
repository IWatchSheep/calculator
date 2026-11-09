"""Capture valuation (Step 14.3), used by List 2."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Tuple

from board import QUEEN, KING, Board, Move, piece_value

MATE_BONUS = 100_000


@dataclass(frozen=True)
class Exchange:
    gain: int
    loss: int

    def net(self) -> int:
        return self.gain - self.loss


def _move_from(m: Move) -> int:
    v = getattr(m, "from_", None)
    if v is None:
        v = getattr(m, "from")
    return v


def step_value(b: Board, m: Move) -> Tuple[int, bool]:
    """Value of one step: the piece taken, plus a promotion bonus, plus a mate bonus."""
    if b.is_en_passant(m):
        v = 100
    else:
        v = piece_value(b.captured_piece(m))
    if m.promo != 0:
        v += piece_value(m.promo) - 100
    after = b.make(m)
    mate = after.is_checkmate()
    if mate:
        v += MATE_BONUS
    return v, mate


def cheapest_recapture(b: Board, target: int) -> Optional[Move]:
    """The cheapest legal recapture on `target`.

    A promoting pawn counts as a pawn, and promotes to a queen.
    """
    best: Optional[Tuple[int, Move]] = None
    for m in b.legal_moves():
        if m.to != target or not b.is_capture(m) or (m.promo != 0 and m.promo != QUEEN):
            continue
        p = b.sq[_move_from(m)]
        order = 10_000 if abs(p) == KING else piece_value(p)
        if best is None or order < best[0]:
            best = (order, m)
    return None if best is None else best[1]


def evaluate(b: Board, m: Move) -> Exchange:
    """Evaluate playing `m` and the exchange that follows on its landing square.

    The first move is always played; each later recapture may be declined, and
    an exchange stops when continuing would give an equal net value.
    """
    values: List[int] = []
    v0, mate0 = step_value(b, m)
    values.append(v0)
    cur = b.make(m)
    target = m.to
    if not mate0:
        for _ in range(32):
            r = cheapest_recapture(cur, target)
            if r is None:
                break
            v, mate = step_value(cur, r)
            values.append(v)
            cur = cur.make(r)
            if mate:
                break
    # best[k]: what the side making step k nets by playing it and then playing on well.
    n = len(values)
    best = [0] * (n + 1)
    for k in range(n - 1, -1, -1):
        nxt = best[k + 1] if k + 1 < n else 0
        best[k] = values[k] - max(nxt, 0)
    gain = 0
    loss = 0
    for k in range(n):
        if k > 0 and best[k] <= 0:
            break
        if k % 2 == 0:
            gain += values[k]
        else:
            loss += values[k]
    return Exchange(gain=gain, loss=loss)
