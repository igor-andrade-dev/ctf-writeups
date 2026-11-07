#!/usr/bin/env python3
"""
Cleithrophobia - SpookyCTF 2026
Flag: Spooky{Be0m_Me_Up_Sc0tty_2266}

Varre o pcap em busca de POST /bridge/ignition, testa cada credencial
HTTP Basic contra a resposta no mesmo stream TCP e remonta a flag a
partir dos headers deflector_part1/2/3 da resposta 200.
"""
import sys
import re
import base64
from scapy.all import rdpcap, IP, TCP, Raw


def find_flag(pcap_path: str) -> str | None:
    packets = rdpcap(pcap_path)

    # mapeia cada requisicao de ignicao (por stream) -> credencial decodificada
    ignition_requests = {}
    for i, pkt in enumerate(packets):
        if TCP in pkt and Raw in pkt and b"/bridge/ignition" in pkt[Raw].load:
            m = re.search(rb"Basic (\S+)", pkt[Raw].load)
            if not m:
                continue
            cred = base64.b64decode(m.group(1)).decode()
            key = (pkt[IP].src, pkt[TCP].sport, pkt[IP].dst, pkt[TCP].dport)
            ignition_requests[key] = (i, cred)

    # procura a resposta correspondente (direcao invertida, mesma porta)
    for i, pkt in enumerate(packets):
        if TCP in pkt and IP in pkt and Raw in pkt:
            key = (pkt[IP].dst, pkt[TCP].dport, pkt[IP].src, pkt[TCP].sport)
            if key in ignition_requests:
                req_i, cred = ignition_requests[key]
                payload = bytes(pkt[Raw].load)
                if b"IGNITION AUTHORIZED" in payload:
                    print(f"[+] Credencial valida: {cred} (pacote {req_i})")
                    # as 3 partes vem em headers custom, cada um no formato
                    # X-Qualquer-Coisa: deflector_partN=<base64>
                    parts = dict(
                        re.findall(rb"deflector_part(\d)=(\S+)", payload)
                    )
                    flag = "".join(
                        base64.b64decode(parts[str(n).encode()]).decode()
                        for n in sorted(int(k) for k in parts)
                    )
                    return flag
    return None


def main():
    if len(sys.argv) != 2:
        print(f"uso: {sys.argv[0]} <Cleithrophobia.pcap>")
        sys.exit(1)

    flag = find_flag(sys.argv[1])
    print(f"\nFLAG: {flag}")


if __name__ == "__main__":
    main()
