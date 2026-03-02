<fact tables>
<table>
id: foder1
description: Foderforbruget efter fodermiddel, oprindelse, enhed og tid
columns: foder2, oprind, enhed, tid (time), indhold (unit -)
tid range: 1990 to 2025
</table>
<table>
id: foder2
description: Fordeling af foder efter fodermiddel, anvendelse og tid
columns: foder2, vandty, tid (time), indhold (unit Mio. kg)
tid range: 1992-01-01 to 2024-01-01
</table>
<table>
id: foder3
description: Produktion af foder efter foderblanding, periode og tid
columns: foder1, periode, tid (time), indhold (unit Mio. kg)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: foder6
description: Værdiberegning for foderstoffer efter foder, enhed og tid
columns: foder, maengde4, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: kvael2
description: Den samlede handelsgødningsforsyning/Indhold af rene næringsstoffer efter stoftype, måleenhed og tid
columns: stoftype, maleenhed, tid (time), indhold (unit -)
tid range: 1983 to 2024
</table>
<table>
id: pest1
description: Salget af pesticider til anvendelse i landbrugets planteavl samt behandlingshyppighed efter pesticidgruppe, måleenhed og tid
columns: pesticidgr, maleenhed, tid (time), indhold (unit -)
tid range: 1981-01-01 to 2023-01-01
</table>
<table>
id: pest2
description: Det samlede pesticidsalg efter pesticidtype, måleenhed og tid
columns: pesticidtype, maleenhed, tid (time), indhold (unit -)
tid range: 1981-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- All 7 tables in this subject have a measurement selector column (enhed, maleenhed, or maengde4) that silently multiplies row counts if not filtered. Always filter to exactly one selector value before aggregating.
- For feed consumption (foderforbrug): use foder1 (1990–) for breakdowns by origin (Danish vs imported) and unit (weight/feed units/protein), or foder2 (1992–) for breakdown by usage type (foderblandinger vs enkeltfoderstof) in weight only.
- For feed production: use foder3 (1990–, compound feed production by type). Note the periode selector: KAAR=calendar year, DAAR=farm year — always pick one.
- For feed value/price: use foder6 (2000–), which has amount + price per 100 kg + total value via maengde4.
- For fertilizer: kvael2 covers commercial fertilizer supply in N, P, K from 1983. Simple table — just filter maleenhed (MIOKG or KGPRHA).
- For pesticides in agricultural crop production with treatment frequency index: use pest1 (1981–2023, 4 pesticid groups, 4 metrics).
- For total pesticide sales across all sectors: use pest2 (1981–2023, 14 types, product weight vs active substance). Use TOT for consistent long-run series — type classifications changed around 2015.
- foder1 and kvael2 have int4range tid (harvest-year windows). Filter with `WHERE tid @> 2024` not `WHERE tid = 2024`.