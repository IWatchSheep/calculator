"""Basic Step 15.8 checks that do not require a long drill."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from board import Board
from index import Index, Status
from lists34 import list3, list4
from normalize import Cat, kpk_positions, normalize


def test_empty_index_lists():
    b = Board.start()
    ix = Index()
    l3 = list3(ix, b, None)
    assert all(r.kind.kind == "never_tried" for r in l3.rows)
    assert list4(ix, b, None) == []


def test_kpk_key_set_sizes():
    assert len(kpk_positions(False)) == 331352
    assert len(kpk_positions(True)) == 165676


def test_mirror_shares_entry():
    # e-pawn position and its left-right reflection share one normalized key.
    a = Board.from_fen("4k3/8/8/8/4P3/8/8/4K3 w - - 0 1")
    # Mirror files: e->d, kings e1/e8 -> d1/d8
    b = Board.from_fen("3k4/8/8/8/3P4/8/8/3K4 w - - 0 1")
    na, nb = normalize(a), normalize(b)
    assert na.cat == Cat.Kpk and nb.cat == Cat.Kpk
    assert na.key() == nb.key()


def test_promotion_goal_win_and_draw():
    from index import edge_goal
    from normalize import normalize

    # Queen promo, lone king cannot take: win distance 0
    b = Board.from_fen("4k3/P7/8/8/8/8/8/4K3 w - - 0 1")
    m = b.parse_move("a7a8q")
    assert m is not None
    g = edge_goal(normalize(b), m, b)
    assert g is not None and g.is_win() and g.dist == 0

    # Bishop promo is a draw
    m = b.parse_move("a7a8b")
    assert m is not None
    g = edge_goal(normalize(b), m, b)
    assert g == Status.draw()


def test_hand_made_proof_rules():
    ix = Index()
    # Attacker to move: one try into a proven win => proven win
    a = ix.add_test_node("A", Cat.Kpk, True, 2)
    b = ix.add_test_node("B", Cat.Kpk, False, 0)
    ix.nodes[b].terminal = True
    ix.nodes[b].status = Status.win(0)
    ix.add_test_edge(a, 0, b, None)
    ix.recheck([a, b])
    assert ix.nodes[a].status == Status.win(1)


if __name__ == "__main__":
    test_empty_index_lists()
    print("empty lists ok")
    test_mirror_shares_entry()
    print("mirror ok")
    test_promotion_goal_win_and_draw()
    print("promo goals ok")
    test_hand_made_proof_rules()
    print("proof rules ok")
    test_kpk_key_set_sizes()
    print("kpk sizes ok")
