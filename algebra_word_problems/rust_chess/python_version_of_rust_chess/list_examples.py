"""Print List 1/3/4 examples for the report (empty archive + solved KPK presets)."""

from __future__ import annotations

import sys
from pathlib import Path

from archive import Archive
from board import Board
from evaluate import list1, list2
from index import Index
from lists34 import list3, list4
from strategies import stage_name


def show_lists(label: str, ix: Index, fen: str) -> None:
    b = Board.from_fen(fen)
    print(f"\n=== {label} ===")
    print(f"FEN {fen}")
    rows = list1(b, b.white_to_move, [])
    print("List 1:")
    if not rows:
        print("  (none)")
    for r in rows:
        print(f"  {r.score:>3}  {stage_name(r.score):<20} {r.name}")
    print("List 2:")
    rows2 = list2(b, b.white_to_move, [])
    if not rows2:
        print("  (none)")
    for r in rows2[:8]:
        print(f"  {r.san} net {r.exchange.net()} [{r.strategy}]")
    l3 = list3(ix, b, None)
    print(f"List 3 ({l3.cat.code()}, known={l3.position_known}):")
    for r in l3.rows[:12]:
        k = r.kind.kind
        if k == "proven_win":
            status = f"proven win in {r.kind.dist}"
        elif k == "proven_draw":
            status = "proven draw"
        elif k == "tried":
            status = "tried"
        elif k == "similar":
            status = "similar"
        else:
            status = "never tried"
        extra = ""
        if k != "never_tried":
            extra = f"  played {r.counts.played} W{r.counts.wins} D{r.counts.draws} L{r.counts.losses}"
        print(f"  {r.san:<8} {status}{extra}")
    rows4 = list4(ix, b, None)
    print("List 4:")
    if not rows4:
        print("  (none)")
    for r in rows4[:8]:
        print(
            f"  {r.san:<8} reply {r.reply:<8} next {r.next:<8} "
            f"played {r.count} gain {r.gain} loss {r.loss} net {r.net()}"
        )


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    dir_ = Path(args[0]) if args else Path("game_files_kpk")
    show_lists("Empty archive, standard start", Index(), Board.start().to_fen())
    archive = Archive(dir_)
    ix, _, notes = archive.open_index()
    for n in notes:
        print(n)
    show_lists("Solved KPK archive, preset kpk-win", ix, "3k4/8/3K4/3P4/8/8/8/8 w - - 0 1")
    show_lists("Solved KPK archive, preset kpk-draw", ix, "7k/8/7K/7P/8/8/8/8 w - - 0 1")
    show_lists("Solved KPK archive, preset kpk-black", ix, "8/8/8/3p4/3k4/8/8/3K4 b - - 0 1")


if __name__ == "__main__":
    main()
