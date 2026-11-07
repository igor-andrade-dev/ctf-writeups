#!/usr/bin/env python3
"""Haunted Portrait - esteganografia LSB: texto desenhado no plano de bits 0 do canal azul."""
import codecs, sys
import numpy as np
from PIL import Image

path = sys.argv[1] if len(sys.argv) > 1 else "haunted_portrait.png"
a = np.array(Image.open(path).convert("RGB"))

# Triagem estatistica: media do bit menos significativo de cada canal.
for c, name in enumerate("RGB"):
    print(name, "LSB medio:", round(float((a[:, :, c] & 1).mean()), 3))
# O canal azul fica em ~0.036 (os demais ~0.49): ha algo desenhado ali.

# Renderiza o plano de bits (1 = branco) e abre-se a imagem para ler o texto.
Image.fromarray(((a[:, :, 2] & 1) * 255).astype("uint8")).save("haunted_lsb_blue.png")
print("plano salvo em haunted_lsb_blue.png (leia o texto da imagem)")

# O texto lido na imagem estava em ROT13:
rot13_text = "fcbbxl{cbegenvgf_xrrc_frpergf}"
print("flag:", codecs.decode(rot13_text, "rot13"))
