#!/usr/bin/env python3
"""Diagraphephobia - PDF 'redigido': AES-128-ECB com a chave escondida nos metadados.

Requer: poppler-utils (pdftotext, pdfinfo) e `pip install cryptography`.
"""
import base64, re, subprocess, sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

path = sys.argv[1] if len(sys.argv) > 1 else "Diagraphephobia.pdf"

# 1) As tarjas pretas so cobrem o texto; ele continua na camada de texto do PDF.
text = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True).stdout
b64 = "".join(re.findall(r"^[A-Za-z0-9+/=]{20,}$", text, re.M))
ct = base64.b64decode(b64)
print(f"ciphertext: {len(ct)} bytes (multiplo de 16: {len(ct) % 16 == 0})")

# 2) A chave (16 bytes) esta no campo Subject dos metadados, escrita em klingon.
info = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
key = re.search(r"^Subject:\s*(.+)$", info, re.M).group(1).strip().encode()
print("chave:", key)

# 3) AES-128 em modo ECB
pt = Cipher(algorithms.AES(key), modes.ECB()).decryptor().update(ct)
print(pt.decode("utf-8", "replace"))
