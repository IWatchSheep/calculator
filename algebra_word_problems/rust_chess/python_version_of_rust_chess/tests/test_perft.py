"""Move generation against published perft counts."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from board import Board, perft


def test_start_position_counts():
    b = Board.start()
    expect = [20, 400, 8902, 197281]
    for d, n in enumerate(expect, start=1):
        assert perft(b, d) == n, f"depth {d}"


def test_start_position_depth_5():
    assert perft(Board.start(), 5) == 4865609


def test_kiwipete():
    b = Board.from_fen(
        "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1"
    )
    assert perft(b, 1) == 48
    assert perft(b, 2) == 2039
    assert perft(b, 3) == 97862


def test_endgame_and_promotion_positions():
    b = Board.from_fen("8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1")
    assert perft(b, 4) == 43238
    b = Board.from_fen(
        "r3k2r/Pppp1ppp/1b3nbN/nP6/BBP1P3/q4N2/Pp1P2PP/R2Q1RK1 w kq - 0 1"
    )
    assert perft(b, 3) == 9467


if __name__ == "__main__":
    test_start_position_counts()
    print("start depths 1-4 ok")
    test_kiwipete()
    print("kiwipete ok")
    test_endgame_and_promotion_positions()
    print("endgame ok")
    # depth 5 is slow; run only if asked
    import os

    if os.environ.get("PERFT5"):
        test_start_position_depth_5()
        print("depth 5 ok")
