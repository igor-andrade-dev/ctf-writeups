# Eisoptrophobia

| | |
|---|---|
| **CTF** | SpookyCTF 2026 • Phobias |
| **Categoria** | Stego |
| **Flag** | `spooky{the_reflection_never_lies}` |
| **Script** | [`solve.py`](solve.py) |

**Arquivo:** `Eisoptrophobiactf.png` — mulher diante de um espelho (1365×2048).

**Raciocínio**
1. Sem metadados e sem dados depois do `IEND`. Os riscos vermelhos no espelho são parte da arte.
2. Os planos de bits 0 e 1 parecem grão de foto, e a média ficou perto de 0,5, então a triagem estatística não ajudou.
3. Varredura de LSB testando combinações de canais (R, G, B, RGB, BGR…), número de bits, ordem de leitura (linha, coluna, invertida) e ordem de bits (big/little endian), procurando `spooky`, assinaturas de arquivo e trechos longos de texto legível.
4. O resultado veio da leitura mais simples: LSB de **R, G, B em ordem de linha, a partir do primeiro pixel**. A mensagem é `c3Bvb2t5e3RoZV9yZWZsZWN0aW9uX25ldmVyX2xpZXN9`, que termina em um byte nulo.
5. Base64 decodifica para `spooky{the_reflection_never_lies}`.

**Observação:** a varredura também achou assinaturas de `gz` e `jpg` em vários lugares. São falsos positivos, já que bytes aleatórios do ruído coincidem às vezes com cabeçalhos de arquivo.

**Ferramentas:** Python (Pillow, NumPy). Alternativa: `zsteg -a`.

## Reproduzir

```bash
python3 solve.py /caminho/para/arquivo-do-desafio
```
