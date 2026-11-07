#!/usr/bin/env python3
"""Invert the per-character integer checks in binary.class."""

# Each item is the inverse of one bytecode expression, in character order.
# Java int XOR is signed 32-bit; Python's signed integer XOR gives the same
# result for these negative constants.
chars = [
    (115 - 7) ^ 31,
    73 - (-46 ^ 11),
    (98 ^ 22) - 5,
    70 - (-41),
    (66 - 13) ^ 94,
    37 - (-69 ^ 23),
    (128 ^ 12) - 17,
    86 - (-15),
    (124 - 29) ^ 41,
    66 - (-44 ^ 9),
    (142 ^ 9) - 21,
    70 - (-25),
    (69 - 27) ^ 88,
    14 - (-74 ^ 31),
    (50 ^ 79) - 7,
    58 - (-43),
    (90 - 11) ^ 61,
    27 - (-71 ^ 17),
    (66 ^ 48) - 13,
    113 - 13,
    (136 - 9) ^ 32,
    69 - (-57 ^ 28),
    (96 ^ 13) - 12,
    81 - (-37),
    (69 - 15) ^ 87,
    31 - (-62 ^ 34),
    (23 ^ 68) - 18,
    49 - (-5),
    (27 - 21) ^ 49,
    86 - (-15 ^ 5),
    (105 ^ 30) - 24,
    75 - 18,
    (85 - 27) ^ 11,
    48 - (-72 ^ 11),
]

flag = "".join(map(chr, chars))
assert len(flag) == 34
print(flag)

# Optional runtime verification. Run this script beside binary.class.
import shutil
import subprocess
if shutil.which("java"):
    result = subprocess.run(["java", "binary", flag], text=True, capture_output=True)
    print(result.stdout.strip())
    if result.returncode != 0 or "Correct!" not in result.stdout:
        raise SystemExit("Java validation failed")
