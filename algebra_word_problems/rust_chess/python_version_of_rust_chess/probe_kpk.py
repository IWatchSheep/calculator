"""Read a solved KPK index and print the same kinds of lines as the Rust report."""

from __future__ import annotations

import sys
from pathlib import Path

from archive import Archive
from board import Board
from drill import choose
from index import GameResult, Status, goal_after
from normalize import Cat, normalize


PRESETS = [
    ("3k4/8/3K4/3P4/8/8/8/8 w - - 0 1", "kpk-win"),
    ("7k/8/7K/7P/8/8/8/8 w - - 0 1", "kpk-draw"),
    ("8/8/8/3p4/3k4/8/8/3K4 b - - 0 1", "kpk-black"),
    ("4k3/8/4K3/4P3/8/8/8/8 w - - 0 1", "central win"),
    ("8/8/8/4k3/4P3/4K3/8/8 w - - 0 1", "king in front draw"),
    ("8/8/8/8/4k3/8/4P3/4K3 w - - 0 1", "pawn on 2nd white"),
    ("8/8/8/8/4k3/8/4P3/4K3 b - - 0 1", "pawn on 2nd black"),
]


def status_line(ix, b: Board) -> str:
    n = normalize(b)
    id_ = ix.lookup(n.key())
    if id_ is None:
        return "not in index"
    node = ix.nodes[id_]
    st = node.status
    if st.is_win():
        return f"PROVEN WIN for the pawn side in {st.dist} moves"
    if st.is_draw():
        return "PROVEN DRAW"
    return "not proven"


def best_play(ix, start: Board, limit: int = 80) -> tuple[str, str]:
    """Follow the drill's choose() policy and return SAN line + result text."""
    b = start.copy()
    sans = []
    move_no = 1
    for _ in range(limit):
        m = choose(ix, b)
        if m is None:
            break
        san = b.san(m)
        if b.white_to_move:
            sans.append(f"{move_no}. {san}")
        else:
            if not sans or not sans[-1].endswith("..."):
                sans.append(f"{move_no}... {san}")
            else:
                sans[-1] = sans[-1]  # noqa
            # black move after white: append to previous if white just moved
            if sans and "." in sans[-1] and "..." not in sans[-1] and sans[-1].count(" ") == 1:
                sans[-1] = sans[-1] + f" {san}"
                move_no += 1
            else:
                sans.append(f"{move_no}... {san}")
                move_no += 1
            if b.white_to_move is False and sans and sans[-1].count(" ") >= 2:
                pass
        after = b.make(m)
        g = goal_after(b, m, after)
        if g is not None:
            return " ".join(sans), g
        # fix move numbering for white-only appends
        if b.white_to_move:
            # after white move, wait for black before bumping? already handled above poorly
            pass
        b = after
        if not b.white_to_move:
            # we just played white; don't bump yet
            pass
        else:
            move_no += 1
    return " ".join(sans), "unfinished"


def best_play_simple(ix, start: Board, limit: int = 120) -> tuple[str, str]:
    b = start.copy()
    parts: list[str] = []
    full = start.fullmove
    for _ in range(limit):
        m = choose(ix, b)
        if m is None:
            return " ".join(parts), "no-move"
        san = b.san(m)
        if b.white_to_move:
            parts.append(f"{b.fullmove}. {san}")
        else:
            if parts and parts[-1][0].isdigit() and parts[-1].count(" ") == 1:
                parts[-1] = parts[-1] + f" {san}"
            else:
                parts.append(f"{b.fullmove}... {san}")
        after = b.make(m)
        g = goal_after(b, m, after)
        if g is not None:
            return " ".join(parts), g
        # threefold / 50 not needed for short proven lines
        b = after
    return " ".join(parts), "unfinished"


def sample_distance_check(ix, sample: int = 1989) -> None:
    """Replay proven wins; check promotion after exactly the stored distance."""
    import random

    wins = [n for n in ix.nodes if n.cat == Cat.Kpk and n.status.is_win()]
    random.seed(1)
    if len(wins) > sample:
        wins = random.sample(wins, sample)
    exact = longer_promo = other = fail = timeout = 0
    for node in wins:
        b = Board.from_key(node.key())
        want = node.status.dist
        plies = 0
        ok = False
        for _ in range(300):
            m = choose(ix, b)
            if m is None:
                fail += 1
                break
            after = b.make(m)
            plies += 1
            g = goal_after(b, m, after)
            if g in (GameResult.WhiteWin, GameResult.BlackWin):
                if plies == want:
                    exact += 1
                elif plies == want + 1 and m.promo:
                    longer_promo += 1
                else:
                    other += 1
                ok = True
                break
            if g is not None:
                fail += 1
                ok = True
                break
            b = after
        else:
            timeout += 1
            ok = True
        if not ok:
            fail += 1
    print(
        f"distance check on {len(wins)} proven wins sampled across the whole endgame:"
    )
    print(
        f"  pawn side won by promotion after exactly the stored number of plies: {exact}   "
        f"one ply more than stored (the promoting move): {longer_promo}"
    )
    print(
        f"  won, but a different number of moves: {other}   did not end in a win: {fail}   "
        f"did not finish in 300 plies: {timeout}"
    )


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    dir_ = Path(args[0]) if args else Path("game_files_kpk")
    archive = Archive(dir_)
    ix, _, notes = archive.open_index()
    for n in notes:
        print(n)
    p, w, d = ix.proven_counts()
    print(f"index loaded: {p} stored positions, {len(ix.merged)} games merged. notes: {notes}")
    kpk = [n for n in ix.nodes if n.cat == Cat.Kpk]
    pw = sum(1 for n in kpk if n.status.is_win())
    pd = sum(1 for n in kpk if n.status.is_draw())
    un = sum(1 for n in kpk if not n.status.is_proven())
    longest = max((n.status.dist for n in kpk if n.status.is_win()), default=0)
    print(f"king and pawn against king, positions in the index: {len(kpk)}")
    print(
        f"  proven wins for the pawn side: {pw}   proven draws: {pd}   "
        f"not proven: {un}   longest forced win: {longest} moves"
    )
    print()
    for fen, label in PRESETS:
        b = Board.from_fen(fen)
        print(f"position {fen}")
        print(f"  {status_line(ix, b)}")
        line, result = best_play_simple(ix, b)
        print(f"  best play: {line}    -> {result}")
        print()
    sample_distance_check(ix)


if __name__ == "__main__":
    main()
