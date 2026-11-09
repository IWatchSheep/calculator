"""After the 1.4M drill finishes, run verify/probe/tally/lists and refresh chess_test_results.txt."""

from __future__ import annotations

import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "raw_outputs"
DIR = ROOT / "game_files_kpk"
REPORT = ROOT / "chess_test_results.txt"
GAMES = 1_400_000


def run(cmd: list[str], out_name: str) -> str:
    RAW.mkdir(parents=True, exist_ok=True)
    print(f">>> {' '.join(cmd)}", flush=True)
    p = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
    text = (p.stdout or "") + (("\n" + p.stderr) if p.stderr else "")
    (RAW / out_name).write_text(text, encoding="utf-8")
    print(text)
    if p.returncode != 0:
        raise SystemExit(p.returncode)
    return text


def patch_report(drill_text: str, verify_text: str, probe_text: str, tally_text: str, lists_text: str) -> None:
    body = REPORT.read_text(encoding="utf-8")
    # Replace the KPK section marker block if present.
    block = []
    block.append("====================================================================================================")
    block.append("3. KING AND PAWN AGAINST KING (KPK): THE SOLUTION (Python)")
    block.append("====================================================================================================")
    block.append("")
    block.append(f"Finished finalize at {datetime.now().isoformat(timespec='seconds')}")
    block.append("")
    block.append("How it was run")
    block.append(f"  python main.py --dir game_files_kpk drill 1 {GAMES}")
    block.append(f"  python verify_kpk.py {GAMES} game_files_kpk")
    block.append("  python probe_kpk.py game_files_kpk")
    block.append("")
    block.append("The drill, in the program's own words")
    for line in drill_text.splitlines():
        if "games:" in line or line.startswith("Done:") or line.startswith("Index:"):
            block.append(f"  {line.strip()}")
    block.append("")
    block.append("The independent check (verify_kpk)")
    for line in verify_text.splitlines():
        if line.startswith("true:") or line.startswith("after "):
            block.append(f"  {line.strip()}")
    block.append("")
    block.append("The solved index (probe_kpk)")
    block.append(probe_text.rstrip())
    block.append("")
    block.append("Strategy flags in the KPK drill archive")
    block.append(tally_text.rstrip())
    block.append("")
    block.append("List examples")
    block.append(lists_text.rstrip())
    block.append("")
    new_section = "\n".join(block) + "\n"
    if "BEGIN_KPK_SECTION" in body:
        body = re.sub(
            r"BEGIN_KPK_SECTION.*?END_KPK_SECTION",
            "BEGIN_KPK_SECTION\n" + new_section + "END_KPK_SECTION",
            body,
            flags=re.S,
        )
    else:
        body += "\n" + new_section
    REPORT.write_text(body, encoding="utf-8")
    print(f"Updated {REPORT}")


def main() -> None:
    py = sys.executable
    drill = (RAW / "drill_1400000.txt").read_text(encoding="utf-8", errors="replace")
    verify = run([py, "verify_kpk.py", str(GAMES), str(DIR)], "verify_kpk_1400000.txt")
    probe = run([py, "probe_kpk.py", str(DIR)], "probe_kpk.txt")
    tally = run([py, "tally_strategies.py", str(DIR)], "strategy_tally.txt")
    lists = run([py, "list_examples.py", str(DIR)], "list_examples.txt")
    patch_report(drill, verify, probe, tally, lists)


if __name__ == "__main__":
    main()
