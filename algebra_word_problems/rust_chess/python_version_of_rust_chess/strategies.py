"""The 20 strategy templates of Step 14.4.

Each template reads the board (geometric attacks) and the evaluated
player's turn window, and reports whether its foundation, progress and
completion conditions are met. It also names the participating pieces and
the target squares, which Step 14.3 rule 8 uses to tie captures to a
strategy.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Sequence, Tuple

from board import (
    BISHOP,
    CASTLE_BK,
    CASTLE_BQ,
    CASTLE_WK,
    CASTLE_WQ,
    KING,
    KNIGHT,
    NO_SQ,
    PAWN,
    QUEEN,
    ROOK,
    Board,
    file_of,
    make_sq,
    piece_value,
    rank_of,
)

NAMES: Tuple[str, ...] = (
    "Central Pawn Occupation",
    "Central Pawn Break",
    "Kingside Pawn Storm",
    "Queenside Minority Attack",
    "King Shelter",
    "Opposite-Side Castling Attack",
    "Fianchetto",
    "Open-File Control",
    "Seventh-Rank Invasion",
    "Passed-Pawn Advance",
    "Isolated-Pawn Attack",
    "Backward-Pawn Pressure",
    "Knight Outpost",
    "Bishop Pair",
    "Pin",
    "Discovered Attack",
    "Fork",
    "Skewer",
    "Major-Piece Battery",
    "Promotion",
)

DESCRIPTIONS: Tuple[Tuple[str, str, str], ...] = (
    (
        "A friendly pawn occupies the d-file or e-file.",
        "A friendly pawn occupies d4 or e4 for White, or d5 or e5 for Black.",
        "Both central squares are occupied by friendly pawns, and both pawns are defended.",
    ),
    (
        "The opponent has a central pawn, and a friendly pawn remains on a file from c through f.",
        "A friendly pawn attacks an opposing central pawn.",
        "The turn window contains a pawn capturing another pawn on the c-, d-, e-, or f-file.",
    ),
    (
        "At least two friendly pawns remain on the f-, g-, or h-file, at least one has moved, and the friendly king is outside those files.",
        "A participating pawn reaches relative rank 2.",
        "Two participating pawns reach relative rank 3 or higher, and the friendly king occupies a file from a through d.",
    ),
    (
        "The evaluated player has fewer pawns than the opponent on the a-, b-, and c-files, while retaining at least one pawn on those files.",
        "A friendly queenside pawn reaches relative rank 2.",
        "A participating pawn reaches relative rank 3, and an opposing pawn on the a- through d-files is isolated or doubled.",
    ),
    (
        "The king is on e1 or e8 with a remaining castling right, or is already on c1, g1, c8, or g8.",
        "The king has castled, or no more than one piece remains between the king and a castling rook.",
        "The king occupies a castled square, is not attacked, and its three shelter pawns remain unmoved.",
    ),
    (
        "The friendly king occupies the home rank on the a-c or f-h files, while the opposing king occupies the opposite wing.",
        "A friendly pawn on the opposing king's wing reaches relative rank 2.",
        "That pawn reaches relative rank 3, and a friendly rook or queen occupies a half-open file on that wing.",
    ),
    (
        "The b-pawn or g-pawn has advanced one square, or a friendly bishop already occupies b2, g2, b7, or g7.",
        "A friendly bishop occupies one of those fianchetto squares.",
        "The bishop attacks at least one of the central squares d4, d5, e4, or e5.",
    ),
    (
        "At least one file contains no friendly pawn, and a friendly rook or queen remains on the board.",
        "A friendly rook or queen occupies a file without a friendly pawn.",
        "A fully open file contains more friendly major pieces than opposing major pieces.",
    ),
    (
        "A friendly rook or queen exists, and at least one file contains no friendly pawn.",
        "A friendly major piece reaches relative rank 5.",
        "A friendly rook or queen reaches the opponent's second rank and attacks an opposing piece or pawn.",
    ),
    (
        "A friendly pawn has no opposing pawn ahead of it on its own file or either adjacent file.",
        "The passed pawn reaches relative rank 3.",
        "The passed pawn reaches relative rank 5 or higher and is defended.",
    ),
    (
        "An opposing pawn has no friendly neighboring pawn on an adjacent file.",
        "A friendly piece attacks that opposing pawn, or a friendly rook or queen shares its file.",
        "The number of attacks against the isolated pawn exceeds the number of defenses.",
    ),
    (
        "An opposing pawn's advance square is attacked by a friendly pawn, is not defended by an opposing pawn, and lies on a file without a friendly pawn.",
        "A friendly rook or queen occupies the opposing pawn's file.",
        "That major piece remains on the file, and the opposing pawn's advance square is occupied or attacked.",
    ),
    (
        "A square on relative ranks 3 through 6 is empty or contains a friendly knight, is defended by a friendly pawn, and cannot still be attacked by an opposing pawn.",
        "A friendly knight occupies or attacks that square.",
        "A friendly knight occupies the outpost square.",
    ),
    (
        "The evaluated player has two bishops, while the opponent has fewer than two.",
        "At least one friendly bishop has moved away from the back rank.",
        "At least one file from c through f contains no pawns, and a friendly bishop has three squares of unobstructed travel.",
    ),
    (
        "A friendly bishop, rook, or queen aligns with an opposing front piece and a more valuable rear piece or king.",
        "The attacking line to the opposing front piece is unobstructed.",
        "The rear piece is the opposing king, or a second friendly piece also attacks the front piece.",
    ),
    (
        "Exactly one friendly piece stands between a friendly sliding piece and an opposing piece other than a pawn.",
        "The intervening friendly piece has a legal move that takes it off the attacking line.",
        "That move captures a piece or delivers check, while the sliding piece continues attacking the original target.",
    ),
    (
        "A piece's current square or a possible legal move creates attacks against two opposing pieces other than pawns.",
        "Two opposing target pieces are currently attacked.",
        "Both targets satisfy the strategy's value conditions (kings, undefended, or at least as valuable as the attacker).",
    ),
    (
        "A friendly sliding piece aligns with two opposing pieces, and the nearer opposing piece is at least as valuable as the farther piece.",
        "The line to the front opposing piece is unobstructed, and the front piece is the king or is strictly more valuable than the rear piece.",
        "The front piece is the king, or it is more valuable than the attacking sliding piece while the rear piece is undefended or worth at least as much as the attacker.",
    ),
    (
        "Two friendly rooks or queens share a rank or file, no more than two pieces stand between them, and at least one participating major piece has moved from its original square.",
        "No more than one piece remains between the participating major pieces.",
        "The line between the participating pieces is clear, and they share a half-open file or one attacks an opposing piece along that line.",
    ),
    (
        "A friendly pawn reaches relative rank 4 or higher.",
        "The pawn reaches relative rank 5 or higher.",
        "The pawn has an available legal promotion move. A pawn blocked on the seventh rank remains at the progress stage until a legal promotion move becomes available.",
    ),
)


@dataclass
class TurnInfo:
    """One turn of the evaluated player's window (Step 5).

    `from_` mirrors Rust `from` (`from` is a Python keyword).
    """

    white: bool
    from_: int
    to: int
    piece: int
    captured: int


@dataclass
class Reading:
    foundation: bool = False
    progress: bool = False
    completion: bool = False
    participants: List[int] = field(default_factory=list)
    targets: List[int] = field(default_factory=list)

    def flags(self) -> int:
        """Three bits: foundation 1, progress 2, completion 4."""
        return (
            (1 if self.foundation else 0)
            | ((1 if self.progress else 0) << 1)
            | ((1 if self.completion else 0) << 2)
        )


F_FOUNDATION = 1
F_PROGRESS = 2
F_COMPLETION = 4


def score_now(flags: int) -> int:
    """Score from Step 14.2 for List 1 (no look-ahead): 100, 60, 30, or 0 when not listed."""
    if flags & F_COMPLETION:
        return 100
    if (flags & F_FOUNDATION) and (flags & F_PROGRESS):
        return 60
    if flags != 0:
        return 30
    return 0


def stage_name(score: int) -> str:
    if score == 100:
        return "Fully developed"
    if score in (60, 75):
        return "Partially developed"
    if score in (30, 45):
        return "Beginning to form"
    return "-"


def stage_rank(score: int) -> int:
    if score == 100:
        return 0
    if score in (60, 75):
        return 1
    if score in (30, 45):
        return 2
    return 3


def flags_to_text(f: Sequence[int]) -> str:
    """Flags as a compact text: 20 digits, each 0..7."""
    return "".join(chr(ord("0") + (d & 7)) for d in f)


def flags_to_sparse(f: Sequence[int]) -> str:
    """Sparse form for drill records: '-' or 'index=flags' pairs, e.g. '9=3,19=1'."""
    parts = [f"{i}={v}" for i, v in enumerate(f) if v != 0]
    return "-" if not parts else ",".join(parts)


def flags_from_sparse(s: str) -> List[int]:
    f = [0] * 20
    if not s or s == "-":
        return f
    for part in s.split(","):
        if "=" not in part:
            continue
        i_s, v_s = part.split("=", 1)
        try:
            i = int(i_s)
            v = int(v_s)
        except ValueError:
            continue
        if 0 <= i < 20:
            f[i] = v & 7
    return f


def flags_from_text(s: str) -> List[int]:
    f = [0] * 20
    for i, c in enumerate(s.encode("ascii", "ignore")[:20]):
        f[i] = max(0, c - ord("0")) & 7
    return f


@dataclass
class Ctx:
    b: Board
    white: bool
    window: Sequence[TurnInfo]


def friendly(p: int, white: bool) -> bool:
    return p > 0 if white else p < 0


def enemy(p: int, white: bool) -> bool:
    return p != 0 and not friendly(p, white)


def rel_rank(sq: int, white: bool) -> int:
    return rank_of(sq) if white else 7 - rank_of(sq)


def rel_sq(file: int, rrank: int, white: bool) -> int:
    """Square from a relative file and rank for the evaluated player."""
    r = rrank if white else 7 - rrank
    return r * 8 + file


def own(white: bool, t: int) -> int:
    return t if white else -t


def squares_of(b: Board, p: int) -> List[int]:
    return [s for s in range(64) if b.sq[s] == p]


def file_has(b: Board, file: int, p: int) -> bool:
    return any(b.sq[r * 8 + file] == p for r in range(8))


def compare_value(p: int) -> int:
    if abs(p) == KING:
        return 10_000
    return piece_value(p)


def is_major(p: int) -> bool:
    return abs(p) in (ROOK, QUEEN)


def is_slider(p: int) -> bool:
    return abs(p) in (BISHOP, ROOK, QUEEN)


def slider_dirs(p: int) -> List[Tuple[int, int]]:
    d: List[Tuple[int, int]] = []
    if abs(p) in (BISHOP, QUEEN):
        d.extend([(1, 1), (1, -1), (-1, 1), (-1, -1)])
    if abs(p) in (ROOK, QUEEN):
        d.extend([(1, 0), (-1, 0), (0, 1), (0, -1)])
    return d


def ray(from_sq: int, d: Tuple[int, int]) -> List[int]:
    out: List[int] = []
    f = file_of(from_sq) + d[0]
    r = rank_of(from_sq) + d[1]
    while True:
        s = make_sq(f, r)
        if s is None:
            break
        out.append(s)
        f += d[0]
        r += d[1]
    return out


def defended(b: Board, sq: int, by_white: bool) -> bool:
    return b.attacked_by(sq, by_white)


def read_all(ctx: Ctx) -> List[Reading]:
    """Read every template for one side."""
    return [read(i, ctx) for i in range(20)]


def flags_all(ctx: Ctx) -> List[int]:
    return [r.flags() for r in read_all(ctx)]


_READERS = None  # filled lazily after strategy functions exist


def read(id: int, ctx: Ctx) -> Reading:
    global _READERS
    if _READERS is None:
        _READERS = (
            central_occupation,
            central_break,
            kingside_storm,
            minority_attack,
            king_shelter,
            opposite_castling,
            fianchetto,
            open_file,
            seventh_rank,
            passed_pawn,
            isolated_attack,
            backward_pressure,
            knight_outpost,
            bishop_pair,
            pin,
            discovered,
            fork,
            skewer,
            battery,
            promotion,
        )
    return _READERS[id](ctx)


def central_squares(white: bool) -> Tuple[int, int]:
    if white:
        return (27, 28)  # d4, e4
    return (35, 36)  # d5, e5


def central_occupation(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    pawn = own(w, PAWN)
    r = Reading()
    pawns = [s for s in squares_of(b, pawn) if file_of(s) in (3, 4)]
    r.foundation = bool(pawns)
    cs = central_squares(w)
    r.progress = any(b.sq[s] == pawn for s in cs)
    r.completion = all(b.sq[s] == pawn and defended(b, s, w) for s in cs)
    r.participants = pawns
    r.targets = [27, 28, 35, 36]
    return r


def opposing_central_pawns(b: Board, w: bool) -> List[int]:
    """Opposing pawns on d4, e4, d5 or e5."""
    return [s for s in (27, 28, 35, 36) if b.sq[s] == own(not w, PAWN)]


def central_break(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    opp = opposing_central_pawns(b, w)
    mine = [s for s in squares_of(b, own(w, PAWN)) if 2 <= file_of(s) <= 5]
    r.foundation = bool(opp) and bool(mine)
    r.progress = any(t in b.attacks_from(m) for t in opp for m in mine)
    r.completion = any(
        abs(t.piece) == PAWN and abs(t.captured) == PAWN and 2 <= file_of(t.to) <= 5
        for t in c.window
    )
    r.participants = mine
    r.targets = opp
    return r


def kingside_storm(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    pawns = [s for s in squares_of(b, own(w, PAWN)) if file_of(s) >= 5]
    k = b.king_sq(w)
    king_outside = k != NO_SQ and file_of(k) < 5
    moved = any(rel_rank(s, w) >= 2 for s in pawns)
    r.foundation = len(pawns) >= 2 and moved and king_outside
    r.progress = any(rel_rank(s, w) >= 2 for s in pawns)
    r.completion = (
        sum(1 for s in pawns if rel_rank(s, w) >= 3) >= 2
        and k != NO_SQ
        and file_of(k) <= 3
    )
    r.participants = pawns
    r.targets = [s for s in range(64) if file_of(s) >= 5]
    return r


def pawns_on_files(b: Board, p: int, lo: int, hi: int) -> List[int]:
    return [s for s in squares_of(b, p) if lo <= file_of(s) <= hi]


def pawn_isolated(b: Board, sq: int) -> bool:
    p = b.sq[sq]
    f = file_of(sq)
    return not (f > 0 and file_has(b, f - 1, p)) and not (f < 7 and file_has(b, f + 1, p))


def pawn_doubled(b: Board, sq: int) -> bool:
    p = b.sq[sq]
    return sum(1 for r in range(8) if b.sq[r * 8 + file_of(sq)] == p) >= 2


def minority_attack(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    mine = pawns_on_files(b, own(w, PAWN), 0, 2)
    theirs = pawns_on_files(b, own(not w, PAWN), 0, 2)
    r.foundation = bool(mine) and len(mine) < len(theirs)
    r.progress = any(rel_rank(s, w) >= 2 for s in mine)
    weak = any(
        pawn_isolated(b, s) or pawn_doubled(b, s)
        for s in pawns_on_files(b, own(not w, PAWN), 0, 3)
    )
    r.completion = any(rel_rank(s, w) >= 3 for s in mine) and weak
    r.participants = mine
    r.targets = [s for s in range(64) if file_of(s) <= 3 and enemy(b.sq[s], w)]
    return r


def king_shelter(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    k = b.king_sq(w)
    if k == NO_SQ:
        return r
    kbit, qbit = (CASTLE_WK, CASTLE_WQ) if w else (CASTLE_BK, CASTLE_BQ)
    home = rel_sq(4, 0, w)
    castled_sqs = [rel_sq(2, 0, w), rel_sq(6, 0, w)]
    has_right = (b.castling & (kbit | qbit)) != 0
    r.foundation = (k == home and has_right) or (k in castled_sqs)

    def between(a: int, z: int) -> int:
        lo, hi = (a, z) if a < z else (z, a)
        return sum(1 for s in range(lo + 1, hi) if b.sq[s] != 0)

    near_rook = False
    if k == home:
        if (b.castling & kbit) != 0 and between(k, rel_sq(7, 0, w)) <= 1:
            near_rook = True
        if (b.castling & qbit) != 0 and between(k, rel_sq(0, 0, w)) <= 1:
            near_rook = True
    r.progress = (k in castled_sqs) or near_rook
    if k in castled_sqs:
        kf = file_of(k)
        files = [5, 6, 7] if kf >= 4 else [1, 2, 3]
        shelter_unmoved = all(b.sq[rel_sq(f, 1, w)] == own(w, PAWN) for f in files)
        r.completion = (not b.attacked_by(k, not w)) and shelter_unmoved
        r.participants = [rel_sq(f, 1, w) for f in files]
    r.participants.append(k)
    r.targets = b.attacks_from(k)
    return r


def opposite_castling(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    k = b.king_sq(w)
    ok = b.king_sq(not w)
    if k == NO_SQ or ok == NO_SQ:
        return r
    my_wing_q = file_of(k) <= 2
    my_wing_k = file_of(k) >= 5
    opp_lo, opp_hi = (5, 7) if my_wing_q else (0, 2)

    def in_opp(f: int) -> bool:
        return opp_lo <= f <= opp_hi

    r.foundation = (
        rel_rank(k, w) == 0
        and (my_wing_q or my_wing_k)
        and in_opp(file_of(ok))
    )
    wing_pawns = [
        s
        for s in squares_of(b, own(w, PAWN))
        if in_opp(file_of(ok)) and in_opp(file_of(s))
    ]
    r.progress = any(rel_rank(s, w) >= 2 for s in wing_pawns)
    half_open_major = any(
        friendly(b.sq[s], w)
        and is_major(b.sq[s])
        and in_opp(file_of(s))
        and not file_has(b, file_of(s), own(w, PAWN))
        and file_has(b, file_of(s), own(not w, PAWN))
        for s in range(64)
    )
    r.completion = (
        r.foundation
        and any(rel_rank(s, w) >= 3 for s in wing_pawns)
        and half_open_major
    )
    r.participants = [
        s
        for s in range(64)
        if friendly(b.sq[s], w)
        and (abs(b.sq[s]) == PAWN or is_major(b.sq[s]))
        and in_opp(file_of(s))
    ]
    r.targets = [s for s in range(64) if in_opp(file_of(s))]
    return r


def fianchetto(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    fsq = [rel_sq(1, 1, w), rel_sq(6, 1, w)]
    pawn_adv = any(b.sq[s] == own(w, PAWN) for s in (rel_sq(1, 2, w), rel_sq(6, 2, w)))
    bishops = [s for s in fsq if b.sq[s] == own(w, BISHOP)]
    r.foundation = pawn_adv or bool(bishops)
    r.progress = bool(bishops)
    r.completion = any(
        any(t in (27, 28, 35, 36) for t in b.attacks_from(s)) for s in bishops
    )
    r.participants = bishops
    r.targets = [27, 28, 35, 36]
    return r


def open_file(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    pawn = own(w, PAWN)
    no_pawn_files = [f for f in range(8) if not file_has(b, f, pawn)]
    majors = [s for s in range(64) if friendly(b.sq[s], w) and is_major(b.sq[s])]
    r.foundation = bool(no_pawn_files) and bool(majors)
    r.progress = any(file_of(s) in no_pawn_files for s in majors)
    r.completion = any(
        (not file_has(b, f, PAWN) and not file_has(b, f, -PAWN))
        and (
            sum(
                1
                for rk in range(8)
                if friendly(b.sq[rk * 8 + f], w) and is_major(b.sq[rk * 8 + f])
            )
            > sum(
                1
                for rk in range(8)
                if enemy(b.sq[rk * 8 + f], w) and is_major(b.sq[rk * 8 + f])
            )
        )
        for f in range(8)
    )
    r.participants = majors
    r.targets = [s for s in range(64) if file_of(s) in no_pawn_files]
    return r


def seventh_rank(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    majors = [s for s in range(64) if friendly(b.sq[s], w) and is_major(b.sq[s])]
    r.foundation = bool(majors) and any(not file_has(b, f, own(w, PAWN)) for f in range(8))
    r.progress = any(rel_rank(s, w) >= 5 for s in majors)
    r.completion = any(
        rel_rank(s, w) == 6
        and any(
            enemy(b.sq[t], w) and abs(b.sq[t]) != KING for t in b.attacks_from(s)
        )
        for s in majors
    )
    r.participants = majors
    r.targets = [rel_sq(f, 6, w) for f in range(8)]
    return r


def is_passed(b: Board, sq: int, w: bool) -> bool:
    f = file_of(sq)
    rr = rel_rank(sq, w)
    for df in (-1, 0, 1):
        ff = f + df
        if not (0 <= ff < 8):
            continue
        for r2 in range(rr + 1, 8):
            if b.sq[rel_sq(ff, r2, w)] == own(not w, PAWN):
                return False
    return True


def passed_pawn(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    passed = [s for s in squares_of(b, own(w, PAWN)) if is_passed(b, s, w)]
    r.foundation = bool(passed)
    r.progress = any(rel_rank(s, w) >= 3 for s in passed)
    r.completion = any(rel_rank(s, w) >= 5 and defended(b, s, w) for s in passed)
    for s in passed:
        f = file_of(s)
        for df in (-1, 0, 1):
            ff = f + df
            if 0 <= ff < 8:
                for r2 in range(rel_rank(s, w) + 1, 8):
                    r.targets.append(rel_sq(ff, r2, w))
    r.participants = passed
    return r


def isolated_attack(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    iso = [s for s in squares_of(b, own(not w, PAWN)) if pawn_isolated(b, s)]
    r.foundation = bool(iso)
    parts: List[int] = []
    for s in iso:
        att = list(b.attackers(s, w))
        file_major = any(
            friendly(b.sq[q], w) and is_major(b.sq[q]) and file_of(q) == file_of(s)
            for q in range(64)
        )
        if att or file_major:
            r.progress = True
        def_ = sum(1 for _ in b.attackers(s, not w))
        if len(att) > def_:
            r.completion = True
        parts.extend(att)
    parts = sorted(set(parts))
    r.participants = parts
    r.targets = iso
    return r


def backward_pressure(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    targets: List[int] = []
    for s in squares_of(b, own(not w, PAWN)):
        # The opposing pawn advances toward the evaluated player's side.
        adv_rank = rank_of(s) + (-1 if w else 1)
        adv = make_sq(file_of(s), adv_rank)
        if adv is None:
            continue
        attacked_by_my_pawn = any(
            b.sq[a] == own(w, PAWN) for a in b.attackers(adv, w)
        )
        defended_by_their_pawn = any(
            b.sq[a] == own(not w, PAWN) for a in b.attackers(adv, not w)
        )
        if (
            attacked_by_my_pawn
            and not defended_by_their_pawn
            and not file_has(b, file_of(s), own(w, PAWN))
        ):
            r.foundation = True
            major_on_file = [
                q
                for rk in range(8)
                for q in [(rk * 8 + file_of(s))]
                if friendly(b.sq[q], w) and is_major(b.sq[q])
            ]
            if major_on_file:
                r.progress = True
                # Rust: && binds tighter than ||
                if (b.sq[adv] != 0 and friendly(b.sq[adv], w)) or b.attacked_by(adv, w):
                    r.completion = True
            r.participants.extend(major_on_file)
            targets.append(s)
            targets.append(adv)
    r.targets = targets
    return r


def outpost_squares(b: Board, w: bool) -> List[int]:
    out: List[int] = []
    for rr in range(3, 7):
        for f in range(8):
            s = rel_sq(f, rr, w)
            p = b.sq[s]
            if not (p == 0 or p == own(w, KNIGHT)):
                continue
            by_pawn = any(b.sq[a] == own(w, PAWN) for a in b.attackers(s, w))
            if not by_pawn:
                continue
            # An opposing pawn on an adjacent file that has not yet passed this square could still attack it.
            threat = any(
                any(
                    b.sq[rel_sq(ff, r2, w)] == own(not w, PAWN)
                    for r2 in range(rr + 1, 8)
                )
                for ff in (f - 1, f + 1)
                if 0 <= ff < 8
            )
            if not threat:
                out.append(s)
    return out


def knight_outpost(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    posts = outpost_squares(b, w)
    knights = squares_of(b, own(w, KNIGHT))
    r.foundation = bool(posts)
    r.progress = any(
        p in knights or any(p in b.attacks_from(k) for k in knights) for p in posts
    )
    r.completion = any(p in knights for p in posts)
    r.participants = knights
    r.targets = posts
    return r


def bishop_pair(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    mine = squares_of(b, own(w, BISHOP))
    theirs = squares_of(b, own(not w, BISHOP))
    r.foundation = len(mine) >= 2 and len(theirs) < 2
    r.progress = any(rel_rank(s, w) != 0 for s in mine)
    open_center = any(
        not file_has(b, f, PAWN) and not file_has(b, f, -PAWN) for f in range(2, 6)
    )
    travel = any(
        sum(1 for t in b.attacks_from(s) if b.sq[t] == 0) >= 3 for s in mine
    )
    r.completion = r.foundation and open_center and travel
    r.targets = [
        t for s in mine for t in b.attacks_from(s) if enemy(b.sq[t], w)
    ]
    r.participants = mine
    return r


@dataclass
class LineHit:
    """Pieces along a ray from a friendly slider, for Pin and Skewer."""

    slider: int
    blocker: Optional[int]
    front: int
    rear: int


def _push_hit(pieces: Sequence[int], s: int, out: List[LineHit]) -> None:
    if len(pieces) >= 2:
        out.append(LineHit(slider=s, blocker=None, front=pieces[0], rear=pieces[1]))
    if len(pieces) >= 3:
        out.append(
            LineHit(slider=s, blocker=pieces[0], front=pieces[1], rear=pieces[2])
        )


def line_hits(b: Board, w: bool) -> List[LineHit]:
    out: List[LineHit] = []
    for s in range(64):
        p = b.sq[s]
        if not (friendly(p, w) and is_slider(p)):
            continue
        for d in slider_dirs(p):
            pieces = [q for q in ray(s, d) if b.sq[q] != 0][:3]
            if any(friendly(b.sq[q], w) for q in pieces):
                # Stop at the first friendly piece.
                cut = []
                for q in pieces:
                    if friendly(b.sq[q], w):
                        break
                    cut.append(q)
                _push_hit(cut, s, out)
            else:
                _push_hit(pieces, s, out)
    return out


def pin(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    for h in line_hits(b, w):
        front = b.sq[h.front]
        rear = b.sq[h.rear]
        if abs(front) == KING:
            continue
        if not (abs(rear) == KING or piece_value(rear) > piece_value(front)):
            continue
        r.foundation = True
        r.participants.append(h.slider)
        r.targets.append(h.front)
        r.targets.append(h.rear)
        if h.blocker is None:
            r.progress = True
            second = any(a != h.slider for a in b.attackers(h.front, w))
            if abs(rear) == KING or second:
                r.completion = True
    return r


def _move_from(m) -> int:
    """Origin square of a Move (`from_` preferred; `from` accepted if present)."""
    v = getattr(m, "from_", None)
    if v is None:
        v = getattr(m, "from")
    return v


def discovered(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    legal = b.legal_moves_for(w)
    for s in range(64):
        p = b.sq[s]
        if not (friendly(p, w) and is_slider(p)):
            continue
        for d in slider_dirs(p):
            line = ray(s, d)
            pieces = [q for q in line if b.sq[q] != 0][:2]
            if len(pieces) < 2:
                continue
            mid, tgt = pieces[0], pieces[1]
            if (
                not friendly(b.sq[mid], w)
                or not enemy(b.sq[tgt], w)
                or abs(b.sq[tgt]) == PAWN
            ):
                continue
            r.foundation = True
            r.participants.append(s)
            r.participants.append(mid)
            r.targets.append(tgt)
            for m in legal:
                if _move_from(m) != mid or m.to in line:
                    continue
                r.progress = True
                after = b.make(m)
                captures = b.is_capture(m)
                check = after.in_check(not w)
                still = tgt in after.attacks_from(s)
                if (captures or check) and still:
                    r.completion = True
                    if captures:
                        r.targets.append(b.captured_sq(m))
    return r


def fork_targets_ok(b: Board, attacker: int, targets: Sequence[int], w: bool) -> bool:
    return all(
        abs(b.sq[t]) == KING
        or not b.attacked_by(t, not w)
        or compare_value(b.sq[t]) >= compare_value(attacker)
        for t in targets
    )


def forked(b: Board, from_sq: int, w: bool) -> List[int]:
    return [
        t
        for t in b.attacks_from(from_sq)
        if enemy(b.sq[t], w) and abs(b.sq[t]) != PAWN
    ]


def fork(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    for s in range(64):
        p = b.sq[s]
        if not friendly(p, w):
            continue
        t = forked(b, s, w)
        if len(t) >= 2:
            r.foundation = True
            r.progress = True
            r.participants.append(s)
            r.targets.extend(t)
            good = [x for x in t if fork_targets_ok(b, p, [x], w)]
            if len(good) >= 2:
                r.completion = True
    for m in b.legal_moves_for(w):
        after = b.make(m)
        t = forked(after, m.to, w)
        if len(t) >= 2:
            r.foundation = True
            r.participants.append(_move_from(m))
            r.targets.extend(t)
    r.participants = sorted(set(r.participants))
    r.targets = sorted(set(r.targets))
    return r


def skewer(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    for h in line_hits(b, w):
        front = b.sq[h.front]
        rear = b.sq[h.rear]
        if compare_value(front) < compare_value(rear):
            continue
        r.foundation = True
        r.participants.append(h.slider)
        r.targets.append(h.front)
        r.targets.append(h.rear)
        if h.blocker is None and (
            abs(front) == KING or compare_value(front) > compare_value(rear)
        ):
            r.progress = True
            sv = piece_value(b.sq[h.slider])
            rear_ok = (not b.attacked_by(h.rear, not w)) or piece_value(rear) >= sv
            if abs(front) == KING or (piece_value(front) > sv and rear_ok):
                r.completion = True
    return r


def battery(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    majors = [s for s in range(64) if friendly(b.sq[s], w) and is_major(b.sq[s])]

    def original(s: int) -> bool:
        p = b.sq[s]
        return (abs(p) == ROOK and s in (rel_sq(0, 0, w), rel_sq(7, 0, w))) or (
            abs(p) == QUEEN and s == rel_sq(3, 0, w)
        )

    for i in range(len(majors)):
        for j in range(i + 1, len(majors)):
            a, z = majors[i], majors[j]
            same_file = file_of(a) == file_of(z)
            same_rank = rank_of(a) == rank_of(z)
            if not (same_file or same_rank):
                continue
            step = 8 if same_file else 1
            lo, hi = (a, z) if a < z else (z, a)
            between = []
            s = lo + step
            while s < hi:
                if b.sq[s] != 0:
                    between.append(s)
                s += step
            if len(between) > 2 or (original(a) and original(z)):
                continue
            r.foundation = True
            r.participants.append(a)
            r.participants.append(z)
            if len(between) <= 1:
                r.progress = True
            if not between:
                half_open = same_file and not file_has(b, file_of(a), own(w, PAWN))
                mn = min(a, z)

                def attacks_along() -> bool:
                    for s0 in (a, z):
                        if same_file:
                            d = (0, -1) if s0 == mn else (0, 1)
                        else:
                            d = (-1, 0) if s0 == mn else (1, 0)
                        for q in ray(s0, d):
                            if b.sq[q] != 0:
                                if enemy(b.sq[q], w):
                                    return True
                                break
                    return False

                if half_open or attacks_along():
                    r.completion = True
                dirs = ((0, 1), (0, -1)) if same_file else ((1, 0), (-1, 0))
                for d in dirs:
                    r.targets.extend(ray(a, d))
    return r


def promotion(c: Ctx) -> Reading:
    b = c.b
    w = c.white
    r = Reading()
    pawns = [s for s in squares_of(b, own(w, PAWN)) if rel_rank(s, w) >= 4]
    r.foundation = bool(pawns)
    r.progress = any(rel_rank(s, w) >= 5 for s in pawns)
    r.completion = any(m.promo != 0 for m in b.legal_moves_for(w))
    for s in pawns:
        r.targets.extend(b.attacks_from(s))
        t = make_sq(file_of(s), rank_of(s) + (1 if w else -1))
        if t is not None:
            r.targets.append(t)
    r.participants = pawns
    return r
