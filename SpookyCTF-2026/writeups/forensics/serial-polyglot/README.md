# Serial Polyglot

*(nome não-oficial — a plataforma não deu um título pro desafio, só o
arquivo `serial-capture.log` e a dica "so many languages... so many ways
to interpret data")*

**Categoria:** Forensics (protocolo serial) + Stego (steghide) + Crypto (multi-encoding)
**Flag:** `spooky{mu1tipl3_l@ngu@ges}`

## Arquivos

- `serial-capture.log` — captura de um analisador lógico/serial, linhas
  `> ...` (enviado pelo dispositivo) e `< ...` (ACK do host), em hex.

## Raciocínio

1. O padrão dos pacotes (`SOH, blockno, ~blockno, 128 bytes, checksum`,
   ACK `0x06` do host) é o protocolo **XMODEM**.
2. Reconstruindo todos os pacotes `>` em ordem e removendo o framing,
   dá pra remontar o(s) arquivo(s) transferido(s).
3. Tem **dois arquivos** na mesma sessão: o primeiro EOT (`0x04`) fecha o
   arquivo 1 e os números de bloco reiniciam em 1 pro arquivo 2.
   - **Arquivo A** (377.344 bytes): um `.jpg` — print do jogo
     *Supermarket Simulator*.
   - **Arquivo B** (256 bytes, com padding `0x1A`): um bilhete em **latim**:
     > *"Ut clavem invenias ad plura de 'loco' cognoscenda, intellegere
     > debes quid imago tibi significet. Est id quod 'supermercado' vocant!"*
     > ("Para achar a chave... entenda o que a imagem significa. É o que
     > chamam de 'supermercado'!")
4. A dica aponta pra esteganografia com **senha = `supermercado`**.
   `steghide extract -sf fileA.jpg -p supermercado` extrai um payload.
5. O payload tem **duas camadas de encoding** coladas:
   - uma sequência de escapes hex `\xNN` (texto em **português**, Latin-1,
     terminando em `...O bandeira é spooky{mu1tipl3_`)
   - seguida de uma lista de **bytes decimais separados por espaço**
     (`108 64 110 103 117 64 103 101 115 125`), que lidos como ASCII dão
     `l@ngu@ges}`
6. Concatenando as duas partes: `spooky{mu1tipl3_l@ngu@ges}`.

## Ferramentas

- parser Python próprio pra remontar o XMODEM
- `steghide` (linha de comando) pra extração
- decodificação manual hex-escape + bytes decimais

## Rodar

```bash
python3 solve.py serial-capture.log
```

Requer o binário `steghide` instalado (`apt-get install steghide`).

## Evidência recuperada nesta consolidação

O arquivo `evidence/serial-capture.log` está incluído. A etapa de reconstrução do parser foi executada novamente e produziu:

- Arquivo A: 377.344 bytes (JPEG recebido via XMODEM, incluindo padding final do protocolo).
- Arquivo B: 256 bytes (bilhete com a pista em latim).

`evidence/recovered_xmodem.jpg` é uma cópia previamente recuperada de 377.221 bytes: ela corresponde ao prefixo do Arquivo A, sem os 123 bytes finais de padding. Para reproduzir o fluxo completo, use o `serial-capture.log` como entrada do script.
