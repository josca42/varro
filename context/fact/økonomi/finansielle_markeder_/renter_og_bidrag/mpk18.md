table: fact.mpk18
description: Gennemsnitsrenter i pengeinstitutterne (pct. p.a.) efter sektor, ud-/indlån og tid
measure: indhold (unit Pct. pro anno)
columns:
- sektor: join dim.esa on sektor=kode [approx]
- udindlan: values [INDLÅN=Indlån, UDLÅN=Udlån]
- tid: date range 2002-01-01 to 2025-04-01
dim docs: /dim/esa.md
notes:
- sektor is effectively an inline column. The fact table uses codes WITHOUT dots (S11, S12, S13, S14) while dim.esa uses dotted codes (S.11, S.12, S.13, S.14) — the join fails. Do NOT attempt to join to dim.esa.
- Sektor values and their meaning: TOT=alle sektorer, S11=ikke-finansielle selskaber, S012=finansielle selskaber (note: S012 not S12), S13=offentlig forvaltning og service, S14=husholdninger, S141S142=personligt ejede virksomheder, S143S145=lønmodtagere mv., 100=ikke-finansielle + finansielle + husholdninger (sub-total), 50=kun pengeinstitutter (sub-total).
- udindlan is a direction selector: INDLÅN or UDLÅN. Filter to one value — the table contains both independently (not aggregated together).
- TOT/100/50 are aggregate totals — include both sub-sectors already. Filter to sektor='TOT' for all sectors combined.
- Monthly data from 2002.
