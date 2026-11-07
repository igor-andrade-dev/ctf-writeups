#!/usr/bin/env python3
"""Recover the activation phrase from the byte table in the challenge ELF."""

TABLE = bytes.fromhex("2a 24 2a 29 43 37 45 50 5c 5d 65 72 74 6f")

# The validation routine checks:
#   table[i] == ((input[i] ^ 0x5d) + 7*i + 0x0b) & 0xff
# Reverse the arithmetic in 8-bit space, then undo XOR.
phrase = bytes((((value - 7 * i - 0x0B) & 0xFF) ^ 0x5D) for i, value in enumerate(TABLE))
print(phrase.decode("ascii"))
