#!/usr/bin/env python3
"""Build the 112-byte self-printing ELF; optionally submit it to the CTF service."""
import argparse
import socket
import struct
from pathlib import Path

HOST = "3.129.162.36"
PORT = 31903


def build_elf() -> bytes:
    ident = b"\x7fELF\x02\x01\x01\x00\x00" + bytes.fromhex("be 00 00 40 00 eb 40")
    ehdr = struct.pack(
        "<16sHHIQQQIHHHHHH",
        ident,
        2, 62, 1,
        0x400009,  # entry point: file offset 9
        56,        # program header overlaps tail of ELF header
        0, 0,
        64, 56, 1,
        0, 5, 0,
    )
    # p_paddr bytes are executed as: write(1, 0x400000, 112)
    write_code = bytes.fromhex("b0 01 ff c7 b2 70 0f 05")
    # p_filesz and p_memsz encode two short jumps (EB 06).
    segment_size = 0x06EB
    # p_align bytes execute: dec edi; mov al, 60; syscall; nop; nop
    exit_code = bytes.fromhex("ff cf b0 3c 0f 05 90 90")
    phdr = struct.pack(
        "<IIQQQQQQ",
        1, 5, 0, 0x400000,
        int.from_bytes(write_code, "little"),
        segment_size, segment_size,
        int.from_bytes(exit_code, "little"),
    )
    elf = bytearray(112)
    elf[:64] = ehdr
    elf[56:112] = phdr
    result = bytes(elf)
    assert len(result) == 112
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit", action="store_true", help="send bytes to the SpookyCTF service")
    args = parser.parse_args()

    elf = build_elf()
    out = Path("elves_spooky_too.elf")
    out.write_bytes(elf)
    print(f"[+] Wrote {out} ({len(elf)} bytes)")

    if not args.submit:
        print("[i] Build only. Run ./verify.py for local verification or use --submit to send it.")
        return

    with socket.create_connection((HOST, PORT), timeout=10) as sock:
        sock.settimeout(10)
        sock.sendall(b"SIZE 112\n" + elf)
        sock.shutdown(socket.SHUT_WR)
        response = bytearray()
        try:
            while True:
                block = sock.recv(4096)
                if not block:
                    break
                response.extend(block)
        except socket.timeout:
            pass
    print(response.decode("utf-8", errors="replace"))


if __name__ == "__main__":
    main()
