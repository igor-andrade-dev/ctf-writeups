# Elves can be Spooky Too

**Categoria:** BinRev · **Dificuldade:** Hard · **Limite:** 112 bytes

## Objetivo

Enviar um ELF Linux x86-64 de até 112 bytes que imprima seus próprios bytes, exatamente, em `stdout` e termine com status 0.

## Ideia

O executável usa o próprio cabeçalho ELF como código. Campos que o carregador Linux ignora ou não precisa interpretar para a execução são reaproveitados como instruções x86-64:

- `e_ident` contém o começo do código e o salto para o offset 80.
- O program header começa no offset 56 e se sobrepõe à cauda do cabeçalho ELF.
- Os bytes de `p_paddr` executam `write(1, 0x400000, 112)`.
- `p_filesz` e `p_memsz` codificam saltos curtos.
- `p_align` contém a sequência para `exit(0)`.

O arquivo pode parecer estranho para ferramentas de inspeção (por exemplo, seção ELF inconsistente); o objetivo é que o carregador Linux aceite o segmento de carga necessário.

## Construir e validar localmente

```bash
python3 solve.py
chmod +x elves_spooky_too.elf
python3 verify.py
```

Validação local realizada neste ambiente:

```text
OK: stdout matches all 112 ELF bytes; exit status 0
```

## Envio remoto

O protocolo do desafio é `SIZE <n>\n` seguido de exatamente `n` bytes. Para enviar:

```bash
python3 solve.py --submit
```

**Status remoto:** não há resposta de aceitação/flag registrada nas conversas recuperadas. Portanto, este write-up registra somente a validação local; a submissão remota continua pendente.
