# Stash The Hash

**Categoria:** Crypto (quebra de hash) + Stego (secundário, LSB em PNG)
**Flag:** `spooky{dleeds_isa_devil}`

## Enunciado

> Arquivo com informações de um cryptid famoso. A conta dele guarda
> informação sobrenatural proibida. Descubra a senha para obter o conteúdo.

## Arquivos

- `UserAccountInfo.txt` — dump estilo `net user`, com usuário `dleeds`
  (Daniel "DevilLeeds" Leeds, depto. "Horror Management", e-mail
  `dleeds@galloway.com`) e uma "Password" de 32 chars hex (hash MD5).
- `secretKnowledgeFolder.7z` — arquivo `.7z` com nomes e conteúdo
  criptografados.

## Raciocínio

1. O campo "Password" não é uma senha, é um **hash MD5**
   (`ad7bcd7ab3cc113f496e1840bc582bbd`).
2. O nome "DevilLeeds" + e-mail `@galloway.com` apontam pro
   **Jersey Devil** (lenda do "Leeds Devil", Leeds Point / Galloway, NJ).
3. Quebrando o MD5 contra o `rockyou.txt` completo (14.3M senhas):
   `MD5("newjerseydevils") == ad7bcd7ab3cc113f496e1840bc582bbd`.
4. Usando `newjerseydevils` como senha do `.7z`, extrai-se
   `secretKnowledge.png` — uma arte sem texto visível, metadados limpos,
   sem dados após o chunk `IEND`.
5. Amplificando o **bit menos significativo (LSB)** de cada canal RGBA da
   imagem, aparece o texto `spooky{dleeds_isa_devil}` escrito no ruído.

## Ferramentas

- `hashlib` (MD5) + `rockyou.txt` para quebrar o hash
- `py7zr` para extrair o `.7z` com a senha encontrada
- `Pillow` + `numpy` para extrair e amplificar o plano de bits LSB

## Rodar

```bash
# precisa do rockyou.txt na mesma pasta (ou passar o caminho)
python3 solve.py UserAccountInfo.txt secretKnowledgeFolder.7z rockyou.txt
```

O script salva a visualização do LSB como `lsb_vis.png` — a flag aparece
no topo da imagem.
