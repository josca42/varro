table: fact.skib481
description: Godstransport med skib mellem danske landsdele efter pålæsningsregion, aflæsningsregion, enhed og tid
measure: indhold (unit -)
columns:
- paregion: values [F000=Fra hele landet, F01=Fra Landsdel Byen København, F02=Fra Landsdel Københavns Omegn, F03=Fra Landsdel Nordsjælland, F04=Fra Landsdel Bornholm, F05=Fra Landsdel Østsjælland, F06=Fra Landsdel Vest- og Sydsjælland, F07=Fra Landsdel Fyn, F08=Fra Landsdel Sydjylland, F09=Fra Landsdel Østjylland, F10=Fra Landsdel Vestjylland, F11=Fra Landsdel Nordjylland, F888=Fra danske søområder]
- afregion: values [T000=Til hele landet, T01=Til Landsdel Byen København, T02=Til Landsdel Københavns Omegn, T03=Til Landsdel Nordsjælland, T04=Til Landsdel Bornholm, T05=Til Landsdel Østsjælland, T06=Til Landsdel Vest- og Sydsjælland, T07=Til Landsdel Fyn, T08=Til Landsdel Sydjylland, T09=Til Landsdel Østjylland, T10=Til Landsdel Vestjylland, T11=Til Landsdel Nordjylland, T888=Til danske søområder]
- enhed: values [75=1000 ton, 76=Mio. tonkm]
- tid: date range 2007-01-01 to 2024-01-01
notes:
- enhed is a unit selector — every paregion+afregion+tid combination appears twice, once per unit. Always filter to one: enhed='75' for 1000 ton, enhed='76' for Mio. tonkm. Never sum across both.
- paregion and afregion use custom prefixed codes (F01–F11, T01–T11) that do NOT join to dim.nuts. The landsdel numbering matches (e.g. F01=Landsdel Byen København = nuts code 1), but you must not join to dim.nuts directly. Use ColumnValues("skib481", "paregion") / ColumnValues("skib481", "afregion") for labels.
- Aggregate/special codes: F000/T000=hele landet (national total), F888/T888=Danske søområder. Exclude these when summing across regions to avoid double-counting.
- This is the only table in the subject showing goods flow as an origin-destination matrix between Danish regions (domestic inland/coastal shipping).
- Map: /geo/landsdele.parquet — strip the F/T prefix and cast to int (e.g. paregion.str[1:].astype(int)) to get dim_kode 1–11. Exclude F000/T000 and F888/T888. Aggregate by origin (paregion) or destination (afregion) before merging.
