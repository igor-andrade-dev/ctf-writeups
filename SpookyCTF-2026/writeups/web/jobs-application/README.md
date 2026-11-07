# J*b Application

**Categoria:** Web · **Status:** análise estática parcial

## Observação principal

O código-fonte Flask contém esta validação:

```python
valid_letter = re.match(r"^[A-Za-z0-9 .,!?'-]{1,40}", coverletter)
```

A regex começa com `^`, mas não termina com `$`. Portanto, `re.match` valida apenas um prefixo permitido e não exige que o restante da string também pertença ao conjunto de caracteres. Em seguida, o código verifica separadamente se a string contém:

```text
[[AI-REVIEW: ACCEPT]]
```

Isso cria uma inconsistência entre a validação do prefixo e a verificação do marcador. Uma string como `A[[AI-REVIEW: ACCEPT]]` passa pela regex porque o primeiro caractere é permitido e contém o marcador requerido.

A rota exige também os demais campos do formulário e uma posição da allowlist (`developer`, `security`, `sysadmin`, `data` ou `intern`).

## Limitação

O arquivo recuperado define `FLAG` por variável de ambiente e usa `spooky{NOT_THE_FLAG}` apenas como valor padrão. Não há flag real nem prova de submissão/aceitação remota registrada. O código foi preservado para análise, mas a solução final permanece pendente.
