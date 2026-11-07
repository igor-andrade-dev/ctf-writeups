#!/usr/bin/env python3
"""Graveyard Letter - substituicao monoalfabetica (chave recuperada por analise de palavras)."""
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "graveyard_letter.txt"

CIPHER = "abcdefghijklmnopqrstuvwxyz"
PLAIN  = "njhiatcmbrqovkseplzfgxuwdy"   # cifra -> texto claro (s->z fecha a permutacao)

table = {}
for c, p in zip(CIPHER, PLAIN):
    table[c] = p
    table[c.upper()] = p.upper()

text = open(path).read()
decoded = "".join(table.get(ch, ch) for ch in text)
print(decoded)

# A linha em minusculas, "eyez are watching me", e a flag; a carta manda
# trocar espacos por underscores e embrulhar no formato da flag.
for line in decoded.splitlines():
    if line and line[0].islower():
        phrase = line.split(".")[0].strip()          # "eyez are watching me"
        print("\nFLAG: spooky{%s}" % phrase.replace(" ", "_"))
        break
