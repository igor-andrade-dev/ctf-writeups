# SpookyCTF 2026 — Write-ups e laboratório

Repositório pessoal de write-ups, scripts e evidências dos desafios do **SpookyCTF 2026 (Phobias)** reunidos a partir das conversas, anexos locais e dos dois pacotes de soluções enviados em 07/11/2026.

> **Spoilers:** contém flags, soluções e payloads de CTF. Mantenha o repositório privado enquanto a competição estiver ativa ou enquanto as regras do evento proibirem a publicação.

## Resumo

- **14 flags registradas** nos write-ups e no material importado.
- **1 desafio BinRev** com ELF validado localmente, mas sem flag/aceitação remota confirmada.
- Outros desafios permanecem em análise ou sem artefatos suficientes.

## Índice de desafios com flag registrada

| Desafio | Categoria | Flag | Evidência / observação |
|---|---|---|---|
| [Frankenstein's Password Generator](writeups/binrev/frankenstein-password-generator/) | BinRev | `spooky{its_alive_at_midnight}` | Frase `BOLTATMIDNIGHT`; binário original executado localmente |
| [Java class checker](writeups/binrev/java-class-checker/) | BinRev | `spooky{ever_reversed_java?A67b_91}` | Classe Java executada; retornou `Correct!` |
| [Cyberphobia: Overflowed Bits](writeups/pwn/cyberphobia-overflowed-bits/) | PWN | `spooky{br4v3Se@O77er}` | Serviço remoto retornou o segredo; a submissão final da flag não está registrada |
| [Graveyard Letter](writeups/crypto/graveyard-letter/) | Crypto | `spooky{eyez_are_watching_me}` | Substituição monoalfabética; write-up importado |
| [Numerophobia](writeups/crypto/numerophobia/) | Crypto | `spooky{th3_4n5w3r_h45_4lw4y5_b33n_42}` | Deslocamento seletivo, reversão e leetspeak; write-up importado |
| [Stash The Hash](writeups/crypto/stash-the-hash/) | Crypto / Stego | `spooky{dleeds_isa_devil}` | MD5 → senha 7z → LSB; write-up importado |
| [Cleithrophobia](writeups/forensics/cleithrophobia/) | Forensics | `Spooky{Be0m_Me_Up_Sc0tty_2266}` | PCAP, HTTP Basic e headers customizados; write-up importado |
| [Diagraphephobia](writeups/forensics/diagraphephobia/) | Forensics / Crypto | `spooky{qaStaH_nuq}` | Extração de texto PDF e AES-128-ECB; write-up importado |
| [Phantom Login](writeups/forensics/phantom-login/) | Forensics | `spooky{the_ghost_left_a_trace}` | Correlação de eventos Windows e logs web; write-up importado |
| [Serial Polyglot](writeups/forensics/serial-polyglot/) | Forensics / Stego / Crypto | `spooky{mu1tipl3_l@ngu@ges}` | Reconstrução XMODEM, steghide e múltiplas codificações; write-up importado |
| [Tangled](writeups/forensics/tangled/) | Forensics | `spooky{8_l3gs_4nd_4_z1p}` | ZIP concatenado após `IEND` de PNG; write-up importado |
| [Tormented Tanny](writeups/forensics/tormented-tanny/) | Forensics | `spooky{tormented_tanner_hates_his_vetsulin}` | Flag dividida em metadados PNG; write-up importado |
| [Eisoptrophobia](writeups/stego/eisoptrophobia/) | Stego | `spooky{the_reflection_never_lies}` | LSB RGB → Base64; write-up importado |
| [Haunted Portrait](writeups/stego/haunted-portrait/) | Stego | `spooky{portraits_keep_secrets}` | Plano LSB azul → ROT13; write-up importado |

O arquivo [`FLAGS.md`](FLAGS.md) contém a lista consolidada em formato compacto.

## Desafios sem flag confirmada

| Desafio | Categoria | Situação |
|---|---|---|
| [Elves can be Spooky Too](writeups/binrev/elves-can-be-spooky-too/) | BinRev | ELF de 112 bytes validado localmente; confirmação remota pendente |
| [J*b Application](writeups/web/jobs-application/) | Web | Análise estática do bypass da regex; flag não disponível |
| [NICC — Network Imaging Control Center](writeups/web/nicc-camera-feeds/) | Web / Recon | Feeds e frames analisados parcialmente |
| [Drown in Memory](writeups/forensics/drown-in-memory/) | Forensics / Game | Build Unreal Engine coletada; extração/solução pendente |
| [Glass Bottle](writeups/forensics/glass-bottle/) | Forensics / Stego | Artefatos coletados; solução pendente |
| [Phasmophobia Challenge](writeups/forensics/phasmophobia/) | Forensics / Stego | Espectrograma investigado; flag não confirmada |
| [Pumpkin Head Message](writeups/crypto/pumpkin-head-message/) | Crypto / Misc | Mensagem preservada; solução pendente |
| [My Message to You](writeups/misc/my-message-to-you/) | Misc / Crypto | Arquivo 7z preservado; solução pendente |
| [Laurel / Tree ID](writeups/osint/laurel-tree-id/) | OSINT | Enunciado e identificação incompletos |
| Hashphobia | Crypto | Apenas hash SHA-256; falta contexto/artefato |

Há também nomes vistos no painel sem contexto suficiente para write-up: **Hemophobia, Scopophobia, Typonophobia, Nosocomophobia, Athazagoraphobia e MIA**. Consulte [`CHALLENGE_BACKLOG.md`](CHALLENGE_BACKLOG.md).

## Estrutura

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

## Ambiente e reprodução

Python 3 é necessário para os scripts. Dependências Python:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Ferramentas externas usadas por alguns write-ups: `binutils` (`nm`, `readelf`, `objdump`), Java/JDK, `poppler-utils` (`pdftotext`, `pdfinfo`), `steghide`, `ffmpeg`/`ffprobe`, `7z` e `retoc` (para o jogo Unreal).

Os scripts normalmente recebem o arquivo original do desafio como argumento. **Nem todos os arquivos de entrada foram incluídos** nos pacotes enviados; baixe-os novamente da plataforma quando necessário. O diretório `evidence/` contém somente as evidências que foram recuperadas e associadas com segurança.

### BinRev — Frankenstein

```bash
cd writeups/binrev/frankenstein-password-generator
python3 solve.py
printf 'BOLTATMIDNIGHT\n' | ./challenge/frankenstein
```

### BinRev — Java class checker

```bash
cd writeups/binrev/java-class-checker
python3 solve.py
```

### BinRev — Elves can be Spooky Too

```bash
cd writeups/binrev/elves-can-be-spooky-too
python3 solve.py                 # constrói o ELF
python3 verify.py                # verifica stdout byte a byte e exit code
python3 solve.py --submit        # envia ao serviço do CTF
```

### PWN — Cyberphobia: Overflowed Bits

```bash
cd writeups/pwn/cyberphobia-overflowed-bits
python3 exploit.py --send
```

O payload registrado preenche 64 bytes e sobrescreve o ponteiro de função com `0x4011d6` (little-endian), endereço obtido com `nm` no binário `EXEC` fornecido.

## Proveniência e validação

- Frankenstein, Java checker e Cyberphobia foram trabalhados diretamente na conversa; as evidências de execução estão descritas nos respectivos write-ups.
- Os dez write-ups adicionais, mais Graveyard Letter, foram importados do pacote `spookyctf-2026.zip` enviado pelo usuário. O segundo pacote (`spookyctf-20262.zip`) era um subconjunto desses arquivos e incluía diretórios vazios malformados; foi usado apenas para comparação, não como fonte principal.
- Scripts importados foram preservados; não foram todos reexecutados porque os respectivos arquivos de entrada originais não acompanham os ZIPs.
- `Drown-in-Memory_Windows.zip` (266.617.151 bytes) foi intencionalmente omitido do Git comum; o SHA-256 está no write-up e em `SOURCE_INVENTORY.md`.
- Confira as regras do evento antes de tornar públicos flags e write-ups.
