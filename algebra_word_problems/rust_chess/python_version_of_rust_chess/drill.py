"""Step 15.6: the drill. Plays both sides of seeded king-and-pawn starts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

from archive import DRILL, Archive
from board import PAWN, Board, Move, rank_of
from history import WINDOW
from index import (
    Counts,
    GameRecord,
    GameResult,
    Index,
    SavedMove,
    Status,
    goal_after,
)
from normalize import normalize, kpk_positions
from strategies import Ctx, TurnInfo, flags_all


class Rng:
    """SplitMix64 seeded generator: a seed always gives the same order."""

    def __init__(self, seed: int) -> None:
        self.state = seed & 0xFFFFFFFFFFFFFFFF

    @staticmethod
    def new(seed: int) -> Rng:
        return Rng(seed)

    def next_u64(self) -> int:
        self.state = (self.state + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
        z = self.state
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & 0xFFFFFFFFFFFFFFFF
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & 0xFFFFFFFFFFFFFFFF
        return z ^ (z >> 31)

    def below(self, n: int) -> int:
        return self.next_u64() % n


_KPK_FOLDED_CACHE: list[Board] | None = None


def _folded_kpk() -> list[Board]:
    global _KPK_FOLDED_CACHE
    if _KPK_FOLDED_CACHE is None:
        _KPK_FOLDED_CACHE = kpk_positions(True)
    return _KPK_FOLDED_CACHE


def start_sequence(seed: int) -> list[Board]:
    """Normalized KPK set, seventh rank first down to second; seed shuffles within rank."""
    all_pos = _folded_kpk()
    by_rank: list[list[Board]] = [[] for _ in range(8)]
    for b in all_pos:
        ps = next(s for s in range(64) if b.sq[s] == PAWN)
        by_rank[rank_of(ps)].append(b)
    rng = Rng.new(seed)
    out: list[Board] = []
    for rank in range(6, 0, -1):
        group = by_rank[rank][:]
        for i in range(len(group) - 1, 0, -1):
            j = rng.below(i + 1)
            group[i], group[j] = group[j], group[i]
        out.extend(group)
    return out


def choose(ix: Index, b: Board) -> Optional[Move]:
    """The drill's move choice (Step 15.6)."""
    n = normalize(b)
    nlegal = n.board.legal_moves()
    if not nlegal:
        return None
    node = ix.lookup(n.key())
    vals: list[Optional[tuple[Status, Counts]]] = []
    for m in nlegal:
        if node is None:
            vals.append(None)
            continue
        nd = ix.nodes[node]
        try:
            i = nd.legal.index(m.uci())
        except ValueError:
            vals.append(None)
            continue
        e = nd.edges[i]
        if e is None:
            vals.append(None)
            continue
        vals.append((ix.edge_value(e), ix.edge_counts(e, None)))

    def pick(i: int) -> Move:
        return n.t.mv(nlegal[i])

    first_untried = next((i for i, v in enumerate(vals) if v is None), None)
    pawn_side = n.cat.proof_family() and n.board.white_to_move

    def rate(i: int) -> float:
        v = vals[i]
        return v[1].win_rate() if v is not None else 0.0

    if (not n.cat.proof_family()) or pawn_side:
        best = None
        for i, v in enumerate(vals):
            if v is not None and v[0].is_win():
                d = v[0].dist
                if best is None or d < best[0]:
                    best = (d, i)
        if best is not None:
            return pick(best[1])
        if first_untried is not None:
            return pick(first_untried)
        bi = 0
        for i in range(1, len(vals)):
            if rate(i) > rate(bi):
                bi = i
        return pick(bi)

    for i, v in enumerate(vals):
        if v is not None and v[0].is_draw():
            return pick(i)
    if first_untried is not None:
        return pick(first_untried)
    if all(v is not None and v[0].is_win() for v in vals):
        worst = None
        for i, v in enumerate(vals):
            if v is not None and v[0].is_win():
                d = v[0].dist
                # longest loss for the pawn side: maximize distance
                if worst is None or d > worst[0]:
                    worst = (d, i)
        if worst is not None:
            return pick(worst[1])
    bi = 0
    for i in range(1, len(vals)):
        if rate(i) < rate(bi):
            bi = i
    return pick(bi)


def mover_flags(after: Board, white: bool, window: list[TurnInfo]) -> list[int]:
    return list(flags_all(Ctx(b=after, white=white, window=window)))


@dataclass
class PlayedGame:
    moves: list[tuple[Board, Move, list[int]]]
    result: str


def play(ix: Index, start: Board) -> PlayedGame:
    """Play one drill game from start, both sides choosing by Step 15.6."""
    b = start
    seen: dict[str, int] = {b.key(): 1}
    quiet = 0
    windows: list[list[TurnInfo]] = [[], []]
    moves: list[tuple[Board, Move, list[int]]] = []
    while True:
        m = choose(ix, b)
        if m is None:
            return PlayedGame(moves=moves, result=GameResult.Draw)
        after = b.make(m)
        white = b.white_to_move
        w = windows[0 if white else 1]
        w.append(
            TurnInfo(
                white=white,
                from_=m.from_,
                to=m.to,
                piece=b.sq[m.from_],
                captured=b.captured_piece(m),
            )
        )
        if len(w) > WINDOW:
            w.pop(0)
        flags = mover_flags(after, white, w)
        pawn_or_capture = abs(b.sq[m.from_]) == PAWN or b.is_capture(m)
        moves.append((b, m, flags))
        r = goal_after(b, m, after)
        if r is not None:
            return PlayedGame(moves=moves, result=r)
        c = seen.get(after.key(), 0) + 1
        seen[after.key()] = c
        if c >= 3:
            return PlayedGame(moves=moves, result=GameResult.DrawByRule)
        quiet = 0 if pawn_or_capture else quiet + 1
        if quiet >= 100:
            return PlayedGame(moves=moves, result=GameResult.DrawByRule)
        b = after


@dataclass
class DrillReport:
    games: int = 0
    pawn_wins: int = 0
    draws: int = 0
    draws_by_rule: int = 0
    first_start: Optional[str] = None


def _read_progress(path: Path) -> dict[int, int]:
    m: dict[int, int] = {}
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return m
    for line in text.splitlines():
        parts = line.split()
        if len(parts) >= 2:
            try:
                m[int(parts[0])] = int(parts[1])
            except ValueError:
                continue
    return m


def _write_progress(path: Path, m: dict[int, int]) -> None:
    keys = sorted(m.keys())
    text = "".join(f"{k} {m[k]}\n" for k in keys)
    path.write_text(text, encoding="utf-8", newline="\n")


def run(
    ix: Index,
    archive: Archive,
    seed: int,
    games: int,
    on_progress: Optional[Callable[[int, Index], None]] = None,
) -> DrillReport:
    """Run `games` drill games for `seed`, continuing where that seed stopped."""
    seq = start_sequence(seed)
    progress_path = archive.root / "drill_progress.txt"
    progress = _read_progress(progress_path)
    pos = progress.get(seed, 0)
    run_file = f"drill_run_{archive.next_id()}.txt"
    rep = DrillReport()
    for g in range(games):
        start = seq[pos % len(seq)]
        pos += 1
        if rep.first_start is None:
            rep.first_start = start.key()
        played = play(ix, start)
        w = archive.begin_game(DRILL, start, run_file)
        for i, (b, m, f) in enumerate(played.moves):
            w.add_move(i + 1, b, m, f)
        id_ = w.id
        w.finish(played.result)
        rec = GameRecord(
            id=id_,
            bank=DRILL,
            start=start,
            moves=[
                SavedMove(uci=m.uci(), flags=list(f))
                for _, m, f in played.moves
            ],
            result=played.result,
        )
        ix.merge(rec)
        rep.games += 1
        if played.result in (GameResult.WhiteWin, GameResult.BlackWin):
            rep.pawn_wins += 1
        elif played.result == GameResult.DrawByRule:
            rep.draws_by_rule += 1
        else:
            rep.draws += 1
        if (g + 1) % 10_000 == 0:
            ix.save(archive.index_path())
            progress[seed] = pos
            _write_progress(progress_path, progress)
        if on_progress is not None:
            on_progress(g + 1, ix)
    ix.save(archive.index_path())
    progress[seed] = pos
    _write_progress(progress_path, progress)
    return rep
