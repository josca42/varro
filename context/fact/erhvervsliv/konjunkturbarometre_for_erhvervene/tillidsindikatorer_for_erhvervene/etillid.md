table: fact.etillid
description: Tillidsindikatorer for erhvervene efter indikator og tid
measure: indhold (unit Indeks)
columns:
- indikator: values [TE=Erhvervstillidsindikator, KBI=Tillidsindikator for industri, KBB=Tillidsindikator for bygge og anlæg, KBD=Tillidsindikator for detailhandel, KBS=Tillidsindikator for serviceerhverv]
- tid: date range 1998-01-01 to 2025-10-01

notes:
- Monthly series. Each indikator × tid yields exactly one row — no overcounting risk.
- TE (Erhvervstillidsindikator) is the composite business confidence indicator. The 4 sector indicators (KBI, KBB, KBD, KBS) are independent sector-level indices. Do NOT sum across all 5 — TE already represents the overall level and is not the sum of the others.
- KBS (serviceerhverv) starts 2000-04-01; all other indicators from 1998-01-01. Filter by date if comparing across all sectors.
- To get the overall business confidence over time: WHERE indikator = 'TE'
- To compare sector-level confidence at a point in time: filter to a single tid and exclude TE, or show all 5 explicitly labeled.