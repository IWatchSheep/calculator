"""Console program: Steps 1-3, the in-game commands, perft, drill and rebuild-index."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

from archive import GENERAL, Archive, GameWriter
from board import (
    BISHOP,
    KNIGHT,
    QUEEN,
    ROOK,
    START_FEN,
    Board,
    Move,
    parse_sq,
    perft,
    piece_name,
    sq_name,
)
from drill import run as drill_run
from evaluate import list1, list2
from history import WINDOW, History, HistoryRecord
from index import GameRecord, GameResult, Index, SavedMove
from lists34 import list3, list4
from strategies import (
    DESCRIPTIONS,
    NAMES,
    Ctx,
    TurnInfo,
    flags_all,
    stage_name,
)

PRESETS: list[tuple[str, str, str]] = [
    ("start", START_FEN, "The standard starting position"),
    (
        "kpk-win",
        "3k4/8/3K4/3P4/8/8/8/8 w - - 0 1",
        "King and pawn against king: White's king on the sixth rank in front of its pawn",
    ),
    (
        "kpk-draw",
        "7k/8/7K/7P/8/8/8/8 w - - 0 1",
        "King and pawn against king: an h-pawn with the lone king in the h8 corner",
    ),
    (
        "kpk-black",
        "8/8/8/3p4/3k4/8/8/3K4 b - - 0 1",
        "King and pawn against king with Black as the pawn side",
    ),
    ("krk", "8/8/8/4k3/8/8/8/R3K3 w - - 0 1", "King and rook against king"),
    (
        "kiwipete",
        "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1",
        "A busy middlegame",
    ),
]


def prompt(text: str) -> Optional[str]:
    try:
        sys.stdout.write(text)
        sys.stdout.flush()
        line = sys.stdin.readline()
    except Exception:
        return None
    if line == "":
        return None
    return line.strip()


def side_name(white: bool) -> str:
    return "White" if white else "Black"


class App:
    def __init__(self, dir: Path) -> None:
        self.archive = Archive.new(dir)
        stopped = self.archive.mark_unfinished_stopped()
        if stopped:
            print(
                f"Marked {len(stopped)} unfinished saved game(s) as stopped: {stopped}"
            )
        self.index, merged, notes = self.archive.open_index()
        for n in notes:
            print(n)
        if merged > 0 or notes:
            self.index.save(self.archive.index_path())
            print(f"Merged {merged} finished game(s) into the position index.")
        self.history = History(dir)
        self.board = Board.start()
        self.start = Board.start()
        self.ply = 0
        self.writer: Optional[GameWriter] = None
        self.saved_moves: list[SavedMove] = []
        self.seen: dict[str, int] = {}
        self.over: Optional[str] = None
        self.bank: Optional[str] = None
        self.windows: list[list[TurnInfo]] = [[], []]

    def stop_current(self) -> None:
        if self.writer is not None and self.over is None:
            self.end_game(GameResult.Stopped, False)

    def new_game(self, b: Board) -> None:
        self.stop_current()
        self.board = b
        self.start = b
        self.ply = 0
        self.over = None
        self.saved_moves.clear()
        self.seen.clear()
        self.seen[b.key()] = 1
        self.windows = [[], []]
        try:
            self.history.clear()
        except Exception as e:
            print(f"Could not clear the history files: {e}")
        print(
            "\nSave this game's information to the permanent AI learning files?\n"
            "Y — Yes\nN — No"
        )
        ans = prompt("> ") or ""
        self.writer = None
        if ans.lower() == "y":
            try:
                w = self.archive.begin_game(GENERAL, b, None)
                print(f"This game is saved as game {w.id}.")
                self.writer = w
            except Exception as e:
                print(f"Could not start the game file: {e}")
        else:
            print("This game will not be saved.")
        self.show_board()

    def show_board(self) -> None:
        print(f"\n{self.board.ascii()}")
        print(f"{side_name(self.board.white_to_move)} to move.")

    def end_game(self, result: str, announce: bool) -> None:
        if announce:
            print(f"Game over: {GameResult.text(result)}.")
        self.over = result
        w = self.writer
        self.writer = None
        if w is None:
            return
        id_ = w.id
        try:
            w.finish(result)
        except Exception as e:
            print(f"Could not finish the game file: {e}")
            return
        rec = GameRecord(
            id=id_,
            bank=GENERAL,
            start=self.start,
            moves=list(self.saved_moves),
            result=result,
        )
        try:
            self.index.merge(rec)
            self.index.save(self.archive.index_path())
            p, ww, d = self.index.proven_counts()
            print(
                f"Game {id_} merged into the index: {p} positions, "
                f"{ww} proven wins, {d} proven draws."
            )
        except Exception as e:
            print(f"Could not merge game {id_}: {e}")

    def select(self, sq: int) -> None:
        if self.over is not None:
            print("The game is over. Type new, load or preset to start another.")
            return
        p = self.board.sq[sq]
        if p == 0:
            print(f"There is no piece on {sq_name(sq)}.")
            return
        if (p > 0) != self.board.white_to_move:
            print(
                f"The {piece_name(p)} on {sq_name(sq)} belongs to the side "
                "that is not to move."
            )
            return
        moves = [m for m in self.board.legal_moves() if m.from_ == sq]
        if not moves:
            print(
                f"The {piece_name(p)} on {sq_name(sq)} cannot currently "
                "make a legal move."
            )
            return
        listing = ", ".join(
            f"{sq_name(m.to)} ({self.board.san(m)})" for m in moves
        )
        print(f"Legal moves for the {piece_name(p)} on {sq_name(sq)}: {listing}")
        dest = prompt("Destination square (Enter to cancel): ")
        if dest is None:
            return
        to = parse_sq(dest)
        if to is None:
            print("No move made.")
            return
        choices = [m for m in moves if m.to == to]
        if not choices:
            print(f"{sq_name(to)} is not a legal destination. No move made.")
            return
        if len(choices) > 1:
            while True:
                ans = prompt("Promote to (q, r, b, n): ")
                if ans is None:
                    print("No move made.")
                    return
                t = {
                    "q": QUEEN,
                    "r": ROOK,
                    "b": BISHOP,
                    "n": KNIGHT,
                }.get(ans.lower())
                if t is None:
                    print("Please enter q, r, b or n.")
                    continue
                choices = [m for m in choices if m.promo == t]
                break
            m = choices[0]
        else:
            m = choices[0]
        ans = prompt(f"Confirm {self.board.san(m)}? (Y/N): ") or ""
        if ans.lower() != "y":
            print("Move cancelled. Nothing on the board changed.")
            return
        self.play(m)

    def play(self, m: Move) -> None:
        before = self.board
        after = before.make(m)
        white = before.white_to_move
        self.ply += 1
        turn = TurnInfo(
            white=white,
            from_=m.from_,
            to=m.to,
            piece=before.sq[m.from_],
            captured=before.captured_piece(m),
        )
        rec = HistoryRecord(
            ply=self.ply,
            move_no=before.fullmove,
            white=white,
            mv=m,
            san=before.san(m),
            turn=turn,
            before=before,
            after=after,
        )
        try:
            self.history.push(rec)
        except Exception as e:
            print(f"Could not write the history file: {e}")
        w = self.windows[0 if white else 1]
        w.append(turn)
        if len(w) > WINDOW:
            w.pop(0)
        flags = flags_all(Ctx(b=after, white=white, window=w))
        if self.writer is not None:
            try:
                self.writer.add_move(self.ply, before, m, flags)
            except Exception as e:
                print(f"Could not write the game file: {e}")
        self.saved_moves.append(SavedMove(uci=m.uci(), flags=list(flags)))
        print(f"Played {before.san(m)}.")
        self.board = after
        c = self.seen.get(after.key(), 0) + 1
        self.seen[after.key()] = c
        self.show_board()
        if after.is_checkmate():
            self.end_game(
                GameResult.WhiteWin if white else GameResult.BlackWin, True
            )
        elif after.is_stalemate():
            print("Stalemate.")
            self.end_game(GameResult.Draw, True)
        elif after.insufficient_material():
            print("Neither side can checkmate.")
            self.end_game(GameResult.Draw, True)
        elif c >= 3:
            print("The same position has occurred three times.")
            self.end_game(GameResult.DrawByRule, True)
        elif after.halfmove >= 100:
            print("Fifty moves without a pawn move or a capture.")
            self.end_game(GameResult.DrawByRule, True)

    def window(self, white: bool) -> list[TurnInfo]:
        return self.history.window(white)

    def show_lists(self, white: bool) -> None:
        w = self.window(white)
        print(f"\nList 1 — Forming strategies for {side_name(white)} (present game only)")
        rows = list1(self.board, white, w)
        if not rows:
            print("  (none)")
        for r in rows:
            print(f"  {r.score:>3}  {stage_name(r.score):<20} {r.name}")
        print("\nList 2 — Captures for those strategies")
        if self.board.white_to_move != white:
            print(f"  (only made when it is {side_name(white)}'s turn)")
            return
        rows2 = list2(self.board, white, w)
        if not rows2:
            print("  (none)")
        for r in rows2:
            print(
                f"  {r.san:<8} {piece_name(r.piece)} {sq_name(r.from_)} takes "
                f"{piece_name(r.victim)} {sq_name(r.victim_sq)}  "
                f"gain {r.exchange.gain} loss {r.exchange.loss} "
                f"net {r.exchange.net()}  [{r.strategy}]"
            )

    def bank_label(self) -> str:
        if self.bank is None:
            return "all banks"
        return f"bank {self.bank}"

    def show_list3(self) -> None:
        l = list3(self.index, self.board, self.bank)
        print(
            f"\nList 3 — Past games after each legal move "
            f"({self.bank_label()}, {l.cat.code()})"
        )
        if l.cat.proof_family():
            who = "The pawn side" if l.pawn_side_to_move else "The lone king"
            print(
                "  Counts are for the pawn side (or the rook side). "
                f"{who} is to move."
            )
        else:
            print("  Counts are for the side to move.")
        if not l.position_known:
            print(
                "  This position is not in the index yet, so every move is never tried."
            )
        for r in l.rows:
            if r.kind.kind == "proven_win":
                status = f"proven win in {r.kind.dist}"
            elif r.kind.kind == "proven_draw":
                status = "proven draw"
            elif r.kind.kind == "tried":
                status = "tried"
            elif r.kind.kind == "similar":
                status = "never tried here; similar"
            else:
                status = "never tried"
            if r.kind.kind == "never_tried":
                counts = ""
            else:
                c = r.counts
                counts = (
                    f"  played {c.played} W{c.wins} D{c.draws} L{c.losses}"
                )
            print(f"  {r.san:<8} {status}{counts}")
            if r.notes:
                notes = ", ".join(f"{n} {s}" for n, s in r.notes)
                print(f"           strategies: {notes}")

    def show_list4(self) -> None:
        rows = list4(self.index, self.board, self.bank)
        print(
            f"\nList 4 — Captures and promotions that past games played "
            f"after each move ({self.bank_label()})"
        )
        if not rows:
            print("  (none)")
        for r in rows:
            print(
                f"  {r.san:<8} reply {r.reply:<8} next {r.next:<8} "
                f"played {r.count}  gain {r.gain} loss {r.loss} net {r.net()}"
            )

    def show_status(self) -> None:
        p, w, d = self.index.proven_counts()
        print(f"Positions stored: {p}. Proven wins: {w}. Proven draws: {d}.")
        print(
            f"Finished games merged: {len(self.index.merged)}. "
            f"Tried moves: {len(self.index.edges)}."
        )
        for b in self.archive.banks():
            print(f"  bank {b}: {len(self.archive.bank_entries(b))} game(s)")
        print(f"Lists 3 and 4 read: {self.bank_label()}.")
        if self.writer is not None:
            print(f"This game is being saved as game {self.writer.id}.")

    def show_archive(self) -> None:
        games = self.archive.all_games()
        if not games:
            print("No saved games yet.")
            return
        shown = min(30, len(games))
        print(f"Saved games (last {shown} of {len(games)}):")
        for g, fin in games[len(games) - shown :]:
            status = GameResult.text(g.result) if fin else "in progress"
            print(
                f"  game {g.id:>6}  bank {g.bank:<8} "
                f"moves {len(g.moves):>3}  {status}"
            )

    def help(self) -> None:
        print(
            """Commands:
  e2 (any square)        select a piece, see its legal moves, enter a destination, confirm with Y or N
  lists [w|b]            List 1 and List 2
  list3                  List 3 for the side to move (from past games)
  list4                  List 4 for those moves (from past games)
  bank [name|all]        choose which bank's counts Lists 3 and 4 show
  strategies             the 20 templates;  strategy <n>  one template in full
  status                 stored positions, proven positions and banks
  archive                saved games
  new | load <fen> | presets | preset <id>
  resign | draw | board | moves | fen | help | quit"""
        )

    def run(self) -> None:
        self.help()
        self.new_game(self.board)
        while True:
            line = prompt("\n> ")
            if line is None:
                self.stop_current()
                return
            parts = line.split()
            if not parts:
                continue
            cmd = parts[0].lower()
            if cmd in ("quit", "exit"):
                self.stop_current()
                return
            if cmd == "help":
                self.help()
            elif cmd == "board":
                self.show_board()
            elif cmd == "fen":
                print(self.board.to_fen())
            elif cmd == "moves":
                ms = [self.board.san(m) for m in self.board.legal_moves()]
                print(f"{len(ms)} legal moves: {' '.join(ms)}")
            elif cmd == "lists":
                if len(parts) > 1 and parts[1] == "w":
                    white = True
                elif len(parts) > 1 and parts[1] == "b":
                    white = False
                else:
                    white = self.board.white_to_move
                self.show_lists(white)
            elif cmd == "list3":
                self.show_list3()
            elif cmd == "list4":
                self.show_list4()
            elif cmd == "bank":
                if len(parts) < 2 or parts[1] == "all":
                    self.bank = None
                else:
                    self.bank = parts[1]
                print(f"Lists 3 and 4 now read {self.bank_label()}.")
            elif cmd == "strategies":
                for i, n in enumerate(NAMES):
                    print(f"  {i + 1:>2}. {n}")
            elif cmd == "strategy":
                n = 0
                if len(parts) > 1:
                    try:
                        n = int(parts[1])
                    except ValueError:
                        n = 0
                if 1 <= n <= 20:
                    d = DESCRIPTIONS[n - 1]
                    print(
                        f"Strategy {n}: {NAMES[n - 1]}\n"
                        f"  Foundation: {d[0]}\n"
                        f"  Progress: {d[1]}\n"
                        f"  Completion: {d[2]}"
                    )
                else:
                    print("Give a number from 1 to 20.")
            elif cmd == "status":
                self.show_status()
            elif cmd == "archive":
                self.show_archive()
            elif cmd == "new":
                self.new_game(Board.start())
            elif cmd == "load":
                fen = " ".join(parts[1:])
                try:
                    self.new_game(Board.from_fen(fen))
                except Exception as e:
                    print(f"Could not load that position: {e}")
            elif cmd == "presets":
                for id_, _, d in PRESETS:
                    print(f"  {id_:<10} {d}")
            elif cmd == "preset":
                id_ = parts[1] if len(parts) > 1 else ""
                found = next((p for p in PRESETS if p[0] == id_), None)
                if found is None:
                    print("Unknown preset. Type presets to see them.")
                else:
                    self.new_game(Board.from_fen(found[1]))
            elif cmd == "resign":
                if self.over is None:
                    white = self.board.white_to_move
                    print(f"{side_name(white)} resigns.")
                    self.end_game(
                        GameResult.BlackWin if white else GameResult.WhiteWin,
                        True,
                    )
            elif cmd == "draw":
                if self.over is None:
                    self.end_game(GameResult.Draw, True)
            else:
                sq = parse_sq(cmd)
                if sq is not None:
                    self.select(sq)
                else:
                    print("Unknown command. Type help.")


def usage() -> None:
    print(
        """Usage:
  python main.py [--dir <folder>] [--fen "<fen>"]
  python main.py [--dir <folder>] perft <depth> [fen]
  python main.py [--dir <folder>] drill [seed] [games]
  python main.py [--dir <folder>] rebuild-index"""
    )


def main(argv: Optional[list[str]] = None) -> None:
    args = list(sys.argv[1:] if argv is None else argv)
    dir_ = Path("game_files")
    fen: Optional[str] = None
    i = 0
    while i < len(args):
        if args[i] == "--dir" and i + 1 < len(args):
            dir_ = Path(args[i + 1])
            del args[i : i + 2]
        elif args[i] == "--fen" and i + 1 < len(args):
            fen = args[i + 1]
            del args[i : i + 2]
        else:
            i += 1
    if not args:
        try:
            app = App(dir_)
        except Exception as e:
            print(f"Could not start: {e}")
            return
        if fen is not None:
            try:
                app.board = Board.from_fen(fen)
            except Exception as e:
                print(f"Bad FEN, using the start position: {e}")
        app.run()
        return
    cmd = args[0]
    if cmd == "perft":
        depth = 1
        if len(args) > 1:
            try:
                depth = int(args[1])
            except ValueError:
                depth = 1
        try:
            if len(args) > 2:
                b = Board.from_fen(" ".join(args[2:]))
            else:
                b = Board.start()
        except Exception as e:
            print(f"Bad FEN: {e}")
            return
        total = 0
        for d in range(1, depth + 1):
            n = perft(b, d)
            total += n
            print(f"Individual move {d}: {n} sequences")
        print(f"Total: {total} nodes")
    elif cmd == "drill":
        seed = 1
        games = 1000
        if len(args) > 1:
            try:
                seed = int(args[1])
            except ValueError:
                seed = 1
        if len(args) > 2:
            try:
                games = int(args[2])
            except ValueError:
                games = 1000
        archive = Archive.new(dir_)
        archive.mark_unfinished_stopped()
        ix, _, notes = archive.open_index()
        for n in notes:
            print(n)
        print(f"Drill: seed {seed}, {games} game(s).")

        def on_progress(g: int, index: Index) -> None:
            if g % 1000 == 0:
                p, w, d = index.proven_counts()
                print(
                    f"  {g} games: {p} positions, {w} proven wins, {d} proven draws"
                )

        try:
            r = drill_run(ix, archive, seed, games, on_progress)
            p, w, d = ix.proven_counts()
            print(
                f"Done: {r.games} games ({r.pawn_wins} pawn-side wins, "
                f"{r.draws} draws at a goal, {r.draws_by_rule} draws by rule).\n"
                f"Index: {p} positions, {w} proven wins, {d} proven draws."
            )
        except Exception as e:
            print(f"Drill stopped: {e}")
    elif cmd == "rebuild-index":
        archive = Archive.new(dir_)
        ix, errors = archive.rebuild_report()
        for e in errors:
            print(f"Left out of the index: {e}")
        try:
            ix.save(archive.index_path())
            p, w, d = ix.proven_counts()
            print(
                f"Rebuilt from {len(ix.merged)} games: {p} positions, "
                f"{w} proven wins, {d} proven draws."
            )
        except Exception as e:
            print(f"Could not save: {e}")
    elif cmd in ("help", "--help", "-h"):
        usage()
    else:
        print(f"Unknown command: {cmd}")
        usage()


if __name__ == "__main__":
    main()
