# Cleithrophobia

**Categoria:** Forensics (network / pcap)
**Flag:** `Spooky{Be0m_Me_Up_Sc0tty_2266}`

## Enunciado

> Preso na Enterprise, tripulação sumiu, nave parada no espaço. Talvez o
> arquivo de pacotes (`Cleithrophobia.pcap`) tenha como ligar a nave.

## Raciocínio

1. O `.pcap` tem ~2000 pacotes, boa parte ruído (TCP/443 aleatório, ARP, NTP,
   DNS, ICMP, UDP tipo `sensor_sweep=` / `heartbeat=stardate-`).
2. ~20 requisições `POST /bridge/ignition` para
   `bridge.ncc1701.starfleet.local`, cada uma com header HTTP Basic Auth —
   "ligar a nave" = endpoint de ignição.
3. Decodificando cada header Basic (base64 `usuario:senha`) e cruzando com a
   resposta no mesmo stream TCP: todas as combinações erram (401 IGNITION
   DENIED), exceto `captain.kirk:Enterprise-1701-A` (pacote 403), que retorna
   `200 IGNITION AUTHORIZED`.
4. A resposta de sucesso carrega a flag dividida em três headers custom
   (`deflector_part1/2/3`), cada um em base64. Concatenados e decodificados,
   formam a flag.
5. Sessões FTP (scotty, sulu, chekov) e os payloads `deflector=` em UDP/TCP
   são iscas — decodificam pra bytes aleatórios, não fazem parte da flag.

## Ferramentas

- `scapy` para parsear o pcap e navegar pelos streams TCP
- `base64` para decodificar credenciais e headers

## Rodar

```bash
python3 solve.py path/to/Cleithrophobia.pcap
```
