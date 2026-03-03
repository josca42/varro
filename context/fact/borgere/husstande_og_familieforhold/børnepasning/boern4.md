table: fact.boern4
description: Institutioner og enheder efter område, pasningstilbud, ejerform og tid
measure: indhold (unit Antal)
columns:
- blstkom: join dim.nuts on blstkom=kode; levels [3]
- pastil: values [60=Dagplejer, 61=Daginstitution på forældrebestyrelses niveau, 69=Daginstitution på enheds niveau, 63=SFO, 62=Fritidshjem, 64=Klub, 65=Integreret institution, 66=Puljeordning]
- ejerform: values [0=Alle ejerformer, 70=Kommunal, 71=Selvejende, 72=Privat, 73=Udliciteret, 66=Puljeordning]
- tid: date range 2017-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- blstkom contains kode 0 (national total, not in dim.nuts) and niveau 3 (98 kommuner) only — no regional breakdown.
- ejerform=0 (Alle ejerformer) is the aggregate for each pastil type. Never sum across all ejerform values — ejerform=0 already contains the sum of 70+71+72+73. Filter to either ejerform=0 OR specific ejerform codes.
- pastil=65 (Integreret institution) only exists in 2017 data — the category was discontinued.
- pastil=66 (Puljeordning) only appears with ejerform=66 (itself) — not with the standard ejerform codes.
- indhold counts institutions (or units at the enheds-niveau for pastil=69). Comparing pastil=61 (forældrebe-styrelses niveau) and pastil=69 (enheds niveau) gives different granularities of the same daginstitutioner.
- Map: /geo/kommuner.parquet — merge on blstkom=dim_kode. Exclude blstkom=0.
