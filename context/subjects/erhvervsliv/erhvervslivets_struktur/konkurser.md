<fact tables>
<table>
id: konk3
description: Erklærede konkurser efter nøgletal og tid
columns: bnogle, tid (time), indhold (unit -)
tid range: 2009-01-01 to 2025-09-01
</table>
<table>
id: konk4
description: Erklærede konkurser efter branche, virksomhedstype og tid
columns: branche, virktyp1, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2025-09-01
</table>
<table>
id: konk5
description: Erklærede konkurser efter levetid og tid
columns: levtid, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2025-09-01
</table>
<table>
id: konk6
description: Erklærede konkurser efter omsætning og tid
columns: omsaetning, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2025-09-01
</table>
<table>
id: konk7
description: Erklærede konkurser efter beskæftigede og tid
columns: besk, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2025-09-01
</table>
<table>
id: konk8
description: Erklærede konkurser efter region, virksomhedstype og tid
columns: region, virktyp1, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2025-09-01
</table>
<table>
id: konk9
description: Erklærede konkurser (historisk sammendrag) efter sæsonkorrigering og tid
columns: saeson, tid (time), indhold (unit Antal)
tid range: 1979-01-01 to 2025-09-01
</table>
<table>
id: konk15
description: Erklærede konkurser efter branche (DB07), virksomhedstype og tid
columns: branche07, virktyp1, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2025-09-01
</table>
<table>
id: konkeum
description: Nyregistrerede virksomheder og konkurser efter indikator, branche (DB07) og tid
columns: indikator, branche07, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2025-09-01
</table>
<table>
id: konk10e
description: Konkurser (eksperimentel statistik) efter nøgletal og tid
columns: bnogle, tid (time), indhold (unit Antal)
tid range: 2009U01 to 2025U40
</table>
<table>
id: konk11e
description: Konkurser (eksperimentel statistik) efter nøgletal og tid
columns: bnogle, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2025-09-01
</table>
<table>
id: konk12e
description: Konkurser (eksperimentel statistik) efter nøgletal og tid
columns: bnogle, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2025-01-01
</table>
</fact tables>

notes:
- For long historical trends (back to 1979): use konk9. It's monthly, national total only, with unadjusted and seasonally adjusted series. All other tables start at 2009.
- For regional breakdown (by region): use konk8 — the only table with geographic breakdown. 5 regioner only (niveau 1), plus region=0 as national total.
- For industry breakdown (coarse, ~20 categories): use konk4. For fine-grained DB07 industry detail (736 undergrupper): use konk15 — but the join requires LPAD(d.kode::text,6,'0')=f.branche07 because codes are zero-padded.
- For company characteristics breakdowns: use konk5 (levetid/age), konk6 (omsætning/turnover), konk7 (beskæftigede/employees).
- For multiple measures on one table (counts + turnover + jobs + lifetime averages): use konk3. It has mixed measure types in bnogle — never sum across them.
- For new registrations vs. bankruptcies together: use konkeum (the only table with both BURE and BUBA indicators side by side).
- Experimental tables (konk10e/11e/12e): provide Konkursbegæring (petition filings, K04) as a leading indicator not available in the official series. konk10e=weekly, konk11e=monthly, konk12e=annual.
- virktyp1 appears in konk4, konk8, konk15: always filter to one value (K01=total, K02=aktive, K03=nulvirksomheder). K01=K02+K03 — summing all three triples the count. Same pattern for saeson in konk9 (EJSÆSON vs SÆSON) and indikator in konkeum.
- All single-dimension tables (konk5/6/7) include a total code (000 or BTSXO_S94) that equals the sum of the breakdown categories — exclude it when aggregating by category.
- Map: konk8 supports choropleth at region level — /geo/regioner.parquet, merge on region=dim_kode. No other table in this group has geographic breakdown.