#!/usr/bin/env python3
"""
Serial Polyglot - SpookyCTF 2026
Flag: spooky{mu1tipl3_l@ngu@ges}

1) parseia o log serial (framing XMODEM) e remonta os 2 arquivos transferidos
2) extrai o payload escondido no JPEG via steghide (senha = "supermercado",
   pista deixada em latim no 2o arquivo)
3) decodifica as duas camadas de encoding do payload (hex-escape + bytes
   decimais) e concatena pra formar a flag
"""
import sys
import re
import subprocess


def parse_xmodem_blocks(log_path: str):
    """Retorna a lista de blocos SOH enviados pelo dispositivo (direcao '>')."""
    lines = open(log_path, "r", encoding="latin1").read().split("\n")

    blocks = []
    cur_dir, cur_bytes = None, []

    def flush():
        if cur_dir is not None:
            blocks.append((cur_dir, bytes(cur_bytes)))

    for line in lines:
        if line.startswith("> ") or line.startswith("< "):
            flush()
            cur_dir, cur_bytes = line[0], []
        elif line.strip() == "--":
            flush()
            cur_dir = None
        else:
            hexpart = re.split(r"  +", line.strip())[0] if line.strip() else ""
            for h in hexpart.strip().split():
                if re.fullmatch(r"[0-9a-fA-F]{2}", h):
                    cur_bytes.append(int(h, 16))
    flush()
    return [b for d, b in blocks if d == ">"]


def split_files(soh_blocks):
    """Separa os arquivos transferidos usando os marcadores EOT (0x04)."""
    payload_blocks = [b for b in soh_blocks if len(b) >= 3 and b[0] == 0x01]

    eot_idx = [i for i, b in enumerate(soh_blocks) if len(b) == 1 and b[0] == 0x04]
    # indice (em soh_blocks) do primeiro bloco de dados apos o 1o EOT
    restart_idx = eot_idx[0] + 1 if eot_idx else None

    # converte indice em soh_blocks -> indice em payload_blocks
    file_a, file_b = bytearray(), bytearray()
    payload_i = 0
    for i, b in enumerate(soh_blocks):
        if len(b) >= 3 and b[0] == 0x01:
            target = file_b if (restart_idx is not None and i >= restart_idx) else file_a
            target += b[3:3 + 128]
    return bytes(file_a), bytes(file_b)


def steghide_extract(jpg_path: str, password: str, out_path: str):
    subprocess.run(
        ["steghide", "extract", "-sf", jpg_path, "-xf", out_path, "-p", password, "-f"],
        check=True, capture_output=True,
    )
    return open(out_path, "rb").read()


def decode_payload(raw: bytes) -> str:
    content = raw.decode("latin1")
    m = re.search(r"((?:\\x[0-9a-fA-F]{2})+)(.*)", content, re.DOTALL)
    hexpart, rest = m.group(1), m.group(2)

    hex_bytes = bytes(int(hexpart[i + 2:i + 4], 16) for i in range(0, len(hexpart), 4))
    hex_text = hex_bytes.decode("latin1")

    nums = [int(x) for x in rest.strip().split()]
    tail_text = "".join(chr(n) for n in nums)

    return hex_text + tail_text


def main():
    if len(sys.argv) != 2:
        print(f"uso: {sys.argv[0]} <serial-capture.log>")
        sys.exit(1)

    soh_blocks = parse_xmodem_blocks(sys.argv[1])
    file_a, file_b = split_files(soh_blocks)

    open("fileA.jpg", "wb").write(file_a)
    open("fileB.txt", "wb").write(file_b)
    print(f"[+] Arquivo A (imagem): {len(file_a)} bytes -> fileA.jpg")
    print(f"[+] Arquivo B (pista em latim): {len(file_b)} bytes -> fileB.txt")
    print("    " + file_b.decode("latin1").split("\x1a")[0].strip().replace("\n", " "))

    raw = steghide_extract("fileA.jpg", "supermercado", "hidden.txt")
    print("[+] steghide extraiu hidden.txt usando a senha 'supermercado'")

    message = decode_payload(raw)
    print(f"[+] Mensagem decodificada: {message!r}")

    flag = re.search(r"spooky\{.*\}", message).group(0)
    print(f"\nFLAG: {flag}")


if __name__ == "__main__":
    main()
