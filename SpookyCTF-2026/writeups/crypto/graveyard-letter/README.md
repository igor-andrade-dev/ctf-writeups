# Graveyard Letter

| | |
|---|---|
| **CTF** | SpookyCTF 2026 • Phobias |
| **Categoria** | Crypto |
| **Flag** | `spooky{eyez_are_watching_me}` |
| **Script** | [`solve.py`](solve.py) |

**Arquivo:** `graveyard_letter.txt` — carta embaralhada.

**Raciocínio**
1. Espaços e pontuação estão intactos e as frequências batem com inglês, então é **substituição monoalfabética**.
2. Pela saudação `Ypejpof Erpveaypj,` ("Dearest Alexander,") saem as primeiras letras da chave. `D` sozinho é "I", `D'mp` é "I've", `fcp` é "the", `Bwof` é "Just".
3. Decifrada a carta, uma linha em minúsculas, `pzps ejp xefgcdau hp`, é a flag, e o texto manda trocar espaços por underscores e "embrulhar corretamente".
4. **Pegadinha:** a cifra `s` não aparecia na chave, e a frase não é "eyes", é **"eyez"**. A chave é uma permutação do alfabeto: com 25 letras já mapeadas, só o `z` sobra, então `s → z`. Aceitar "eyes" porque "faz sentido" estava errado.

**Chave (cifra → claro):** `abcdefghijklmnopqrstuvwxyz → njhiatcmbrqovkseplzfgxuwdy`

**Ferramentas:** Python. Alternativas: dcode.fr (monoalphabetic substitution) e quipqiup.

**Lição:** em cifra de substituição, decodifique letra por letra com a chave e use a permutação para fechar as que faltam. Quando a chave e o bom senso divergem, vale a chave.

## Reproduzir

```bash
python3 solve.py /caminho/para/arquivo-do-desafio
```
