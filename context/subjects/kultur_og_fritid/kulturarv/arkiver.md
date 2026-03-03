<fact tables>
<table>
id: arkiv01
description: Aktivitet og personale på Rigsarkivet (Statens Arkiver) efter arkiver, nøgletal og tid
columns: arkiv, aktp, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: arkiv03
description: Aktivitet og personale på Rigsarkivet (Statens Arkiver) efter nøgletal og tid
columns: aktp, tid (time), indhold (unit -)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: arkiv02b
description: Aktivitet og personale på stads- og lokalarkiver efter område, nøgletal og tid
columns: blstkom, aktp, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Two institution types: arkiv01/arkiv03 cover Rigsarkivet (the national state archives); arkiv02b covers stads- og lokalarkiver (municipal/local archives). Don't mix them.
- For national archives by location: use arkiv01 (2007–2024, 7 then 4 sub-archives). For digital metrics (website visits, GB of digital holdings): use arkiv03 (2011–2024, no sub-archive breakdown).
- For local/municipal archives by geography: use arkiv02b (2016–2024, breakdowns by 10 landsdele, excluding Bornholm).
- All three tables use aktp as a measurement selector column — it defines what indhold means (shelf metres, visitors, FTE staff, etc). Always filter to one aktp value; summing across aktp is meaningless.
- arkiv01 and arkiv02b share the same set of aktp codes. arkiv03 has the same plus three digital ones (ITBES, ITSML, ITTIL).
- In arkiv01, code TOT is the national aggregate across sub-archives; in arkiv02b, code 0 is the national aggregate across landsdele. Exclude these when summing across the breakdown dimension.
- Map: arkiv02b supports choropleth at landsdel level via /geo/landsdele.parquet — merge on blstkom=dim_kode. arkiv01 and arkiv03 have no geographic breakdown.