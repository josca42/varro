table: fact.turist4
description: Overnatninger på mindre hoteller og campingpladser efter overnatningsform, område, gæstens nationalitet og tid
measure: indhold (unit Antal)
columns:
- overnatf: values [122=Hoteller (10-39 senge), 144=Campingpladser (10-74 enheder)]
- omrade: join dim.nuts on omrade=kode; levels [1]
- nation1: values [TOT=I alt, DAN=Danmark, UDLAN=Verden udenfor Danmark, BELU=Belgien, BUL=Bulgarien ... THA=Thailand, SØA=Asien uden Kina, Japan, Sydkorea, Indien og Thailand, AUS=Australien, OCEX=Oceanien uden Australien, ANDRE=Ukendt land]
- tid: date range 2016-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Niche table: covers only small establishments — hoteller with 10–39 beds (code 122) and campingpladser with 10–74 units (code 144). Not for overall accommodation statistics; use turist or turist2 for that.
- omrade: only niveau 1 (5 regioner: kode 81–85) plus omrade=0 (national total, not in dim.nuts). No landsdel breakdown. Join: JOIN dim.nuts d ON f.omrade = d.kode — all matched codes are niveau 1 (no need to filter by niveau).
- omrade=0 is the national aggregate, not in dim.nuts.
- No periode column and no saeson column — simplest structure of the four tables. Each tid is a direct monthly observation with no sub-period ambiguity.
- Counts overnatninger (overnight stays), same measure as turist.
- Limited time range: 2016–2024. Ends at 2024 — may not have the latest data.
- Map: context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.