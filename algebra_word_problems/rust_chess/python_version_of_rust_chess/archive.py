"""Step 15.4 and 15.5: compact game files, banks, and merging into the index."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from board import Board, Move
from index import GameRecord, GameResult, Index, SavedMove
import strategies

GENERAL = "general"
DRILL = "drill"


class Archive:
    def __init__(self, game_dir: Path | str) -> None:
        self.root = Path(game_dir) / "ai_learning"
        self._next = self._scan_next_id()

    @staticmethod
    def new(game_dir: Path | str) -> Archive:
        return Archive(game_dir)

    def index_path(self) -> Path:
        return self.root / "index.txt"

    def games_dir(self) -> Path:
        return self.root / "games"

    def bank_path(self, bank: str) -> Path:
        return self.root / "banks" / f"{bank}.txt"

    def bank_entries(self, bank: str) -> list[tuple[int, str]]:
        path = self.bank_path(bank)
        try:
            text = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            return []
        out: list[tuple[int, str]] = []
        for line in text.splitlines():
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            try:
                id_ = int(parts[0])
            except ValueError:
                continue
            out.append((id_, parts[1]))
        return out

    def banks(self) -> list[str]:
        banks_dir = self.root / "banks"
        out: list[str] = []
        if banks_dir.is_dir():
            for e in banks_dir.iterdir():
                name = e.name
                if name.endswith(".txt"):
                    out.append(name[: -len(".txt")])
        out.sort()
        return out

    def next_id(self) -> int:
        return self._next

    def _scan_next_id(self) -> int:
        ids = [id_ for b in self.banks() for id_, _ in self.bank_entries(b)]
        return (max(ids) + 1) if ids else 1

    def _add_to_bank(self, bank: str, id_: int, file: str) -> None:
        p = self.bank_path(bank)
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("a", encoding="utf-8", newline="\n") as f:
            f.write(f"{id_}\t{file}\n")

    def begin_game(
        self,
        bank: str,
        start: Board,
        run_file: Optional[str] = None,
    ) -> GameWriter:
        id_ = self.next_id()
        self._next = id_ + 1
        file = run_file if run_file is not None else f"game_{id_}.txt"
        self.games_dir().mkdir(parents=True, exist_ok=True)
        path = self.games_dir() / file
        w = GameWriter(
            path=path,
            id=id_,
            bank=bank,
            buffered=run_file is not None,
        )
        w.text = f"GAME START id={id_} bank={bank} start={start.key()}\n"
        if not w.buffered:
            path.write_text(w.text, encoding="utf-8", newline="\n")
            w.text = ""
        self._add_to_bank(bank, id_, file)
        return w

    def all_games(self) -> list[tuple[GameRecord, bool]]:
        out: list[tuple[GameRecord, bool]] = []
        seen_files: set[str] = set()
        for bank in self.banks():
            for _, file in self.bank_entries(bank):
                if file in seen_files:
                    continue
                seen_files.add(file)
                path = self.games_dir() / file
                try:
                    text = path.read_text(encoding="utf-8")
                except FileNotFoundError:
                    continue
                out.extend(parse_games(text))
        out.sort(key=lambda pair: pair[0].id)
        return out

    def mark_unfinished_stopped(self) -> list[int]:
        stopped: list[int] = []
        checked: set[str] = set()
        for bank in self.banks():
            for _, file in self.bank_entries(bank):
                if file in checked:
                    continue
                checked.add(file)
                path = self.games_dir() / file
                try:
                    text = path.read_text(encoding="utf-8")
                except FileNotFoundError:
                    continue
                complete = complete_lines(text)
                if len(complete) < len(text):
                    path.write_bytes(complete.encode("utf-8"))
                games = parse_games(complete)
                if games and not games[-1][1]:
                    g = games[-1][0]
                    with path.open("a", encoding="utf-8", newline="\n") as f:
                        f.write("GAME STOPPED\n")
                    stopped.append(g.id)
        return stopped

    def catch_up_report(self, ix: Index) -> tuple[int, list[str]]:
        n = 0
        errors: list[str] = []
        for g, finished in self.all_games():
            if finished and not ix.is_merged(g.id):
                try:
                    ix.merge(g)
                    n += 1
                except (ValueError, Exception) as e:
                    errors.append(str(e))
        return n, errors

    def catch_up(self, ix: Index) -> int:
        return self.catch_up_report(ix)[0]

    def rebuild_report(self) -> tuple[Index, list[str]]:
        ix = Index.new()
        _, errors = self.catch_up_report(ix)
        return ix, errors

    def rebuild(self) -> Index:
        return self.rebuild_report()[0]

    def open_index(self) -> tuple[Index, int, list[str]]:
        notes: list[str] = []
        try:
            ix = Index.load(self.index_path())
        except Exception as e:
            notes.append(
                f"Could not read the index ({e}). "
                "Building it again from the saved games."
            )
            ix = Index.new()
        n, errors = self.catch_up_report(ix)
        for e in errors:
            notes.append(f"Left out of the index: {e}")
        return ix, n, notes


def complete_lines(text: str) -> str:
    """Text up to and including its last newline; a cut-off line is dropped."""
    if text.endswith("\n"):
        return text
    i = text.rfind("\n")
    if i < 0:
        return ""
    return text[: i + 1]


class GameWriter:
    def __init__(
        self,
        path: Path,
        id: int,
        bank: str,
        buffered: bool = False,
    ) -> None:
        self.path = Path(path)
        self.id = id
        self.bank = bank
        self.text = ""
        self.buffered = buffered

    def add_move(
        self, ply: int, before: Board, m: Move, flags: list[int]
    ) -> None:
        if self.buffered:
            line = f"m\t{m.uci()}\t{strategies.flags_to_sparse(flags)}\n"
            self._write(line)
            return
        legal = [x.uci() for x in before.legal_moves()]
        line = (
            f"M\t{ply}\t{'w' if before.white_to_move else 'b'}\t{m.uci()}\t"
            f"{before.san(m)}\t{strategies.flags_to_text(flags)}\t"
            f"{before.key()}\t{','.join(legal)}\n"
        )
        self._write(line)

    def _write(self, s: str) -> None:
        if self.buffered:
            self.text += s
        else:
            with self.path.open("a", encoding="utf-8", newline="\n") as f:
                f.write(s)

    def finish(self, result: str) -> None:
        if result == GameResult.Stopped:
            end = "GAME STOPPED\n"
        else:
            end = f"GAME END result={GameResult.text(result)}\n"
        self._write(end)
        if self.buffered:
            with self.path.open("a", encoding="utf-8", newline="\n") as f:
                f.write(self.text)


def parse_games(text: str) -> list[tuple[GameRecord, bool]]:
    """Parse the blocks of a game file. The flag says whether the block has an end."""
    out: list[tuple[GameRecord, bool]] = []
    for line in complete_lines(text).splitlines():
        if line.startswith("GAME START "):
            rest = line[len("GAME START ") :]
            id_ = 0
            bank = GENERAL
            start = Board.start()
            for part in rest.split(" "):
                if part.startswith("id="):
                    try:
                        id_ = int(part[3:])
                    except ValueError:
                        id_ = 0
                elif part.startswith("bank="):
                    bank = part[5:]
                elif part.startswith("start="):
                    try:
                        start = Board.from_key(part[6:])
                    except Exception:
                        pass
            out.append(
                (
                    GameRecord(
                        id=id_,
                        bank=bank,
                        start=start,
                        moves=[],
                        result=GameResult.Stopped,
                    ),
                    False,
                )
            )
        elif line.startswith("M\t"):
            if out and not out[-1][1]:
                rest = line[2:]
                f = rest.split("\t")
                if len(f) >= 5:
                    listed = True
                    if len(f) > 6:
                        listed = any(x == f[2] for x in f[6].split(","))
                    uci = f[2] if listed else "????"
                    out[-1][0].moves.append(
                        SavedMove(
                            uci=uci,
                            flags=list(strategies.flags_from_text(f[4])),
                        )
                    )
        elif line.startswith("m\t"):
            if out and not out[-1][1]:
                rest = line[2:]
                parts = rest.split("\t")
                if len(parts) >= 2:
                    out[-1][0].moves.append(
                        SavedMove(
                            uci=parts[0],
                            flags=list(strategies.flags_from_sparse(parts[1])),
                        )
                    )
        elif line.startswith("GAME END result="):
            if out:
                g, _ = out[-1]
                g.result = GameResult.parse(line[len("GAME END result=") :].strip())
                out[-1] = (g, True)
        elif line.startswith("GAME STOPPED"):
            if out:
                g, _ = out[-1]
                g.result = GameResult.Stopped
                out[-1] = (g, True)
    return out
