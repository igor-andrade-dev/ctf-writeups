#!/usr/bin/env python3
"""Eisoptrophobia - LSB de R,G,B (ordem de linha) contendo uma string base64."""
import base64, sys
import numpy as np
from PIL import Image

path = sys.argv[1] if len(sys.argv) > 1 else "Eisoptrophobiactf.png"
a = np.array(Image.open(path).convert("RGB"))

bits = (a & 1).reshape(-1)                 # R0 G0 B0 R1 G1 B1 ... (linha por linha)
data = np.packbits(bits[: 8 * 200]).tobytes()
b64 = data.split(b"\x00")[0].decode()      # a mensagem termina no primeiro byte nulo
print("base64:", b64)
print("flag  :", base64.b64decode(b64 + "=" * (-len(b64) % 4)).decode())
