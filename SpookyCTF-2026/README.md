# SpookyCTF 2026 — Write-ups

Este repositório reúne minhas anotações, soluções e scripts usados durante o **SpookyCTF 2026 (Phobias)**. A ideia é deixar registrado como resolvi cada desafio, quais ferramentas usei e o que ainda falta investigar.

> **Atenção: spoilers.** Há flags, soluções e payloads neste repositório. Mantenha-o privado enquanto a competição estiver acontecendo ou se as regras do evento não permitirem a divulgação.

## Progresso

- 14 flags registradas nos write-ups.
- 1 desafio de BinRev com o ELF validado localmente, mas sem confirmação de aceitação no serviço remoto.
- Outros desafios continuam em análise ou ainda não têm material suficiente para uma solução.

## Desafios com flag registrada

| Desafio | Categoria | Flag | Como foi resolvido / observações |
|---|---|---|---|
| [Frankenstein's Password Generator](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/binrev/frankenstein-password-generator) | BinRev | `spooky{its_alive_at_midnight}` | A frase `BOLTATMIDNIGHT` foi testada no binário original, localmente. |
| [Java class checker](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/binrev/java-class-checker) | BinRev | `spooky{ever_reversed_java?A67b_91}` | A classe Java foi executada e retornou `Correct!`. |
| [Cyberphobia: Overflowed Bits](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/pwn/cyberphobia-overflowed-bits) | PWN | `spooky{br4v3Se@O77er}` | O serviço remoto retornou o segredo. Não tenho registro da confirmação da submissão final da flag. |
| [Graveyard Letter](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/crypto/graveyard-letter) | Crypto | `spooky{eyez_are_watching_me}` | Substituição monoalfabética. |
| [Numerophobia](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/crypto/numerophobia) | Crypto | `spooky{th3_4n5w3r_h45_4lw4y5_b33n_42}` | Deslocamento seletivo, reversão e leetspeak. |
| [Stash The Hash](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/crypto/stash-the-hash) | Crypto / Stego | `spooky{dleeds_isa_devil}` | MD5, senha de arquivo 7z e extração por LSB. |
| [Cleithrophobia](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/forensics/cleithrophobia) | Forensics | `Spooky{Be0m_Me_Up_Sc0tty_2266}` | Análise de PCAP, HTTP Basic e headers customizados. |
| [Diagraphephobia](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/forensics/diagraphephobia) | Forensics / Crypto | `spooky{qaStaH_nuq}` | Extração de texto de PDF e descriptografia AES-128-ECB. |
| [Phantom Login](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/forensics/phantom-login) | Forensics | `spooky{the_ghost_left_a_trace}` | Correlação de eventos do Windows com logs web. |
| [Serial Polyglot](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/forensics/serial-polyglot) | Forensics / Stego / Crypto | `spooky{mu1tipl3_l@ngu@ges}` | Reconstrução XMODEM, steghide e análise de diferentes codificações. |
| [Tangled](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/forensics/tangled) | Forensics | `spooky{8_l3gs_4nd_4_z1p}` | Identificação de um ZIP concatenado após o marcador `IEND` de um PNG. |
| [Tormented Tanny](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/forensics/tormented-tanny) | Forensics | `spooky{tormented_tanner_hates_his_vetsulin}` | A flag estava dividida nos metadados de um PNG. |
| [Eisoptrophobia](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/stego/eisoptrophobia) | Stego | `spooky{the_reflection_never_lies}` | Extração por LSB em RGB e decodificação Base64. |
| [Haunted Portrait](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/stego/haunted-portrait) | Stego | `spooky{portraits_keep_secrets}` | Extração pelo plano LSB azul e decodificação ROT13. |

A lista de flags também está disponível em [`FLAGS.md`](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/FLAGS.md).

## Desafios em andamento

| Desafio | Categoria | Situação |
|---|---|---|
| [Elves can be Spooky Too](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/binrev/elves-can-be-spooky-too) | BinRev | ELF de 112 bytes validado localmente. Falta confirmar o resultado no serviço remoto. |
| [J\*b Application](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/web/jobs-application) | Web | Bypass da regex analisado estaticamente; flag ainda não obtida. |
| [NICC — Network Imaging Control Center](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/web/nicc-camera-feeds) | Web / Recon | Feeds e frames parcialmente analisados. |
| [Drown in Memory](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/forensics/drown-in-memory) | Forensics / Game | Build da Unreal Engine coletada; extração e solução ainda pendentes. |
| [Glass Bottle](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/forensics/glass-bottle) | Forensics / Stego | Artefatos coletados; falta concluir a análise. |
| [Phasmophobia Challenge](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/forensics/phasmophobia) | Forensics / Stego | Espectrograma analisado, mas a flag ainda não foi confirmada. |
| [Pumpkin Head Message](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/crypto/pumpkin-head-message) | Crypto / Misc | Mensagem preservada; solução pendente. |
| [My Message to You](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/misc/my-message-to-you) | Misc / Crypto | Arquivo 7z preservado; solução pendente. |
| [Laurel / Tree ID](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/writeups/osint/laurel-tree-id) | OSINT | Ainda faltam informações para fechar a identificação. |
| Hashphobia | Crypto | Tenho apenas o hash SHA-256; falta o contexto ou o arquivo original. |

Também anotei alguns nomes que apareceram no painel, mas ainda não tenho informações suficientes para montar um write-up: **Hemophobia, Scopophobia, Typonophobia, Nosocomophobia, Athazagoraphobia e MIA**. Eles estão listados em [`CHALLENGE_BACKLOG.md`](https://github.com/igor-andrade-dev/ctf-writeups/blob/main/SpookyCTF-2026/CHALLENGE_BACKLOG.md).

## Organização dos arquivos

```text
writeups/
  binrev/       # Frankenstein, Java checker, Elves
  pwn/          # Cyberphobia
  crypto/       # Graveyard Letter, Numerophobia, Stash The Hash, Pumpkin Head
  forensics/    # Cleithrophobia, Diagraphephobia, Phantom Login, Serial Polyglot,
                # Tangled, Tormented Tanny, Drown in Memory, Glass Bottle, Phasmophobia
  stego/        # Eisoptrophobia, Haunted Portrait
  web/          # J*b Application, NICC
  misc/         # My Message to You
  osint/        # Laurel / Tree ID
```

## Ambiente

Os scripts usam Python 3. Para preparar o ambiente:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Alguns desafios também dependem de ferramentas instaladas no sistema:

- `binutils` (`nm`, `readelf` e `objdump`)
- Java / JDK
- `poppler-utils` (`pdftotext` e `pdfinfo`)
- `steghide`
- `ffmpeg` e `ffprobe`
- `7z`
- `retoc` (para o desafio baseado em Unreal Engine)

Nem todos os arquivos originais dos desafios estão neste repositório. Quando um script precisar de um desses arquivos, baixe-o novamente pela plataforma do CTF. O diretório `evidence/` contém apenas os materiais que consegui recuperar e associar a cada desafio.

## Alguns comandos de reprodução

### Frankenstein's Password Generator

```bash
cd writeups/binrev/frankenstein-password-generator
python3 solve.py
printf 'BOLTATMIDNIGHT\n' | ./challenge/frankenstein
```

### Java class checker

```bash
cd writeups/binrev/java-class-checker
python3 solve.py
```

### Elves can be Spooky Too

```bash
cd writeups/binrev/elves-can-be-spooky-too
python3 solve.py          # gera o ELF
python3 verify.py         # confere a saída byte a byte e o código de saída
python3 solve.py --submit # envia ao serviço do CTF
```

### Cyberphobia: Overflowed Bits

```bash
cd writeups/pwn/cyberphobia-overflowed-bits
python3 exploit.py --send
```

Nesse desafio, o payload usa 64 bytes de preenchimento e sobrescreve o ponteiro de função com `0x4011d6` em little-endian. O endereço foi identificado com `nm`, usando o binário `EXEC` fornecido no desafio.

## Notas

- Frankenstein, Java class checker e Cyberphobia foram analisados e executados durante a resolução; os detalhes estão nos respectivos write-ups.
- Parte dos outros write-ups veio do arquivo `spookyctf-2026.zip`. Mantive os scripts, mas não consegui executar todos novamente porque os arquivos originais de entrada não estavam incluídos.
- O arquivo `Drown-in-Memory_Windows.zip` (266.617.151 bytes) ficou fora do Git por causa do tamanho. O SHA-256 está registrado no write-up e em `SOURCE_INVENTORY.md`.
- Antes de publicar flags ou soluções, confira as regras do evento.
