<fact tables>
<table>
id: glob
description: Fremstillingsvirksomhedernes internationale produktion efter poster, im- og eksport, land og tid
columns: post, indud, land, tid (time), indhold (unit Mio. kr.)
tid range: 2005-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- glob is the only table here. It covers Danish manufacturing firms' international production (global value chains), broken down by transaction type (post), direction (indud: Import/Eksport), and a small set of countries (W1=verden, B6=EU-27, D6=Extra EU-27, DE=Tyskland, US=USA).
- Always filter indud (1=Import, 2=Eksport) — every combination is repeated for both directions.
- For world totals use land = 'W1'; this code is not in dim.lande_uht_bb but is the most useful aggregate.
- The post codes encode BPM6/MITS2010 trade-in-services/goods distinctions — use the full code descriptions from the fact doc when presenting results to users.