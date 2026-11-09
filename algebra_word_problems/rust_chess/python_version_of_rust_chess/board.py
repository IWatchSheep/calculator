"""Board, legal move generation, SAN, check, mate and draws.

Squares are numbered a1 = 0, b1 = 1, ..., h1 = 7, a2 = 8, ..., h8 = 63.
Pieces are signed: 1 pawn, 2 knight, 3 bishop, 4 rook, 5 queen, 6 king.
White pieces are positive, Black pieces negative, 0 is an empty square.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator, List, Optional, Tuple

PAWN: int = 1
KNIGHT: int = 2
BISHOP: int = 3
ROOK: int = 4
QUEEN: int = 5
KING: int = 6

CASTLE_WK: int = 1
CASTLE_WQ: int = 2
CASTLE_BK: int = 4
CASTLE_BQ: int = 8

NO_SQ: int = 255

START_FEN: str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

KNIGHT_D: Tuple[Tuple[int, int], ...] = (
    (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2),
)
KING_D: Tuple[Tuple[int, int], ...] = (
    (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1),
)
BISHOP_D: Tuple[Tuple[int, int], ...] = ((1, 1), (1, -1), (-1, 1), (-1, -1))
ROOK_D: Tuple[Tuple[int, int], ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


def file_of(sq: int) -> int:
    return sq % 8


def rank_of(sq: int) -> int:
    return sq // 8


def make_sq(file: int, rank: int) -> Optional[int]:
    if 0 <= file < 8 and 0 <= rank < 8:
        return rank * 8 + file
    return None


def sq_name(sq: int) -> str:
    return chr(ord("a") + (sq % 8)) + chr(ord("1") + (sq // 8))


def parse_sq(s: str) -> Optional[int]:
    if len(s) != 2:
        return None
    f = s[0].lower()
    r = s[1]
    if not ("a" <= f <= "h") or not ("1" <= r <= "8"):
        return None
    return (ord(r) - ord("1")) * 8 + (ord(f) - ord("a"))


def piece_char(p: int) -> str:
    c = {
        PAWN: "p",
        KNIGHT: "n",
        BISHOP: "b",
        ROOK: "r",
        QUEEN: "q",
        KING: "k",
    }.get(abs(p), ".")
    return c.upper() if p > 0 else c


def piece_name(p: int) -> str:
    return {
        PAWN: "pawn",
        KNIGHT: "knight",
        BISHOP: "bishop",
        ROOK: "rook",
        QUEEN: "queen",
        KING: "king",
    }.get(abs(p), "none")


def piece_value(p: int) -> int:
    """Values from Step 14.3. The king has no capture value."""
    return {
        PAWN: 100,
        KNIGHT: 320,
        BISHOP: 330,
        ROOK: 500,
        QUEEN: 900,
    }.get(abs(p), 0)


@dataclass(frozen=True, slots=True)
class Move:
    """A chess move. Rust field `from` is `from_` here (`from` is a Python keyword)."""

    from_: int
    to: int
    promo: int = 0  # promotion piece type (2..=5), or 0

    def uci(self) -> str:
        s = f"{sq_name(self.from_)}{sq_name(self.to)}"
        if self.promo != 0:
            s += piece_char(-self.promo)
        return s


def promo_rank(p: int) -> int:
    """Promotion order used by the Step 4 listing: queen, rook, bishop, knight."""
    return {QUEEN: 0, ROOK: 1, BISHOP: 2, KNIGHT: 3}.get(p, 4)


def listing_key(m: Move) -> Tuple[int, int, int]:
    """Step 4 listing order: origin a1..h8, then destination a1..h8, then Q/R/B/N."""
    return (m.from_, m.to, promo_rank(m.promo))


@dataclass
class Board:
    sq: List[int] = field(default_factory=lambda: [0] * 64)
    white_to_move: bool = True
    castling: int = 0
    ep: int = NO_SQ
    halfmove: int = 0
    fullmove: int = 1

    def copy(self) -> Board:
        return Board(
            sq=self.sq[:],
            white_to_move=self.white_to_move,
            castling=self.castling,
            ep=self.ep,
            halfmove=self.halfmove,
            fullmove=self.fullmove,
        )

    def __copy__(self) -> Board:
        return self.copy()

    def __deepcopy__(self, memo: dict) -> Board:
        return self.copy()

    @staticmethod
    def empty() -> Board:
        return Board(sq=[0] * 64, white_to_move=True, castling=0, ep=NO_SQ, halfmove=0, fullmove=1)

    @staticmethod
    def start() -> Board:
        return Board.from_fen(START_FEN)

    @staticmethod
    def from_fen(fen: str) -> Board:
        parts = fen.split()
        if len(parts) < 2:
            raise ValueError("a FEN needs at least the placement and the side to move")
        b = Board.empty()
        rows = parts[0].split("/")
        if len(rows) != 8:
            raise ValueError("the placement needs 8 ranks")
        for i, row in enumerate(rows):
            rank = 7 - i
            file = 0
            for c in row:
                if c.isdigit():
                    file += int(c)
                    continue
                t = {
                    "p": PAWN,
                    "n": KNIGHT,
                    "b": BISHOP,
                    "r": ROOK,
                    "q": QUEEN,
                    "k": KING,
                }.get(c.lower())
                if t is None:
                    raise ValueError(f"unknown piece '{c}'")
                s = make_sq(file, rank)
                if s is None:
                    raise ValueError("a rank has too many squares")
                b.sq[s] = t if c.isupper() else -t
                file += 1
            if file != 8:
                raise ValueError("a rank does not have 8 squares")
        if parts[1] == "w":
            b.white_to_move = True
        elif parts[1] == "b":
            b.white_to_move = False
        else:
            raise ValueError("side to move must be w or b")
        if len(parts) > 2:
            for c in parts[2]:
                b.castling |= {
                    "K": CASTLE_WK,
                    "Q": CASTLE_WQ,
                    "k": CASTLE_BK,
                    "q": CASTLE_BQ,
                }.get(c, 0)
        if len(parts) > 3 and parts[3] != "-":
            ep = parse_sq(parts[3])
            if ep is None:
                raise ValueError("bad en passant square")
            b.ep = ep
        if len(parts) > 4:
            try:
                b.halfmove = int(parts[4])
            except ValueError:
                b.halfmove = 0
        if len(parts) > 5:
            try:
                b.fullmove = int(parts[5])
            except ValueError:
                b.fullmove = 1
        wk = sum(1 for p in b.sq if p == KING)
        bk = sum(1 for p in b.sq if p == -KING)
        if wk != 1 or bk != 1:
            raise ValueError("each side needs exactly one king")
        b.fix_castling()
        return b

    def fix_castling(self) -> None:
        """Drop castling rights whose king or rook is not on its home square."""
        if self.sq[4] != KING:
            self.castling &= ~(CASTLE_WK | CASTLE_WQ)
        if self.sq[7] != ROOK:
            self.castling &= ~CASTLE_WK
        if self.sq[0] != ROOK:
            self.castling &= ~CASTLE_WQ
        if self.sq[60] != -KING:
            self.castling &= ~(CASTLE_BK | CASTLE_BQ)
        if self.sq[63] != -ROOK:
            self.castling &= ~CASTLE_BK
        if self.sq[56] != -ROOK:
            self.castling &= ~CASTLE_BQ

    def to_fen(self) -> str:
        ranks: List[str] = []
        for rank in range(7, -1, -1):
            empty = 0
            row: List[str] = []
            for file in range(8):
                p = self.sq[rank * 8 + file]
                if p == 0:
                    empty += 1
                else:
                    if empty > 0:
                        row.append(str(empty))
                        empty = 0
                    row.append(piece_char(p))
            if empty > 0:
                row.append(str(empty))
            ranks.append("".join(row))
        ep = "-" if self.ep == NO_SQ else sq_name(self.ep)
        side = "w" if self.white_to_move else "b"
        return f"{'/'.join(ranks)} {side} {self.castling_str()} {ep} {self.halfmove} {self.fullmove}"

    def castling_str(self) -> str:
        c = ""
        if self.castling & CASTLE_WK:
            c += "K"
        if self.castling & CASTLE_WQ:
            c += "Q"
        if self.castling & CASTLE_BK:
            c += "k"
        if self.castling & CASTLE_BQ:
            c += "q"
        return c if c else "-"

    def king_sq(self, white: bool) -> int:
        k = KING if white else -KING
        for i, p in enumerate(self.sq):
            if p == k:
                return i
        return NO_SQ

    def _own(self, p: int, white: bool) -> bool:
        return p > 0 if white else p < 0

    def attacked_by(self, target: int, by_white: bool) -> bool:
        """Is `target` attacked by any piece of the given color (geometric attack)?"""
        sq = self.sq
        tf = target & 7
        tr = target >> 3
        pawn = PAWN if by_white else -PAWN
        direction = -1 if by_white else 1
        for df in (-1, 1):
            f = tf + df
            r = tr + direction
            if 0 <= f < 8 and 0 <= r < 8 and sq[r * 8 + f] == pawn:
                return True
        knight = KNIGHT if by_white else -KNIGHT
        for df, dr in KNIGHT_D:
            f = tf + df
            r = tr + dr
            if 0 <= f < 8 and 0 <= r < 8 and sq[r * 8 + f] == knight:
                return True
        king = KING if by_white else -KING
        for df, dr in KING_D:
            f = tf + df
            r = tr + dr
            if 0 <= f < 8 and 0 <= r < 8 and sq[r * 8 + f] == king:
                return True
        for dirs, kinds in ((BISHOP_D, (BISHOP, QUEEN)), (ROOK_D, (ROOK, QUEEN))):
            for df, dr in dirs:
                f = tf + df
                r = tr + dr
                while 0 <= f < 8 and 0 <= r < 8:
                    p = sq[r * 8 + f]
                    if p != 0:
                        if self._own(p, by_white) and abs(p) in kinds:
                            return True
                        break
                    f += df
                    r += dr
        return False

    def attackers(self, target: int, by_white: bool) -> Iterator[int]:
        """Squares of pieces of `by_white` color that attack `target` geometrically."""
        out: List[int] = []
        tf = file_of(target)
        tr = rank_of(target)
        direction = -1 if by_white else 1
        for df in (-1, 1):
            s = make_sq(tf + df, tr + direction)
            if s is not None and self.sq[s] == (PAWN if by_white else -PAWN):
                out.append(s)
        for df, dr in KNIGHT_D:
            s = make_sq(tf + df, tr + dr)
            if s is not None and self.sq[s] == (KNIGHT if by_white else -KNIGHT):
                out.append(s)
        for df, dr in KING_D:
            s = make_sq(tf + df, tr + dr)
            if s is not None and self.sq[s] == (KING if by_white else -KING):
                out.append(s)
        for dirs, kinds in ((BISHOP_D, (BISHOP, QUEEN)), (ROOK_D, (ROOK, QUEEN))):
            for df, dr in dirs:
                f = tf + df
                r = tr + dr
                while True:
                    s = make_sq(f, r)
                    if s is None:
                        break
                    p = self.sq[s]
                    if p != 0:
                        if self._own(p, by_white) and abs(p) in kinds:
                            out.append(s)
                        break
                    f += df
                    r += dr
        return iter(out)

    def attacks_from(self, from_sq: int) -> List[int]:
        """Squares attacked by the piece on `from_sq` (geometric, ignores pins)."""
        p = self.sq[from_sq]
        out: List[int] = []
        if p == 0:
            return out
        f0 = file_of(from_sq)
        r0 = rank_of(from_sq)
        kind = abs(p)
        if kind == PAWN:
            direction = 1 if p > 0 else -1
            for df in (-1, 1):
                s = make_sq(f0 + df, r0 + direction)
                if s is not None:
                    out.append(s)
        elif kind == KNIGHT:
            for df, dr in KNIGHT_D:
                s = make_sq(f0 + df, r0 + dr)
                if s is not None:
                    out.append(s)
        elif kind == KING:
            for df, dr in KING_D:
                s = make_sq(f0 + df, r0 + dr)
                if s is not None:
                    out.append(s)
        else:
            dirs: List[Tuple[int, int]] = []
            if kind in (BISHOP, QUEEN):
                dirs.extend(BISHOP_D)
            if kind in (ROOK, QUEEN):
                dirs.extend(ROOK_D)
            for df, dr in dirs:
                f = f0 + df
                r = r0 + dr
                while True:
                    s = make_sq(f, r)
                    if s is None:
                        break
                    out.append(s)
                    if self.sq[s] != 0:
                        break
                    f += df
                    r += dr
        return out

    def in_check(self, white: bool) -> bool:
        k = self.king_sq(white)
        return k != NO_SQ and self.attacked_by(k, not white)

    def occupied(self) -> List[int]:
        return [i for i, p in enumerate(self.sq) if p != 0]

    def _pseudo_moves(self, out: List[Move]) -> None:
        white = self.white_to_move
        for from_sq in self.occupied():
            p = self.sq[from_sq]
            if not self._own(p, white):
                continue
            f0 = file_of(from_sq)
            r0 = rank_of(from_sq)
            kind = abs(p)
            if kind == PAWN:
                direction = 1 if white else -1
                start_rank = 1 if white else 6
                last_rank = 7 if white else 0

                def push(to: int, frm: int = from_sq, lr: int = last_rank) -> None:
                    if rank_of(to) == lr:
                        for pr in (QUEEN, ROOK, BISHOP, KNIGHT):
                            out.append(Move(from_=frm, to=to, promo=pr))
                    else:
                        out.append(Move(from_=frm, to=to, promo=0))

                one = make_sq(f0, r0 + direction)
                if one is not None and self.sq[one] == 0:
                    push(one)
                    if r0 == start_rank:
                        two = make_sq(f0, r0 + 2 * direction)
                        if two is not None and self.sq[two] == 0:
                            out.append(Move(from_=from_sq, to=two, promo=0))
                for df in (-1, 1):
                    to = make_sq(f0 + df, r0 + direction)
                    if to is not None:
                        q = self.sq[to]
                        if (q != 0 and not self._own(q, white)) or to == self.ep:
                            push(to)
            elif kind in (KNIGHT, KING):
                ds = KNIGHT_D if kind == KNIGHT else KING_D
                for df, dr in ds:
                    to = make_sq(f0 + df, r0 + dr)
                    if to is not None:
                        q = self.sq[to]
                        if q == 0 or not self._own(q, white):
                            out.append(Move(from_=from_sq, to=to, promo=0))
                if kind == KING:
                    self._castle_moves(white, out)
            else:
                dirs: List[Tuple[int, int]] = []
                if kind in (BISHOP, QUEEN):
                    dirs.extend(BISHOP_D)
                if kind in (ROOK, QUEEN):
                    dirs.extend(ROOK_D)
                for df, dr in dirs:
                    f = f0 + df
                    r = r0 + dr
                    while True:
                        to = make_sq(f, r)
                        if to is None:
                            break
                        q = self.sq[to]
                        if q == 0:
                            out.append(Move(from_=from_sq, to=to, promo=0))
                        else:
                            if not self._own(q, white):
                                out.append(Move(from_=from_sq, to=to, promo=0))
                            break
                        f += df
                        r += dr

    def _castle_moves(self, white: bool, out: List[Move]) -> None:
        if white:
            kbit, qbit, ksq = CASTLE_WK, CASTLE_WQ, 4
        else:
            kbit, qbit, ksq = CASTLE_BK, CASTLE_BQ, 60
        if self.sq[ksq] != (KING if white else -KING):
            return
        if self.in_check(white):
            return
        if (
            self.castling & kbit
            and self.sq[ksq + 1] == 0
            and self.sq[ksq + 2] == 0
            and not self.attacked_by(ksq + 1, not white)
            and not self.attacked_by(ksq + 2, not white)
        ):
            out.append(Move(from_=ksq, to=ksq + 2, promo=0))
        if (
            self.castling & qbit
            and self.sq[ksq - 1] == 0
            and self.sq[ksq - 2] == 0
            and self.sq[ksq - 3] == 0
            and not self.attacked_by(ksq - 1, not white)
            and not self.attacked_by(ksq - 2, not white)
        ):
            out.append(Move(from_=ksq, to=ksq - 2, promo=0))

    def legal_moves(self) -> List[Move]:
        """All legal moves, in the Step 4 listing order."""
        pseudo: List[Move] = []
        self._pseudo_moves(pseudo)
        white = self.white_to_move
        legal = [m for m in pseudo if not self.make(m).in_check(white)]
        legal.sort(key=listing_key)
        return legal

    def legal_moves_for(self, white: bool) -> List[Move]:
        """Legal moves for `white` as if it were that side's turn."""
        if self.white_to_move == white:
            return self.legal_moves()
        b = self.copy()
        b.white_to_move = white
        b.ep = NO_SQ
        return b.legal_moves()

    def is_capture(self, m: Move) -> bool:
        return self.sq[m.to] != 0 or self.is_en_passant(m)

    def is_en_passant(self, m: Move) -> bool:
        return abs(self.sq[m.from_]) == PAWN and m.to == self.ep and file_of(m.from_) != file_of(m.to)

    def is_castle(self, m: Move) -> bool:
        return abs(self.sq[m.from_]) == KING and abs(file_of(m.from_) - file_of(m.to)) == 2

    def captured_piece(self, m: Move) -> int:
        """The piece captured by `m` (0 if none)."""
        if self.is_en_passant(m):
            return -PAWN if self.white_to_move else PAWN
        return self.sq[m.to]

    def captured_sq(self, m: Move) -> int:
        """Square of the piece captured by `m` (differs from `to` for en passant)."""
        if self.is_en_passant(m):
            return m.to - 8 if self.white_to_move else m.to + 8
        return m.to

    def make(self, m: Move) -> Board:
        """Returns the board after `m`. `m` must be at least pseudo-legal."""
        b = self.copy()
        p = b.sq[m.from_]
        white = p > 0
        capture = self.sq[m.to] != 0 or (
            self.ep != NO_SQ and abs(p) == PAWN and m.to == self.ep and file_of(m.from_) != file_of(m.to)
        )
        if self.ep != NO_SQ and abs(p) == PAWN and m.to == self.ep and file_of(m.from_) != file_of(m.to):
            b.sq[self.captured_sq(m)] = 0
        b.sq[m.to] = (m.promo if white else -m.promo) if m.promo != 0 else p
        b.sq[m.from_] = 0
        if self.castling and abs(p) == KING and abs(file_of(m.from_) - file_of(m.to)) == 2:
            if m.to > m.from_:
                rf, rt = m.from_ + 3, m.from_ + 1
            else:
                rf, rt = m.from_ - 4, m.from_ - 1
            b.sq[rt] = b.sq[rf]
            b.sq[rf] = 0
        b.ep = NO_SQ
        if abs(p) == PAWN and abs(rank_of(m.to) - rank_of(m.from_)) == 2:
            b.ep = (m.from_ + m.to) // 2
        if self.castling:
            b.fix_castling()
        else:
            b.castling = 0
        b.halfmove = 0 if abs(p) == PAWN or capture else self.halfmove + 1
        if not white:
            b.fullmove += 1
        b.white_to_move = not self.white_to_move
        return b

    def legal_ep(self) -> int:
        """The en passant square, but only when a legal en passant capture exists."""
        if self.ep == NO_SQ:
            return NO_SQ
        if any(self.is_en_passant(m) for m in self.legal_moves()):
            return self.ep
        return NO_SQ

    def is_checkmate(self) -> bool:
        return self.in_check(self.white_to_move) and not self.legal_moves()

    def is_stalemate(self) -> bool:
        return not self.in_check(self.white_to_move) and not self.legal_moves()

    def insufficient_material(self) -> bool:
        """King against king, or king and one minor piece against king."""
        minors = 0
        for p in self.sq:
            a = abs(p)
            if a in (0, KING):
                continue
            if a in (KNIGHT, BISHOP):
                minors += 1
            else:
                return False
        return minors <= 1

    def san(self, m: Move) -> str:
        """Standard Algebraic Notation for a legal move."""
        p = self.sq[m.from_]
        s = ""
        if self.is_castle(m):
            s = "O-O" if m.to > m.from_ else "O-O-O"
        elif abs(p) == PAWN:
            if self.is_capture(m):
                s += chr(ord("a") + (m.from_ % 8))
                s += "x"
            s += sq_name(m.to)
            if m.promo != 0:
                s += "=" + piece_char(m.promo)
        else:
            s += piece_char(abs(p))
            others = [
                o
                for o in self.legal_moves()
                if o.to == m.to and o.from_ != m.from_ and self.sq[o.from_] == p
            ]
            if others:
                same_file = any(file_of(o.from_) == file_of(m.from_) for o in others)
                same_rank = any(rank_of(o.from_) == rank_of(m.from_) for o in others)
                if not same_file:
                    s += chr(ord("a") + (m.from_ % 8))
                elif not same_rank:
                    s += chr(ord("1") + (m.from_ // 8))
                else:
                    s += sq_name(m.from_)
            if self.is_capture(m):
                s += "x"
            s += sq_name(m.to)
        after = self.make(m)
        if after.in_check(after.white_to_move):
            s += "#" if not after.legal_moves() else "+"
        return s

    def parse_move(self, text: str) -> Optional[Move]:
        """Parse a move typed as from-to coordinates ("e2e4", "e7e8q") or as SAN."""
        t = text.strip()
        legal = self.legal_moves()
        lower = t.lower()
        if len(lower) >= 4:
            f = parse_sq(lower[0:2])
            to = parse_sq(lower[2:4])
            if f is not None and to is not None:
                promo_ch = lower[4] if len(lower) > 4 else ""
                promo = {"q": QUEEN, "r": ROOK, "b": BISHOP, "n": KNIGHT}.get(promo_ch, 0)
                for m in legal:
                    if m.from_ == f and m.to == to and (m.promo == promo or (promo == 0 and m.promo == QUEEN)):
                        return m

        def clean(s: str) -> str:
            return s.rstrip("+#")

        cleaned = clean(t)
        for m in legal:
            if clean(self.san(m)) == cleaned:
                return m
        return None

    def ascii(self) -> str:
        s = ""
        for rank in range(7, -1, -1):
            s += f"{rank + 1} "
            for file in range(8):
                p = self.sq[rank * 8 + file]
                s += ("." if p == 0 else piece_char(p)) + " "
            s += "\n"
        s += "  a b c d e f g h\n"
        return s

    def key(self) -> str:
        """Position as a piece list, side to move, castling rights and en passant square.

        This is the key text used in listings and in the position index. It is not a FEN.
        """
        items: List[str] = []
        for i in range(64):
            p = self.sq[i]
            if p != 0:
                items.append(piece_char(p) + sq_name(i))
        ep = self.legal_ep()
        side = "w" if self.white_to_move else "b"
        ep_s = "-" if ep == NO_SQ else sq_name(ep)
        return f"{','.join(items)}|{side}|{self.castling_str()}|{ep_s}"

    @staticmethod
    def from_key(key: str) -> Board:
        """Rebuild a board from `key()` text (clocks are not part of the key)."""
        parts = key.split("|")
        if len(parts) != 4:
            raise ValueError("a key has four parts")
        b = Board.empty()
        if parts[0]:
            for item in parts[0].split(","):
                if not item:
                    continue
                c = item[0]
                s = parse_sq(item[1:])
                if s is None:
                    raise ValueError("bad square in key")
                t = {
                    "p": PAWN,
                    "n": KNIGHT,
                    "b": BISHOP,
                    "r": ROOK,
                    "q": QUEEN,
                    "k": KING,
                }.get(c.lower())
                if t is None:
                    raise ValueError("bad piece in key")
                b.sq[s] = t if c.isupper() else -t
        b.white_to_move = parts[1] == "w"
        for c in parts[2]:
            b.castling |= {
                "K": CASTLE_WK,
                "Q": CASTLE_WQ,
                "k": CASTLE_BK,
                "q": CASTLE_BQ,
            }.get(c, 0)
        if parts[3] == "-":
            b.ep = NO_SQ
        else:
            ep = parse_sq(parts[3])
            if ep is None:
                raise ValueError("bad ep")
            b.ep = ep
        return b

    def count(self, p: int) -> int:
        return sum(1 for q in self.sq if q == p)


def perft(b: Board, depth: int) -> int:
    """Count legal move sequences to `depth`. Writes nothing and fills no list."""
    if depth == 0:
        return 1
    moves = b.legal_moves()
    if depth == 1:
        return len(moves)
    return sum(perft(b.make(m), depth - 1) for m in moves)
