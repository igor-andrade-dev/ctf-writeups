# Java class checker — reverse engineering

**Categoria:** BinRev · **Arquivo:** `binary.class` (class file Java 8 / major version 52)

## Análise

Comecei identificando o arquivo e descompilando o bytecode:

```bash
file binary.class
javap -c -p binary
```

O método privado `check(String)` exige uma string de 34 caracteres e aplica uma expressão aritmética/XOR independente a cada `charAt(i)`. As constantes de comparação são visíveis no bytecode; não é necessário adivinhar a flag por força bruta.

O script `solve.py` inverte cada expressão, monta a string e, quando o Java está instalado, chama o próprio verificador.

## Resultado

```text
spooky{ever_reversed_java?A67b_91}
Correct!
```

**Validação:** a classe fornecida foi executada localmente e retornou `Correct!` para a string reconstruída. O título original deste desafio não ficou identificado nas notas recuperadas, por isso a pasta usa um nome descritivo.
