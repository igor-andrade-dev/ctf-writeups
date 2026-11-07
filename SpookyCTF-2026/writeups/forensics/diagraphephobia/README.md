# Diagraphephobia

| | |
|---|---|
| **CTF** | SpookyCTF 2026 • Phobias |
| **Categoria** | Forensics (+ Crypto) |
| **Flag** | `spooky{qaStaH_nuq}` |
| **Script** | [`solve.py`](solve.py) |

**Arquivo:** `Diagraphephobia.pdf` — título "Ja'", parágrafo coberto por tarjas pretas, uma imagem ruidosa e um bloco em base64.

**Raciocínio**
1. As tarjas pretas são só retângulos desenhados por cima. O texto continua na camada de texto do PDF e sai com `pdftotext`.
2. O base64 decodifica para 160 bytes (múltiplo de 16), sem cabeçalho `Salted__`: provavelmente uma cifra de bloco sem IV, como AES-ECB.
3. Os metadados do PDF (`pdfinfo`) têm no campo *Subject* a frase `lojmIt yIpoSmoH!`, em klingon ("abra a porta"). Ela tem exatamente 16 bytes, o tamanho de uma chave AES-128.
4. AES-128-ECB com essa chave decifra um texto em klingon com a flag na última linha. A imagem de fundo era só ilustração.

**Ferramentas:** `pdftotext` e `pdfinfo` (poppler-utils), `pdfimages`, Python com `cryptography`.

## Reproduzir

```bash
python3 solve.py /caminho/para/arquivo-do-desafio
```
