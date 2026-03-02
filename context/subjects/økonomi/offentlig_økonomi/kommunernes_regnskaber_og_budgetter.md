<fact tables>
<table>
id: nglk
description: Udvalgte kommunale regnskabstal efter område, nøgletal, brutto-/nettoudgifter, prisenhed og tid
columns: omrade, bnogle, brutnetudg, prisenhed, tid (time), indhold (unit Kr.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: regk11
description: Kommunernes regnskaber på hovedkonti efter område, hovedkonto, dranst, art, prisenhed og tid
columns: omrade, funk1, dranst, art, prisenhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: regk31
description: Kommunernes regnskaber på funktioner efter område, funktion, dranst, art, prisenhed og tid
columns: omrade, funktion, dranst, art, prisenhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: regk4
description: Kommunernes balancer efter område, funktion og tid
columns: omrade, funktion, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: regk100
description: Kommunernes regnskaber på gruppering uden tekst efter område, funktion, dranst, ejerforhold, gruppering, art, prisenhed og tid
columns: omrade, funktion, dranst, ejer, gruppering, art, prisenhed, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: regkc
description: Kommunernes regnskaber på gruppering med tekst efter område, dranst funktion og gruppering, ejerforhold, art, prisenhed og tid
columns: omrade, dranst1, ejer, art, prisenhed, tid (time), indhold (unit -)
tid range: 2018-01-01 to 2024-01-01
</table>
<table>
id: regk63
description: Kommunernes finansielle aktiver og passiver efter funktion og tid
columns: funktion, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: regk64
description: Kommunernes likvide beholdninger (1000 kr.) efter funktion og tid
columns: funktion, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: regk65
description: Kommunernes langfristede gæld (1000 kr.) efter funktion og tid
columns: funktion, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: regk73
description: Kommunernes forskydninger i likvide aktiver (1000 kr.) efter funktion, gruppering og tid
columns: funktion, gruppering, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: regk74
description: Kommunernes langfristede låntagning (1000 kr.) efter funktion, dranst og tid
columns: funktion, dranst, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: budk1
description: Kommunernes budgetter, hovedkonti efter kommune, hovedkonto, dranst, art, prisenhed og tid
columns: regi07a, funk1, dranst, art, prisenhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2025-01-01
</table>
<table>
id: budk32
description: Kommunernes budgetter, funktioner efter kommune, funktion, dranst, art, prisenhed og tid
columns: regi07a, funktion, dranst, art, prisenhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2025-01-01
</table>
<table>
id: budk100
description: Kommunernes budgetter, grupperinger uden tekst - efter område, funktion, dranst, ejerforhold, gruppering, art, prisenhed og tid
columns: omrade, funktion, dranst, ejer, gruppering, art, prisenhed, tid (time), indhold (unit 1.000 kr.)
tid range: 2017-01-01 to 2025-01-01
</table>
<table>
id: budkc
description: Kommunernes budgetter, grupperinger med tekst - efter område, dranst funktion og gruppering, ejerforhold, art, prisenhed og tid
columns: omrade, dranst1, ejer, art, prisenhed, tid (time), indhold (unit 1.000 kr.)
tid range: 2019-01-01 to 2025-01-01
</table>
</fact tables>

notes:
- **Regnskab vs budget**: Tables prefixed regk = actual accounts (regnskaber); tables prefixed budk = budgets. Both cover 2007+. Budget tables lead actuals by ~1 year (budk* goes to 2025, regk* to 2024).
- **Granularity ladder (actuals)**: nglk (12 key ratios, easiest) → regk11 (9 main accounts / funk1) → regk31 (355 functions) → regk100/regkc (function × dranst × ejer × gruppering, most granular). Same ladder for budgets: budk1 → budk32 → budk100/budkc.
- **Quick key figures**: Use nglk for ready-made per-capita benchmarks (driftsudgifter, ældreudgifter, gæld, etc.) by region or kommune. Requires filtering bnogle + brutnetudg + prisenhed.
- **Standard expenditure questions**: Use regk11 (actuals) or budk1 (budget) for main account breakdown by region/kommune. Filter: art='TOT', prisenhed='LOBM', and choose dranst (1=drift, 3=anlæg) and funk1.
- **Function-level detail**: Use regk31 (actuals) or budk32 (budget). 355 funktion codes — use ColumnValues with fuzzy search to find the right code.
- **Ownership breakdown**: Use regk100/regkc (actuals) or budk100/budkc (budget). The "c" variants (regkc/budkc) encode dranst+funktion+gruppering as a composite dranst1 key with labels; useful when searching by label text via ColumnValues fuzzy match. The "100" variants have separate columns, easier for SQL filtering.
- **Balance sheet**: regk4 = actuals by region/kommune; regk63 = national-only with explicit AKTIV/PASSIV totals, quarterly to 2025.
- **Liquid assets and debt (national, quarterly)**: regk64 = likvide beholdninger stock; regk65 = langfristet gæld stock; regk73 = changes in liquid assets (flow); regk74 = long-term borrowing flows (new loans vs repayments).
- **Geography column naming**: regk* tables use omrade; budk1/budk32 use regi07a; budk100/budkc use omrade. Both column names join dim.nuts on kode. nivel=1 gives 5 regioner, niveau=3 gives 98–99 kommuner. Extra codes not in dim.nuts: 0=Hele landet, 910=Hovedstadskommuner, 920=Storbykommuner, 930=Provinsbykommuner, 940=Oplandskommuner, 960=Landkommuner.
- **Universal overcounting traps**: (1) prisenhed doubles rows in all tables that have it — always filter to LOBM or INDL. (2) art='TOT' is the net aggregate of UE minus I — never sum TOT with UE or I. (3) funk1='X' is the aggregate of 0–7 — never sum X with individual funk1 codes.
- **Map support**: All tables with omrade/regi07a support choropleth maps — nglk, regk11, regk31, regk4, regk100, regkc, budk1, budk32, budk100, budkc. Use context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1). Tables regk63–regk74 have no geographic column (national only).
