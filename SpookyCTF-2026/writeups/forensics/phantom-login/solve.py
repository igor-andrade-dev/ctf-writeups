#!/usr/bin/env python3
"""
Phantom Login (NJIT) - SpookyCTF 2026
Flag: spooky{the_ghost_left_a_trace}

Reconstroi a cadeia de eventos do ataque a partir dos logs de
segurança do Windows (njit_security.csv) e de acesso web (njit_web.log),
e extrai a flag codificada em base64 no parametro `note` da requisicao
de exportacao do arquivo.
"""
import sys
import re
import base64
import pandas as pd


def analyze_security_log(csv_path: str) -> str | None:
    df = pd.read_csv(csv_path)

    # eventos fora do ruido rotineiro
    noise = df["details"].astype(str).str.contains(
        "Routine security event|LogonType=3; AuthenticationPackage=Negotiate",
        regex=True, na=False,
    )
    anomalous = df[~noise].sort_values("timestamp_utc")
    print("=== Eventos anomalos ===")
    print(anomalous.to_string(index=False))

    # conta comprometida: aquela com falhas (4625) seguidas de sucesso (4624)
    accounts_with_failures = set(
        anomalous.loc[anomalous["event_code"] == 4625, "account"]
    )
    accounts_with_success = set(
        anomalous.loc[anomalous["event_code"] == 4624, "account"]
    )
    compromised = accounts_with_failures & accounts_with_success
    compromised.discard("administrator")  # isca de brute-force, nunca autentica
    if compromised:
        account = sorted(compromised)[0]
        print(f"\n[+] Conta comprometida: {account}")
        return account
    return None


def find_flag_in_weblog(log_path: str) -> str | None:
    with open(log_path, "r", errors="ignore") as f:
        content = f.read()

    m = re.search(r"/archives/export\?note=([A-Za-z0-9+/=]+)", content)
    if not m:
        return None
    b64 = m.group(1)
    flag = base64.b64decode(b64).decode()
    return flag


def main():
    if len(sys.argv) != 3:
        print(f"uso: {sys.argv[0]} <njit_security.csv> <njit_web.log>")
        sys.exit(1)

    analyze_security_log(sys.argv[1])
    flag = find_flag_in_weblog(sys.argv[2])
    print(f"\nFLAG: {flag}")


if __name__ == "__main__":
    main()
