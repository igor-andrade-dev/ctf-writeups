# NICC — Network Imaging Control Center

**Categoria provável:** Web / Recon · **Status:** investigação parcial

## Alvo observado

`http://18.189.35.130/`

As notas de terminal recuperadas registram enumeração de feeds de câmera e respostas HTML com pistas em comentários.

## Rotas observadas

| Rota | Resultado registrado | Observação |
|---|---|---|
| `/feeds/service/sc-12` | HTTP 200 | Comentário: `Service feed migration incomplete`; aponta namespace redundante `/feeds/mirror/` |
| `/feeds/service/sc-12/frame` | HTTP 200 | Retorna GIF animado |
| `/feeds/mirror/cam-19` | HTTP 200 | Comentário: `Restricted camera migration`; diz que a imagem usa um diretório de três letras |
| `/feeds/mirror/cam-19/frame` | GIF de 10 frames | Extraído para inspeção com `ffmpeg` |
| `/feeds/legacy/cam-07` | HTTP 200 | Feed legado encontrado |
| `/feeds/archived/cam-07` | HTTP 404 | Testado |
| `/feeds/archival/cam-07` | HTTP 404 | Testado |
| `/feeds/decommissioned/cam-07` | HTTP 404 | Testado |
| `/feeds/active/CAM-07` | HTTP 404 | Testado |

## Pistas relevantes

- O HTML de `cam-19` marca o feed como `UNREGISTERED CAMERA`, `LEGACY ROUTING` e `ACCESS CLASS: RESTRICTED`.
- O JavaScript da aplicação contém o comentário `The final feed holds the cryptid frame until playback is reset.`
- O feed `cam-19` tem 10 frames e duração de 2,6 segundos, segundo `ffprobe`.
- Foram montadas contact sheets de `cam-19` e `sc-12` para revisão visual.

## Próximos passos

1. Revisar todos os frames dos GIFs, em especial o último frame e estados após reset/replay.
2. Examinar o diretório de três letras sugerido no comentário da rota `cam-19`.
3. Comparar rotas e nomes de feed em `app.js` e respostas de erro.
4. Registrar a flag somente quando ela aparecer em uma resposta reproduzível.

**Flag:** não registrada nas notas recuperadas.
