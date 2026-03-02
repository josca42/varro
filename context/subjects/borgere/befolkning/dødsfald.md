<fact tables>
<table>
id: dod
description: Døde efter alder, køn og tid
columns: alder, kon, tid (time), indhold (unit Antal)
tid range: 1974-01-01 to 2024-01-01
</table>
<table>
id: fod207
description: Døde efter område, alder, køn og tid
columns: omrade, alder, kon, tid (time), indhold (unit Antal)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: doddag
description: Døde efter dødsdag, dødsmåned og tid
columns: ddag, dman, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: doda1
description: Døde efter dødsårsag, alder, køn og tid
columns: arsag, alder, kon, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2022-01-01
</table>
<table>
id: dodb1
description: Døde efter dødsårsag, køn og tid
columns: arsag, kon, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2022-01-01
</table>
<table>
id: dod2
description: Døde under 5 år efter køn, alder og tid
columns: kon, alder, tid (time), indhold (unit Antal)
tid range: 1901-01-01 to 2024-01-01
</table>
<table>
id: ligehi5a
description: Ligestillingsindikator for døde efter indikator, dødsårsag, alder og tid
columns: indikator, arsag, alder, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2022-01-01
</table>
</fact tables>

notes:
- For all-cause deaths by age and sex (no region): use dod (1974–2024, individual ages 0–98 + 99-).
- For regional breakdown: use fod207 (2006–2024, region or kommune via dim.nuts niveau 1 or 3).
- For cause of death (grouped, with age): use doda1 (2007–2022, 24 A-level cause groups, grouped ages).
- For cause of death (granular, no age): use dodb1 (2007–2022). WARNING: arsag contains both A-level aggregates and B-level specific diseases — always filter to one level (LIKE 'A%' or LIKE 'B%') to avoid double-counting.
- For gender equality rates in mortality: use ligehi5a (2007–2022). Values are rates per 100,000, not counts. Filter indikator to M1, K1, or F1.
- For child mortality (under 5): use dod2 (1901–2024) — the longest series in this subject.
- For deaths by day/month of year (seasonality): use doddag (2007–2024).
- kon coding is inconsistent across tables: dod/fod207 use M/K (no total); doda1/dodb1 use 1/2 with TOT; dod2 uses D/P; ligehi5a has no kon column (indikator handles sex).
- doda1 and dodb1 both cover 2007–2022 cause-of-death data. They share the same arsag A-level taxonomy. Use doda1 when you need age breakdown; use dodb1 when you need fine B-level disease detail.
- Map: fod207 supports choropleth maps — context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) via omrade=dim_kode. Exclude omrade=0.