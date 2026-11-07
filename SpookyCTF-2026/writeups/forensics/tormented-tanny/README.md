# Tormented Tanny

| | |
|---|---|
| **CTF** | SpookyCTF 2026 • Phobias |
| **Categoria** | Forensics |
| **Flag** | `spooky{tormented_tanner_hates_his_vetsulin}` |
| **Script** | [`solve.py`](solve.py) |

**Arquivo:** `TormentedTanny.png` — foto de um poodle assustador.

**Raciocínio**
1. Pixels sem nada e sem dados depois do `IEND`.
2. A flag foi dividida em três metadados:

| Local | Conteúdo |
|-------|----------|
| chunk `tEXt` (*Title*) | `spooky{tormented_tanner_` |
| chunk `iTXt` (XMP, *dc:description*) | `hates_his_` |
| chunk `eXIf` (*ImageDescription*) | `vetsulin}` |

3. Concatenando na ordem: `spooky{tormented_tanner_hates_his_vetsulin}`.

**Ferramentas:** Python (Pillow, parser de chunks), `strings`. A ferramenta ideal é `exiftool -a -G1 arquivo.png`, que mostra todos os campos de uma vez. Ela não estava disponível no ambiente em que resolvi.

## Reproduzir

```bash
python3 solve.py /caminho/para/arquivo-do-desafio
```
