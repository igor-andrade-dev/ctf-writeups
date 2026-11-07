#!/usr/bin/env python3
"""Tangled - ZIP anexado depois do chunk IEND do PNG."""
import io, sys, zipfile

path = sys.argv[1] if len(sys.argv) > 1 else "tangled.png"
data = open(path, "rb").read()

end = data.rfind(b"IEND") + 8          # 4 bytes do nome + 4 bytes de CRC
trailer = data[end:]
print(f"{len(trailer)} bytes depois do IEND; assinatura: {trailer[:4]!r}")   # PK\x03\x04

zf = zipfile.ZipFile(io.BytesIO(trailer))
for name in zf.namelist():
    print(name, "->", zf.read(name).decode().strip())
