# Numerophobia

| | |
|---|---|
| **CTF** | SpookyCTF 2026 • Phobias |
| **Categoria** | Crypto |
| **Flag** | `spooky{th3_4n5w3r_h45_4lw4y5_b33n_42}` |
| **Script** | [`solve.py`](solve.py) |

**Arquivo:** `numerophobia.txt` — três linhas de números entre 10 e 138.

**Pistas da história:** "degraus faltando marcados com 13" (deslocamento de 13), "livro sobre dislexia" (texto invertido), e o número 42.

**Raciocínio**
1. Valores acima de 127 não cabem em ASCII, então há um deslocamento somado em alguma posição.
2. Subtraindo 13 dos números nas posições ímpares (1º, 3º, 5º…), tudo vira ASCII. O `23` do começo vira `10` (quebra de linha), o que dá as três linhas esperadas.
3. As linhas externas são enchimento (`2424…`). O miolo sai de trás para frente: `}24_n33b_...{ykoops`.
4. Invertendo o miolo e lendo o leetspeak (3=e, 4=a, 5=s), a mensagem é "the answer has always been 42", referência a *O Guia do Mochileiro das Galáxias*.

**Ferramentas:** Python. No CyberChef é incômodo, porque "subtrair só nos ímpares" não tem receita pronta.

## Reproduzir

```bash
python3 solve.py /caminho/para/arquivo-do-desafio
```
