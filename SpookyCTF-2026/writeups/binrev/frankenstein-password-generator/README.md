# Frankenstein's Password Generator

**Categoria:** BinRev · **Dificuldade:** Medium

## Objetivo

O executável Linux x86-64 exige uma frase de ativação. A pista do enunciado é: “A bolt at midnight gave it life.”

## Análise

O ELF está stripped, mas `strings` revela as mensagens e o `objdump -d -M intel` permite localizar a rotina de validação em `0x401176`.

A rotina exige exatamente 14 caracteres. Para cada posição `i`, compara o byte armazenado na tabela em `0x402010` com:

```text
((input[i] XOR 0x5d) + 7*i + 0x0b) mod 256
```

A inversão é direta:

```text
input[i] = (table[i] - 7*i - 0x0b) mod 256 XOR 0x5d
```

## Solução

```bash
python3 solve.py
# BOLTATMIDNIGHT

printf 'BOLTATMIDNIGHT\n' | ./challenge/frankenstein
```

Saída observada ao executar o binário localmente:

```text
The laboratory lights flicker. IT'S ALIVE!
The creature whispers: spooky{its_alive_at_midnight}
```

## Resultado

- Frase de ativação: `BOLTATMIDNIGHT`
- Flag: `spooky{its_alive_at_midnight}`
- **Validação:** confirmada executando o binário original fornecido no ZIP.
