#!/usr/bin/env python3
"""
Stash The Hash - SpookyCTF 2026
Flag: spooky{dleeds_isa_devil}

1) le o hash MD5 do UserAccountInfo.txt
2) quebra contra uma wordlist (rockyou.txt)
3) usa a senha encontrada para abrir o .7z
4) extrai o PNG e amplifica o plano de bits LSB pra revelar a flag
"""
import sys
import re
import hashlib
import py7zr
from PIL import Image
import numpy as np


def get_hash_from_account_info(path: str) -> str:
    text = open(path, "r", errors="ignore").read()
    m = re.search(r"Password:\s*([0-9a-f]{32})", text)
    if not m:
        raise ValueError("hash MD5 nao encontrado em " + path)
    return m.group(1)


def crack_md5(target: str, wordlist_path: str) -> str | None:
    with open(wordlist_path, "rb") as f:
        for line in f:
            w = line.rstrip(b"\n").rstrip(b"\r")
            if hashlib.md5(w).hexdigest() == target:
                return w.decode()
    return None


def extract_7z(archive_path: str, password: str, out_dir: str) -> str:
    with py7zr.SevenZipFile(archive_path, mode="r", password=password) as z:
        names = z.getnames()
        z.extractall(path=out_dir)
    return names[0]


def reveal_lsb_flag(png_path: str, out_path: str = "lsb_vis.png"):
    im = Image.open(png_path).convert("RGBA")
    arr = np.array(im)
    lsb = (arr & 1) * 255
    Image.fromarray(lsb.astype("uint8")).save(out_path)
    print(f"[+] Visualizacao do LSB salva em {out_path} (leia a flag no topo)")


def main():
    if len(sys.argv) != 4:
        print(f"uso: {sys.argv[0]} <UserAccountInfo.txt> <secretKnowledgeFolder.7z> <rockyou.txt>")
        sys.exit(1)

    account_info, archive, wordlist = sys.argv[1:4]

    target_hash = get_hash_from_account_info(account_info)
    print(f"[+] Hash alvo: {target_hash}")

    password = crack_md5(target_hash, wordlist)
    if not password:
        print("[-] Senha nao encontrada na wordlist")
        sys.exit(1)
    print(f"[+] Senha quebrada: {password}")

    name = extract_7z(archive, password, "extracted")
    png_path = f"extracted/{name}"
    print(f"[+] Extraido: {png_path}")

    reveal_lsb_flag(png_path)
    print("\nFLAG: spooky{dleeds_isa_devil}  (confira em lsb_vis.png)")


if __name__ == "__main__":
    main()
