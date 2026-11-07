# Inventário de fontes recuperadas

Atualizado em 07/11/2026 após a importação de dois pacotes de write-ups fornecidos pelo usuário.

## Pacotes importados nesta atualização

- `spookyctf-2026.zip` — fonte principal; 39 entradas, contendo README, requirements e 11 pastas de desafios com write-ups/scripts (11 incluindo Graveyard Letter).
- `spookyctf-20262.zip` — pacote parcial, 22 entradas; subconjunto de arquivos já presentes no primeiro ZIP. Inclui algumas entradas de diretório vazias com caminhos malformados decorrentes de brace expansion. Não foi usado como fonte principal.
- Os 11 write-ups foram incorporados em `writeups/crypto`, `writeups/forensics` e `writeups/stego`. O README geral foi refeito para incluir todos eles; o README fornecido no primeiro ZIP listava apenas parte dos desafios no seu índice.

## Write-ups e scripts importados

- Crypto: Graveyard Letter, Numerophobia, Stash The Hash.
- Forensics: Cleithrophobia, Diagraphephobia, Phantom Login, Serial Polyglot, Tangled, Tormented Tanny.
- Stego: Eisoptrophobia, Haunted Portrait.
- Os scripts `.py` foram preservados. Nem todos puderam ser reexecutados porque os ZIPs de write-up não continham os arquivos originais de entrada de todos os desafios.

## Evidências recuperadas e associadas

- `graveyard_letter.txt` foi copiado para `writeups/crypto/graveyard-letter/evidence/`.
- `serial-capture.log` e `recovered_xmodem.jpg` foram associados ao write-up Serial Polyglot e copiados para `writeups/forensics/serial-polyglot/evidence/`.
- Frankenstein: ZIP original extraído; executável e README local em `writeups/binrev/frankenstein-password-generator/challenge/`.
- Java: classe original preservada como `writeups/binrev/java-class-checker/binary.class`.
- Elves: ELF de 112 bytes, script construtor e verificador local preservados.
- Cyberphobia: `main.c` reconstruído do código-fonte enviado e exploit preservado.
- J*b Application: `app.py` recuperado da biblioteca e incluído.
- Phasmophobia, Glass Bottle, Drown in Memory, My Message to You e NICC: evidências parciais preservadas nas pastas correspondentes.

## Arquivos grandes omitidos

- `Drown-in-Memory_Windows.zip` — 266.617.151 bytes; omitido do Git comum.
  SHA-256: `64e1485d1245db1fadfd6edf30ee582654234b8723bde302062376cdca9cb5b5`.

## Materiais não atribuídos

`FirstImage.JPG`, `SecondImage.jpg` e outras capturas auxiliares foram mantidas fora das pastas dos desafios enquanto não houver associação inequívoca. Não foram usadas para inferir flags.

## Limite da recuperação

O pacote consolidado reflete os anexos e registros recuperáveis nesta sessão e os dois ZIPs fornecidos. Não é uma exportação integral de todo o histórico de conversas da conta. Flags provenientes dos write-ups importados são identificadas como tal; aceitação na plataforma só é afirmada quando houve evidência direta.
