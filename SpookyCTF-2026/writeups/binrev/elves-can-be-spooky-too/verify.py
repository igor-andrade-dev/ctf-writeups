#!/usr/bin/env python3
"""Run the ELF locally and verify it writes its exact bytes and exits 0."""
from pathlib import Path
import subprocess

elf = Path("elves_spooky_too.elf").read_bytes()
result = subprocess.run(["./elves_spooky_too.elf"], capture_output=True)
assert result.returncode == 0, f"exit code: {result.returncode}"
assert result.stdout == elf, f"stdout was {len(result.stdout)} bytes; ELF is {len(elf)} bytes"
print(f"OK: stdout matches all {len(elf)} ELF bytes; exit status 0")
