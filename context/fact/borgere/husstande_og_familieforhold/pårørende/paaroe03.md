table: fact.paaroe03
description: Befolkningen 1. januar efter relation, hovedpersonens bopæl og tid
measure: indhold (unit Antal)
columns:
- relation: values [TOT=Hele befolkningen, K00=Har ingen nære pårørende, K01=Har en partner, K02=Har børn, K03=Har forældre, K04=Har søskende, K05=Har en partner og børn, K06=Har en partner og forældre, K07=Har en partner og søskende, K08=Har børn og forældre, K09=Har børn og søskende, K10=Har forældre og søskende, K11=Har en partner, børn og forældre, K12=Har en partner, børn og søskende, K13=Har en partner, forældre og søskende, K14=Har børn, forældre og søskende, K15=Har en partner, børn, forældre og søskende]
- hovedbopael: join dim.nuts on hovedbopael=kode; levels [3]
- tid: date range 2020-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- relation codes K00–K15 are mutually exclusive — every person appears in exactly one combination category. TOT = sum of K00+K01+…+K15 (verified: they match exactly). Summing K00–K15 gives the correct population total.
- K00 = no close relatives; K15 = all four types (partner + children + parents + siblings). The 16 categories cover all binary combinations.
- hoofdbopael joins dim.nuts only at niveau 3 (99 kommuner) — no national total or regional level in this table. Code 0 is national total and does not join to dim.nuts. Use WHERE f.hoofdbopael != '0' when joining to dim to exclude it, or include it unjoined for the national figure.
- Use ColumnValues("nuts", "titel", for_table="paaroe03") to see available kommuner.
- Sample query — share of population with no close relatives by kommune: SELECT d.titel, SUM(CASE WHEN f.relation='K00' THEN f.indhold ELSE 0 END)::float / SUM(CASE WHEN f.relation='TOT' THEN f.indhold ELSE 0 END) FROM fact.paaroe03 f JOIN dim.nuts d ON f.hoofdbopael = d.kode WHERE f.tid='2024-01-01' GROUP BY d.titel;
- Map: context/geo/kommuner.parquet — merge on hoofdbopael=dim_kode. Exclude hoofdbopael=0.