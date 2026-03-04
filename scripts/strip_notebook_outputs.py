#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def staged_notebooks() -> list[Path]:
    cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"]
    out = subprocess.check_output(cmd, text=True)
    paths = [Path(p.strip()) for p in out.splitlines() if p.strip().endswith(".ipynb")]
    return [p for p in paths if p.exists()]


def clear_outputs(path: Path) -> bool:
    nb = json.loads(path.read_text())
    changed = False

    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        if cell.get("outputs"):
            cell["outputs"] = []
            changed = True
        if cell.get("execution_count") is not None:
            cell["execution_count"] = None
            changed = True

    if changed:
        path.write_text(json.dumps(nb, indent=1, ensure_ascii=True) + "\n")
    return changed


def main() -> int:
    notebooks = staged_notebooks()
    if not notebooks:
        return 0

    changed = []
    for nb in notebooks:
        if clear_outputs(nb):
            changed.append(str(nb))

    if changed:
        subprocess.check_call(["git", "add", *changed])
        print("Cleared notebook outputs:")
        for path in changed:
            print(f"- {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
