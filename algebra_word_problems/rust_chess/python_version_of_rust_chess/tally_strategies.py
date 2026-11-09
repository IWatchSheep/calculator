"""Count strategy flags stored in archived games (Python port of chess_probe archive)."""

from __future__ import annotations

import sys
from pathlib import Path

from archive import Archive, parse_games
from index import GameResult
from strategies import NAMES, F_COMPLETION, F_FOUNDATION, F_PROGRESS


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    dir_ = Path(args[0]) if args else Path("game_files_kpk")
    archive = Archive(dir_)
    games = archive.all_games()
    # foundation / progress / completion position counts and per-game seen
    pos = [[0, 0, 0] for _ in range(20)]
    g_found = [0] * 20
    g_prog = [0] * 20
    g_compl = [0] * 20
    results = {"white-wins": 0, "black-wins": 0, "draw": 0, "draw-by-rule": 0, "stopped": 0, "other": 0}
    moves = 0
    positions = 0
    for g, fin in games:
        if not fin:
            continue
        results[g.result] = results.get(g.result, 0) + 1
        seen_f = [False] * 20
        seen_p = [False] * 20
        seen_c = [False] * 20
        for sm in g.moves:
            moves += 1
            positions += 1
            for k, fl in enumerate(sm.flags):
                if fl & F_FOUNDATION:
                    pos[k][0] += 1
                    seen_f[k] = True
                if fl & F_PROGRESS:
                    pos[k][1] += 1
                    seen_p[k] = True
                if fl & F_COMPLETION:
                    pos[k][2] += 1
                    seen_c[k] = True
        for k in range(20):
            if seen_f[k]:
                g_found[k] += 1
            if seen_p[k]:
                g_prog[k] += 1
            if seen_c[k]:
                g_compl[k] += 1
    finished = sum(1 for g, fin in games if fin)
    print(f"archive files read under {archive.games_dir()}")
    print(f"moves read: {moves}")
    print(
        f"results: white wins {results.get(GameResult.WhiteWin, 0)}  "
        f"black wins {results.get(GameResult.BlackWin, 0)}  "
        f"draws {results.get(GameResult.Draw, 0) + results.get(GameResult.DrawByRule, 0)}  "
        f"other {results.get(GameResult.Stopped, 0)}"
    )
    print(
        f"== Strategy flags found in the archive {archive.games_dir()} =="
    )
    print(f"games: {finished}   positions with flags counted: {positions}")
    print(
        f" {'#':>2}  {'strategy':<32} {'foundation':>12} {'progress':>12} "
        f"{'completion':>12} {'g:found':>10} {'g:prog':>9} {'g:compl':>9}   best stage"
    )
    seen = 0
    for i, name in enumerate(NAMES):
        f, p, c = pos[i]
        best = "-"
        if c:
            best = "COMPLETION"
        elif p:
            best = "progress"
        elif f:
            best = "foundation"
        if f or p or c:
            seen += 1
        print(
            f" {i + 1:2d}  {name:<32} {f:12d} {p:12d} {c:12d} "
            f"{g_found[i]:10d} {g_prog[i]:9d} {g_compl[i]:9d}   {best}"
        )
    print(f"strategies seen at least once: {seen} of 20")


if __name__ == "__main__":
    main()
