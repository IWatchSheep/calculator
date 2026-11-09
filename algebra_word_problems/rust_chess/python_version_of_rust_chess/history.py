"""Steps 4, 5 and 7: the two history files of the game being played."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Union

from board import NO_SQ, Board, Move, piece_name, sq_name
from strategies import TurnInfo

WINDOW: int = 5


@dataclass
class HistoryRecord:
    ply: int
    move_no: int
    white: bool
    mv: Move
    san: str
    turn: TurnInfo
    before: Board
    after: Board


def listing(b: Board) -> str:
    """Every piece of both colors with its legal moves, plus the side to move,
    castling rights and en passant square (Step 4)."""
    lines: List[str] = []
    lines.append(f"  side to move: {'White' if b.white_to_move else 'Black'}")
    lines.append(f"  castling rights: {b.castling_str()}")
    ep = b.legal_ep()
    lines.append(f"  en passant: {'-' if ep == NO_SQ else sq_name(ep)}")
    lines.append(f"  key: {b.key()}")
    for white in (True, False):
        moves = b.legal_moves_for(white)
        lines.append(f"  {'White' if white else 'Black'} pieces:")
        for sq in range(64):
            p = b.sq[sq]
            if p == 0 or (p > 0) != white:
                continue
            lst = [m.uci() for m in moves if m.from_ == sq]
            dest = "no legal moves" if not lst else " ".join(lst)
            lines.append(f"    {piece_name(p)} {sq_name(sq)}: {dest}")
    return "\n".join(lines) + "\n"


class History:
    def __init__(self, dir: Union[str, Path]) -> None:
        self.dir = Path(dir)
        self.white: List[HistoryRecord] = []
        self.black: List[HistoryRecord] = []

    def path(self, white: bool) -> Path:
        return self.dir / ("white_history.txt" if white else "black_history.txt")

    def clear(self) -> None:
        """Step 7: clear both history files at the start of a new game."""
        self.white.clear()
        self.black.clear()
        self.dir.mkdir(parents=True, exist_ok=True)
        self._write(True)
        self._write(False)

    def push(self, rec: HistoryRecord) -> None:
        white = rec.white
        lst = self.white if white else self.black
        lst.append(rec)
        if len(lst) > WINDOW:
            del lst[0]
        self._write(white)

    def window(self, white: bool) -> List[TurnInfo]:
        """The evaluated player's previous four turns and current turn."""
        lst = self.white if white else self.black
        return [r.turn for r in lst]

    def _write(self, white: bool) -> None:
        lst = self.white if white else self.black
        parts: List[str] = []
        parts.append(
            f"{'White' if white else 'Black'} history: previous four turns "
            f"and the current turn ({len(lst)} kept)"
        )
        for i, r in enumerate(lst):
            current = " (current turn)" if i + 1 == len(lst) else ""
            parts.append(
                f"\nRECORD ply={r.ply} move={r.move_no} "
                f"side={'White' if r.white else 'Black'} "
                f"move={r.mv.uci()} san={r.san}{current}"
            )
            parts.append("BEFORE")
            parts.append(listing(r.before).rstrip("\n"))
            parts.append("AFTER")
            parts.append(listing(r.after).rstrip("\n"))
        text = "\n".join(parts) + "\n"
        self.dir.mkdir(parents=True, exist_ok=True)
        self.path(white).write_text(text, encoding="utf-8")
