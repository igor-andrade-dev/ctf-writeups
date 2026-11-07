# Haunted Portrait

| | |
|---|---|
| **CTF** | SpookyCTF 2026 • Phobias |
| **Categoria** | Stego |
| **Flag** | `spooky{portraits_keep_secrets}` |
| **Script** | [`solve.py`](solve.py) |

**Arquivo:** `haunted_portrait.png` — pintura escura de um retrato.

**Raciocínio**
1. Sem metadados e sem dados depois do `IEND`.
2. Média do bit menos significativo (LSB) por canal: R ≈ 0,49, G ≈ 0,48, mas **B ≈ 0,036**. Um LSB quase todo em zero não é natural.
3. Renderizando o plano de bits do azul como imagem (bit 1 = branco) aparece um texto: *"THE DEAD SPEAK IN ROT13"* e `fcbbxl{cbegenvgf_xrrc_frpergf}`.
4. ROT13 dá `spooky{portraits_keep_secrets}`.

**Ferramentas:** Python (Pillow, NumPy). Alternativas: `zsteg -a`, Stegsolve, CyberChef (ROT13).

## Reproduzir

```bash
python3 solve.py /caminho/para/arquivo-do-desafio
```
