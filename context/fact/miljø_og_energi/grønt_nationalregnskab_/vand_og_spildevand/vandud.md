table: fact.vandud
description: Spildevandsudledning efter område, udledning, anlægstype og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- udl: values [SP=Spildevand, 1.000 m3, KV=Kvælstof, ton total-N, FO=Fosfor, ton total-P, OR=Organisk stof, ton BI5]
- anlaeg: values [115=Dambrug, 120=Havbrug, 125=Industriel udledning, 130=Almene renseanlæg, 135=Spredt bebyggelse ikke tilsluttet kloakering, 140=Regnbetinget udledning]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts on omrade=kode. niveau 1 = 5 regioner (kode 81-85), niveau 3 = 99 kommuner. omrade='0' = Danmark i alt (not in dim).
- udl values have DIFFERENT physical units (m3, ton-N, ton-P, ton BI5) — they are completely incomparable. Always filter to exactly one udl value per query; never sum across udl.
- anlaeg (facility types 115–140) are independent discharge sources — safe to sum or filter individually.
- The only wastewater table with regional breakdown. Use vandud for geography questions; use vandrg4 for industry breakdown.
- Sample: nitrogen discharge by facility type for Denmark in 2023:
  SELECT f.anlaeg, f.indhold FROM fact.vandud f WHERE f.omrade='0' AND f.udl='KV' AND f.tid='2023-01-01' ORDER BY f.indhold DESC;
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
