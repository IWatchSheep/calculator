"""Run the measurements that feed chess_test_results.txt for the Python port."""

from __future__ import annotations

import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw_outputs"
DIR = ROOT / "game_files_kpk"
GAMES = 1_400_000


def run(cmd: list[str], out_name: str) -> str:
    RAW.mkdir(parents=True, exist_ok=True)
    print(f"\n>>> {' '.join(cmd)}", flush=True)
    t0 = time.perf_counter()
    p = subprocess.run(
        cmd,
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    text = (p.stdout or "") + (("\n" + p.stderr) if p.stderr else "")
    (RAW / out_name).write_text(text, encoding="utf-8")
    print(text)
    print(f"[exit {p.returncode} in {time.perf_counter() - t0:.1f}s]", flush=True)
    if p.returncode != 0:
        raise SystemExit(p.returncode)
    return text


def main() -> None:
    print(f"Python report suite started {datetime.now().isoformat(timespec='seconds')}")
    print(f"ROOT={ROOT}")
    py = sys.executable

    # 1. unit tests
    run([py, "tests/test_lists12.py"], "unit_lists12.txt")
    run([py, "tests/test_index_basic.py"], "unit_index_basic.txt")
    run([py, "tests/test_perft.py"], "unit_perft.txt")

    # 2. independent retrograde truth (no drill yet)
    run([py, "verify_kpk.py", "0"], "verify_kpk_truth.txt")

    # 3. full KPK drill
    DIR.mkdir(parents=True, exist_ok=True)
    drill_out = RAW / "drill_1400000.txt"
    print(f"\n>>> drill 1 {GAMES} -> {DIR}", flush=True)
    t0 = time.perf_counter()
    with drill_out.open("w", encoding="utf-8") as f:
        f.write(f"started {datetime.now().isoformat(timespec='seconds')}\n")
        f.flush()
        proc = subprocess.Popen(
            [py, "main.py", "--dir", str(DIR), "drill", "1", str(GAMES)],
            cwd=str(ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        assert proc.stdout is not None
        for line in proc.stdout:
            print(line, end="")
            f.write(line)
            f.flush()
        rc = proc.wait()
        f.write(f"\nfinished {datetime.now().isoformat(timespec='seconds')} exit={rc}\n")
        f.write(f"elapsed_s={time.perf_counter() - t0:.1f}\n")
    if rc != 0:
        raise SystemExit(rc)

    # 4. verify against retrograde using the drilled archive
    run([py, "verify_kpk.py", str(GAMES), str(DIR)], "verify_kpk_1400000.txt")

    # 5. probe a few presets from the solved index
    run([py, "probe_kpk.py", str(DIR)], "probe_kpk.txt")

    # 6. strategy tally from the drill archive
    run([py, "tally_strategies.py", str(DIR)], "strategy_tally.txt")

    # 7. list examples
    run([py, "list_examples.py", str(DIR)], "list_examples.txt")

    print(f"\nAll raw outputs in {RAW}")
    print(f"Finished {datetime.now().isoformat(timespec='seconds')}")


if __name__ == "__main__":
    main()
