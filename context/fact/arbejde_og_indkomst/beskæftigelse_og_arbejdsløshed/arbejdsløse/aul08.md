table: fact.aul08
description: Fuldtidsledige efter område, personer/pct., højest fuldførte uddannelse, alder, køn og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [2]
- perpct: values [L=Fuldtidsledige (antal), L10=Procent af arbejdsstyrken]
- hfudd: join dim.ddu_udd on hfudd=kode [approx]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/ddu_udd.md, /dim/nuts.md

notes:
- hfudd does NOT join dim.ddu_udd. The fact doc link is wrong. hfudd uses a custom H-prefixed classification (H10=Grundskole, H20=Gymnasiale, H30=Erhvervsfaglige, H40=KVU, H50=MVU, H60=Bachelor, H70=LVU, H80=Ph.d., H90=Uoplyst) with sub-codes (e.g. H1001, H3010). Use ColumnValues("aul08", "hfudd") to see all 92 codes with text. Do not join dim.ddu_udd.
- perpct is a measurement selector: L=Fuldtidsledige antal, L10=Procent af arbejdsstyrken. Every row exists twice — once per perpct. Always filter to one perpct before aggregating.
- omrade joins dim.nuts at niveau=2 only (11 landsdele). Extra code 0=Hele landet not in dim.
- Only table in this subject with education breakdown. Stopped at 2024-01 (no aulk equivalent).
- Map: context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.