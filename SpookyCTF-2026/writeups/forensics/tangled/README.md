# Tangled

| | |
|---|---|
| **CTF** | SpookyCTF 2026 • Phobias |
| **Categoria** | Forensics |
| **Flag** | `spooky{8_l3gs_4nd_4_z1p}` |
| **Script** | [`solve.py`](solve.py) |

**Arquivo:** `tangled.png` — logo do SpookyCTF com uma aranha e teias.

**Raciocínio**
1. Listando os chunks do PNG, sobram **214 bytes depois do `IEND`**.
2. Os bytes começam com `PK\x03\x04`, a assinatura de ZIP, e dentro há `flag.txt`.
3. Visualizadores leem o PNG só até o `IEND`, então a imagem abre normalmente.

**Ferramentas:** Python (`struct`, `zipfile`). Alternativas: `binwalk -e`, `unzip imagem.png`, `strings`.

## Reproduzir

```bash
python3 solve.py /caminho/para/arquivo-do-desafio
```
