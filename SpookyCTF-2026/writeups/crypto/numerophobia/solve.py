#!/usr/bin/env python3
"""Numerophobia - cifra numerica (offset de 13 em posicoes alternadas + texto invertido)."""
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "numerophobia.txt"
nums = [int(n) for n in open(path).read().split()]

# Pista "degraus faltando marcados com 13": soma de 13 nas posicoes 1a, 3a, 5a...
dec = [n - 13 if i % 2 == 0 else n for i, n in enumerate(nums)]
text = "".join(chr(n) for n in dec)

# O texto tem 3 linhas (enchimento, miolo, enchimento); o miolo e a flag.
middle = max(text.split("\n"), key=lambda l: sum(c.isalpha() for c in l))
# Pista "livro sobre dislexia": o miolo esta escrito de tras para frente.
print(middle[::-1])
