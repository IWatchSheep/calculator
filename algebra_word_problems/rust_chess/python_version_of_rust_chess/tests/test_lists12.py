"""Lists 1 and 2, the templates, the capture values and the history files."""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from board import PAWN, Board
from evaluate import list1, list2
from exchange import evaluate
from history import History, HistoryRecord, listing
from strategies import TurnInfo


def ex(fen: str, mv: str):
    b = Board.from_fen(fen)
    m = b.parse_move(mv)
    assert m is not None, f"{mv} not legal in {fen}"
    e = evaluate(b, m)
    return e.gain, e.loss, e.net()


def test_starting_list1():
    for white in (True, False):
        rows = list1(Board.start(), white, [])
        got = [(r.name, r.score) for r in rows]
        assert got == [("Central Pawn Occupation", 30), ("King Shelter", 30)]


def test_list1_never_uses_45_or_75():
    b = Board.from_fen(
        "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1"
    )
    for white in (True, False):
        for r in list1(b, white, []):
            assert r.score in (30, 60, 100)


def test_central_pawn_break_completes():
    b = Board.from_fen("4k3/8/8/3P4/8/8/8/4K3 w - - 0 1")
    window = [TurnInfo(white=True, from_=28, to=35, piece=PAWN, captured=-PAWN)]
    rows = list1(b, True, window)
    assert any(r.name == "Central Pawn Break" and r.score == 100 for r in rows)


def test_promotion_template():
    b = Board.from_fen("4k3/P7/8/8/8/8/8/4K3 w - - 0 1")
    rows = list1(b, True, [])
    assert any(r.name == "Promotion" and r.score == 100 for r in rows)
    blocked = Board.from_fen("n3k3/P7/8/8/8/8/8/4K3 w - - 0 1")
    rows = list1(blocked, True, [])
    assert any(r.name == "Promotion" and r.score == 60 for r in rows)


def test_capture_examples():
    assert ex("4k3/8/8/3p4/8/8/8/3QK3 w - - 0 1", "d1d5") == (100, 0, 100)
    assert ex("4k3/2n5/8/3p4/8/8/8/3QK3 w - - 0 1", "d1d5") == (100, 900, -800)
    assert ex("3rk3/8/8/3q4/4P3/8/8/3RK3 w - - 0 1", "e4d5") == (900, 0, 900)
    assert ex("4k3/8/4p3/3q4/4P3/2N5/8/4K3 w - - 0 1", "c3d5") == (1000, 320, 680)
    assert ex("4k3/8/2p5/3r4/8/8/8/3QK3 w - - 0 1", "d1d5") == (500, 900, -400)
    assert ex("3rk3/8/8/3pP3/8/8/8/4K3 w - d6 0 1", "e5d6") == (100, 100, 0)
    assert ex("7k/6pp/5P2/8/8/8/8/K5Q1 w - - 0 1", "g1g7") == (100100, 0, 100100)
    assert ex("2k5/1P6/8/8/8/8/8/4K3 w - - 0 1", "b7b8q") == (800, 900, -100)


def test_list2_only_on_turn():
    b = Board.from_fen(
        "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1"
    )
    assert list2(b, False, []) == []
    rows = list2(b, True, [])
    assert rows
    for a, c in zip(rows, rows[1:]):
        assert a.exchange.net() >= c.exchange.net()


def test_history_files():
    with tempfile.TemporaryDirectory() as td:
        h = History(td)
        h.clear()
        b = Board.start()
        mvs = [
            "g1f3",
            "g8f6",
            "f3g1",
            "f6g8",
            "g1f3",
            "g8f6",
            "f3g1",
            "f6g8",
            "g1f3",
            "g8f6",
            "f3g1",
            "f6g8",
        ]
        for i, mv in enumerate(mvs):
            m = b.parse_move(mv)
            assert m is not None
            a = b.make(m)
            white = b.white_to_move
            h.push(
                HistoryRecord(
                    ply=i + 1,
                    move_no=b.fullmove,
                    white=white,
                    mv=m,
                    san=b.san(m),
                    turn=TurnInfo(
                        white=white,
                        from_=m.from_,
                        to=m.to,
                        piece=b.sq[m.from_],
                        captured=0,
                    ),
                    before=b,
                    after=a,
                )
            )
            b = a
        assert len(h.window(True)) == 5
        text = h.path(True).read_text(encoding="utf-8")
        assert text.count("RECORD") == 5
        assert "castling rights: KQkq" in text
        assert "en passant: -" in text
        l = listing(Board.start())
        assert "pawn e2: e2e3 e2e4" in l
        assert "pawn e7: e7e5 e7e6" in l


if __name__ == "__main__":
    test_starting_list1()
    test_list1_never_uses_45_or_75()
    test_central_pawn_break_completes()
    test_promotion_template()
    test_capture_examples()
    test_list2_only_on_turn()
    test_history_files()
    print("all lists12 tests passed")
