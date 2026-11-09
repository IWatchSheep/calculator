# Forming Strategies Chess (Python)

Python port of `forming_chess-main`. Behavior follows `rules/rules.txt`.

## Run

From this folder:

```
python main.py
python main.py --dir game_files
python main.py --fen "<fen>"
python main.py perft <depth> [fen]
python main.py drill [seed] [games]
python main.py rebuild-index
```

Tests:

```
python tests/test_lists12.py
python tests/test_index_basic.py
python tests/test_perft.py
```

## Package layout

| File | Purpose |
|---|---|
| `board.py` | Board, legal moves, SAN, check, mate, draws, perft |
| `strategies.py` | The 20 templates |
| `exchange.py` | Capture values |
| `evaluate.py` | Lists 1 and 2 |
| `history.py` | The two history files |
| `normalize.py` | Position keys, color flip and mirror |
| `index.py` | Position index and proof rules |
| `lists34.py` | Lists 3 and 4 |
| `archive.py` | Game files, banks, rebuild |
| `drill.py` | King-and-pawn drill |
| `main.py` | Console program |

No third-party chess libraries. Standard library only.
