"""More Step 15.8-style index/proof tests ported from the Rust suite."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from archive import GENERAL, Archive
from board import QUEEN, Board
from drill import start_sequence
from index import GameRecord, GameResult, Index, SavedMove, Status
from lists34 import list3, list4
from normalize import Cat, normalize, similar_key


def game(id_: int, bank: str, fen: str, moves: list[str], result: str) -> GameRecord:
    return GameRecord(
        id=id_,
        bank=bank,
        start=Board.from_fen(fen),
        moves=[SavedMove(uci=m, flags=[0] * 20) for m in moves],
        result=result,
    )


def status_of(ix: Index, fen: str) -> Status:
    b = Board.from_fen(fen)
    id_ = ix.lookup(normalize(b).key())
    assert id_ is not None
    return ix.nodes[id_].status


def test_middlegame_key_is_exact_and_never_similar():
    b = Board.from_fen(
        "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1"
    )
    n = normalize(b)
    assert n.cat == Cat.Other
    assert "|w|KQkq|-" in n.key()
    assert similar_key(n) is None


def test_promotion_goals():
    fen = "8/P7/8/8/8/8/5k2/K7 w - - 0 1"
    ix = Index()
    ix.merge(game(1, GENERAL, fen, ["a7a8q"], GameResult.WhiteWin))
    assert status_of(ix, fen) == Status.win(1)
    ix = Index()
    ix.merge(game(1, GENERAL, fen, ["a7a8r"], GameResult.WhiteWin))
    assert status_of(ix, fen) == Status.win(1)
    ix = Index()
    ix.merge(game(1, GENERAL, fen, ["a7a8b"], GameResult.Draw))
    id_ = ix.lookup(normalize(Board.from_fen(fen)).key())
    assert id_ is not None
    e = next(e for e in ix.nodes[id_].edges if e is not None)
    assert ix.edge_value(e) == Status.draw()


def test_drill_starts_and_seed():
    a = start_sequence(1)
    b = start_sequence(1)
    assert [x.key() for x in a[:10]] == [x.key() for x in b[:10]]
    c = start_sequence(2)
    assert a[0].key() != c[0].key() or a[1].key() != c[1].key()
    # seventh rank first
    from board import PAWN, rank_of

    assert any(a[0].sq[s] == PAWN and rank_of(s) == 6 for s in range(64))


def test_list3_order_pawn_side():
    fen = "8/P7/8/8/8/8/5k2/K7 w - - 0 1"
    ix = Index()
    ix.merge(game(1, GENERAL, fen, ["a7a8q"], GameResult.WhiteWin))
    l3 = list3(ix, Board.from_fen(fen), None)
    assert l3.rows[0].kind.kind == "proven_win"
    assert any(r.kind.kind == "never_tried" for r in l3.rows)


def test_bank_selection_changes_counts_not_proofs():
    fen = "8/P7/8/8/8/8/5k2/K7 w - - 0 1"
    ix = Index()
    ix.merge(game(1, "general", fen, ["a7a8q"], GameResult.WhiteWin))
    ix.merge(game(2, "drill", fen, ["a7a8q"], GameResult.WhiteWin))
    b = Board.from_fen(fen)
    all_rows = list3(ix, b, None)
    gen = list3(ix, b, "general")
    proven_all = [r for r in all_rows.rows if r.kind.kind == "proven_win"][0]
    proven_gen = [r for r in gen.rows if r.kind.kind == "proven_win"][0]
    assert proven_all.kind.dist == proven_gen.kind.dist
    assert proven_all.counts.played == 2
    assert proven_gen.counts.played == 1


def test_short_index_line_is_an_error():
    bad = "FORMING-CHESS-INDEX 2\nK\t0\tonly\tthree\n"
    try:
        Index.from_text(bad)
        assert False, "expected error"
    except ValueError as e:
        assert "line 2" in str(e) or "short" in str(e).lower()


if __name__ == "__main__":
    test_middlegame_key_is_exact_and_never_similar()
    test_promotion_goals()
    test_drill_starts_and_seed()
    test_list3_order_pawn_side()
    test_bank_selection_changes_counts_not_proofs()
    test_short_index_line_is_an_error()
    print("all extra index tests passed")
