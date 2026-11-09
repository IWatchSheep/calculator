"""Step 15.3: position keys, with color and mirror folded in for the two endgames."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from board import (
    KING,
    NO_SQ,
    PAWN,
    QUEEN,
    ROOK,
    Board,
    Move,
    file_of,
    parse_sq,
    piece_char,
    rank_of,
    sq_name,
)


class Cat(Enum):
    """Position category for folding and proof."""

    Kpk = "kpk"  # King and pawn against king.
    Krk = "krk"  # King and rook against king.
    Kqk = "kqk"  # King and queen against king (only reached by promotion here).
    DeadDraw = "dead"  # King against king, or king and bishop or knight against king.
    Other = "other"  # Any other position.

    def code(self) -> str:
        return self.value

    @staticmethod
    def from_code(s: str) -> Cat:
        for c in Cat:
            if c.value == s:
                return c
        return Cat.Other

    def proof_family(self) -> bool:
        """The two endgames where results are proven."""
        return self in (Cat.Kpk, Cat.Krk)

    def folded(self) -> bool:
        """Endgames whose positions are flipped and mirrored."""
        return self != Cat.Other


def categorize(b: Board) -> Cat:
    # A position that still has castling rights is not folded.
    if b.castling != 0:
        return Cat.Other
    others = [p for p in b.sq if p != 0 and abs(p) != KING]
    n = len(others)
    if n == 0:
        return Cat.DeadDraw
    if n == 1:
        a = abs(others[0])
        if a == PAWN:
            return Cat.Kpk
        if a == ROOK:
            return Cat.Krk
        if a == QUEEN:
            return Cat.Kqk
        return Cat.DeadDraw
    return Cat.Other


@dataclass(frozen=True)
class Transform:
    flip: bool = False
    mirror: bool = False

    def sq(self, s: int) -> int:
        f = file_of(s)
        r = rank_of(s)
        if self.flip:
            r = 7 - r
        if self.mirror:
            f = 7 - f
        return r * 8 + f

    def mv(self, m: Move) -> Move:
        """The transform is its own inverse."""
        return Move(from_=self.sq(m.from_), to=self.sq(m.to), promo=m.promo)

    def board(self, b: Board) -> Board:
        if not self.flip and not self.mirror:
            return b.copy()
        n = Board.empty()
        for s in range(64):
            p = b.sq[s]
            if p != 0:
                n.sq[self.sq(s)] = -p if self.flip else p
        n.white_to_move = (not b.white_to_move) if self.flip else b.white_to_move
        # Folded endgames have no castling rights and no en passant.
        n.castling = 0
        n.ep = NO_SQ
        n.halfmove = b.halfmove
        n.fullmove = b.fullmove
        return n

    def move_text(self, uci: str) -> str:
        if not self.flip and not self.mirror:
            return uci
        frm = parse_sq(uci[0:2])
        to = parse_sq(uci[2:4])
        if frm is None:
            frm = 0
        if to is None:
            to = 0
        return f"{sq_name(self.sq(frm))}{sq_name(self.sq(to))}{uci[4:]}"


Transform.IDENTITY = Transform(flip=False, mirror=False)


@dataclass
class Normalized:
    board: Board
    t: Transform
    cat: Cat

    def key(self) -> str:
        return self.board.key()


def normalize(b: Board) -> Normalized:
    """Fold color and mirror for the endgames; leave any other position as it is."""
    cat = categorize(b)
    if not cat.folded():
        return Normalized(board=b.copy(), t=Transform.IDENTITY, cat=cat)
    piece_sq = next(
        (s for s in range(64) if b.sq[s] != 0 and abs(b.sq[s]) != KING),
        None,
    )
    flip = piece_sq is not None and b.sq[piece_sq] < 0
    step1 = Transform(flip=flip, mirror=False)
    fb = step1.board(b)
    if cat == Cat.Kpk:
        ps = next((s for s in range(64) if fb.sq[s] == PAWN), 0)
        mirror = file_of(ps) >= 4
    elif cat in (Cat.Krk, Cat.Kqk):
        mirror = file_of(fb.king_sq(True)) >= 4
    else:
        mirror = False
    t = Transform(flip=flip, mirror=mirror)
    return Normalized(board=t.board(b), t=t, cat=cat)


def counted_legal(b: Board) -> bool:
    """Legal in the counted sense of Step 15.3: pieces on different squares,
    kings not adjacent, the side not to move not in check."""
    wk = b.king_sq(True)
    bk = b.king_sq(False)
    if wk == NO_SQ or bk == NO_SQ:
        return False
    if abs(file_of(wk) - file_of(bk)) <= 1 and abs(rank_of(wk) - rank_of(bk)) <= 1:
        return False
    return not b.in_check(not b.white_to_move)


def kpk_positions(folded: bool) -> List[Board]:
    """Every counted king-and-pawn position with White's pawn on ranks 2 through 7.
    With `folded`, only pawn files a through d."""
    out: List[Board] = []
    for ps in range(8, 56):
        if folded and file_of(ps) >= 4:
            continue
        pf, pr = file_of(ps), rank_of(ps)
        for wk in range(64):
            if wk == ps:
                continue
            wf, wr = file_of(wk), rank_of(wk)
            for bk in range(64):
                if bk == ps or bk == wk:
                    continue
                bf, br = file_of(bk), rank_of(bk)
                # kings not adjacent
                if abs(wf - bf) <= 1 and abs(wr - br) <= 1:
                    continue
                for stm in (True, False):
                    # side not to move must not be in check (only the pawn can check)
                    if stm:
                        # black not to move: white pawn attacks black king?
                        if br == pr + 1 and abs(bf - pf) == 1:
                            continue
                    else:
                        # white not to move: black has no pawn; only black king could
                        # "check" white, but kings are not adjacent, so white is safe.
                        pass
                    b = Board.empty()
                    b.sq[ps] = PAWN
                    b.sq[wk] = KING
                    b.sq[bk] = -KING
                    b.white_to_move = stm
                    out.append(b)
    return out


def similar_key(n: Normalized) -> Optional[str]:
    """Similar-position key for king and pawn against king (Step 12).

    Signed distances of both kings from the pawn, the pawn's rank, whether the
    pawn is on a rook file, and the side to move. Read on the normalized board.
    """
    if n.cat != Cat.Kpk:
        return None
    b = n.board
    ps = next((s for s in range(64) if b.sq[s] == PAWN), None)
    if ps is None:
        return None
    wk = b.king_sq(True)
    bk = b.king_sq(False)

    def d(k: int) -> tuple[int, int]:
        return (file_of(k) - file_of(ps), rank_of(k) - rank_of(ps))

    wf, wr = d(wk)
    bf, br = d(bk)
    rook_file = file_of(ps) == 0 or file_of(ps) == 7
    return (
        f"w{wf},{wr} b{bf},{br} r{rank_of(ps) + 1} "
        f"{'rookfile' if rook_file else 'inner'} "
        f"{'w' if b.white_to_move else 'b'}"
    )


def relative_move(b: Board, m: Move) -> str:
    """A move described relative to its own start, for similar positions."""
    p = b.sq[m.from_]
    promo = piece_char(-m.promo) if m.promo != 0 else ""
    df = file_of(m.to) - file_of(m.from_)
    dr = rank_of(m.to) - rank_of(m.from_)
    return f"{piece_char(p)}{df:+d}{dr:+d}{promo}"
