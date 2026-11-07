# Phantom Login (NJIT)

**Categoria:** Forensics
**Flag:** `spooky{the_ghost_left_a_trace}`

## Enunciado

> Halloween night at NJIT. Às 3:13 AM a equipe de segurança detectou atividade
> de autenticação incomum numa conta "esquecida". O SOC recuperou logs de
> segurança do Windows e de acesso web, mas a evidência está escondida entre
> centenas de eventos normais.

## Arquivos

- `PLAYER_README.md`, `case_notes.txt`
- `njit_security.csv` — export de Windows Security Event Log
- `njit_web.log` — log de acesso web

## Raciocínio

1. Os eventos "normais" (4624 tipo 3 rotineiro, requests `GET /`, `/static/...`,
   `/api/health`) foram filtrados para sobrar só o que destoa.
2. Às `01:48–01:54` há 14 falhas de logon (4625, `0xC000006D`) pra
   `administrator` vindas de `198.51.100.66` — isca de brute-force que nunca
   tem sucesso.
3. Às `03:10–03:12` há 9 falhas de logon (4625, `0xC000006A` — senha errada
   pra usuário válido) pra `evelyn.graves`, de `203.0.113.77`.
4. Às `03:14` um 4624 tipo 3 (NTLM) bem-sucedido pra `evelyn.graves`, mesmo IP,
   `LogonID 0xB130`.
5. `03:15`: 4672 (privilégios especiais) no mesmo LogonID.
6. `03:17`: 4672 → 5140, acesso ao compartilhamento `\\BW-FS01\Archives$`.
7. No log web, do mesmo IP: `GET /archives/`, `/archives/records?year=1893`,
   `GET /archives/export?note=<base64>`.
8. O parâmetro `note` em base64 decodifica direto pra flag.

## Ferramentas

- `pandas` para filtrar o CSV de eventos
- `grep`/regex no log web
- `base64` para decodificar o parâmetro final

## Rodar

```bash
python3 solve.py path/to/njit_security.csv path/to/njit_web.log
```
