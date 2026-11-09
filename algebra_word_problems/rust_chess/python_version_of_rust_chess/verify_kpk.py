"""Independent check: solve KPK by plain retrograde iteration, then compare
every proven result in a drilled index (same idea as the Rust verify_kpk example).
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

from archive import Archive
from board import BISHOP, KNIGHT, QUEEN, Board
from drill import run
from index import Index, Status
from normalize import Cat, kpk_positions, normalize


def retrograde() -> tuple[list[Board], list[str], list[int | None]]:
    all_pos = kpk_positions(True)
    keys = [normalize(b).key() for b in all_pos]
    id_of = {k: i for i, k in enumerate(keys)}

    # successors: (True,) = win goal, (False,) = draw goal, (None, j) = position j
    succ: list[list[tuple]] = []
    for b in all_pos:
        n = normalize(b)
        row = []
        for m in n.board.legal_moves():
            after = n.board.make(m)
            if m.promo != 0:
                r = after.legal_moves()
                if not r:
                    row.append((True,) if after.in_check(after.white_to_move) else (False,))
                elif m.promo in (BISHOP, KNIGHT):
                    row.append((False,))
                else:
                    row.append((True,) if not any(x.to == m.to for x in r) else (False,))
                continue
            na = normalize(after)
            if na.cat != Cat.Kpk:
                row.append((False,))
            else:
                row.append((None, id_of[na.key()]))
        succ.append(row)

    n = len(all_pos)
    dist: list[int | None] = [None] * n
    for i, b in enumerate(all_pos):
        nb = normalize(b).board
        if not nb.legal_moves() and nb.in_check(nb.white_to_move) and not nb.white_to_move:
            dist[i] = 0

    while True:
        changed = False
        snap = dist[:]
        for i in range(n):
            if snap[i] is not None:
                continue
            nb = normalize(all_pos[i]).board
            vals: list[int | None] = []
            for s in succ[i]:
                if s[0] is True:
                    vals.append(0)
                elif s[0] is False:
                    vals.append(None)
                else:
                    vals.append(snap[s[1]])
            if not vals:
                continue
            if nb.white_to_move:
                wins = [v for v in vals if v is not None]
                if wins:
                    dist[i] = min(wins) + 1
                    changed = True
            elif all(v is not None for v in vals):
                dist[i] = max(vals) + 1  # type: ignore[arg-type]
                changed = True
        if not changed:
            break
    return all_pos, keys, dist


def compare(ix: Index, keys: list[str], dist: list[int | None]) -> tuple[int, int, int, int]:
    id_of = {k: i for i, k in enumerate(keys)}
    ok_w = ok_d = bad = longer = 0
    for node in ix.nodes:
        if node.cat != Cat.Kpk:
            continue
        i = id_of.get(node.key)
        if i is None:
            print(f"unknown key {node.key}")
            bad += 1
            continue
        st = node.status
        truth = dist[i]
        if st.is_win() and truth is not None:
            ok_w += 1
            if st.dist < truth:
                bad += 1
                print(f"too short {node.key} {st.dist} < {truth}")
            elif st.dist > truth:
                longer += 1
        elif st.is_win() and truth is None:
            bad += 1
            print(f"false win {node.key}")
        elif st.is_draw() and truth is None:
            ok_d += 1
        elif st.is_draw() and truth is not None:
            bad += 1
            print(f"false draw {node.key}")
    return ok_w, ok_d, bad, longer


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    games = int(args[0]) if args else 20000
    dir_ = Path(args[1]) if len(args) > 1 else Path.cwd() / "game_files_verify_kpk"

    t0 = time.perf_counter()
    all_pos, keys, dist = retrograde()
    wins = sum(1 for d in dist if d is not None)
    print(
        f"true: {len(all_pos)} positions, {wins} wins for the pawn side, "
        f"{len(all_pos) - wins} draws  ({time.perf_counter() - t0:.1f}s)"
    )

    if games <= 0:
        print("after 0 drill games: proven wins correct 0, proven draws correct 0, wrong 0, win distances longer than best 0")
        return

    if dir_.exists():
        # reuse existing drilled index if present
        archive = Archive(dir_)
        ix, _, notes = archive.open_index()
        for n in notes:
            print(n)
        if len(ix.merged) < games:
            need = games - len(ix.merged)
            print(f"Drill: continuing seed 1 for {need} more game(s) toward {games}.")
            run(ix, archive, 1, need, lambda g, index: print(f"  {g}") if g % 1000 == 0 else None)
        else:
            print(f"Using existing index with {len(ix.merged)} merged games.")
    else:
        archive = Archive(dir_)
        ix = Index()
        print(f"Drill: seed 1, {games} game(s).")
        run(ix, archive, 1, games, lambda g, index: print(f"  {g}") if g % 1000 == 0 else None)

    ok_w, ok_d, bad, longer = compare(ix, keys, dist)
    print(
        f"after {games} drill games: proven wins correct {ok_w}, proven draws correct {ok_d}, "
        f"wrong {bad}, win distances longer than best {longer}"
    )


if __name__ == "__main__":
    main()
