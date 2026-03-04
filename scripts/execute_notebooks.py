#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

import nbformat
from nbclient import NotebookClient

SOURCE_ROOT = Path("Pre-algebra")
TARGET_ROOT = Path("executed")
KERNEL_NAME = "python3"


def source_notebooks() -> list[Path]:
    return sorted(p for p in SOURCE_ROOT.rglob("*.ipynb") if p.exists())


def target_for(src: Path) -> Path:
    rel = src.relative_to(SOURCE_ROOT.parent)
    return TARGET_ROOT / rel


def execute_notebook(src: Path, dst: Path) -> None:
    nb = nbformat.read(src, as_version=4)
    client = NotebookClient(nb, timeout=120, kernel_name=KERNEL_NAME)
    client.execute()
    dst.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(nb, dst)


def main() -> int:
    notebooks = source_notebooks()
    if not notebooks:
        print("No source notebooks found.")
        return 0

    for src in notebooks:
        dst = target_for(src)
        execute_notebook(src, dst)
        print(f"executed: {src} -> {dst}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
