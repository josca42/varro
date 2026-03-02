table: fact.deta212
description: Detailomsætningsindeks efter varegruppe, indekstype og tid
measure: indhold (unit Indeks)
columns:
- varegr: values [TOT=Detailhandel i alt, FØDE=Fødevarer og andre dagligvarer, BEKLÆD=Beklædning mv., ANDRE=Andre forbrugsvarer]
- indekstype: values [VAERDI=Værdiindeks, SVAERDI=Sæsonkorrigeret værdiindeks, MAENGDE=Mængdeindeks, SMAENGDE=Sæsonkorrigeret mængdeindeks]
- tid: date range 2000-01-01 to 2025-09-01

notes:
- `indekstype` is a measurement selector: every varegr × indekstype combination exists (4 × 4 = 16 series). Always filter to one indekstype — failing to do so inflates values 4×. Example: `WHERE indekstype = 'MAENGDE'` for the volume index.
- The four index types are: VAERDI (nominal value), SVAERDI (seasonally adjusted value), MAENGDE (volume/real), SMAENGDE (seasonally adjusted volume). Pick the one appropriate to the question — for inflation-adjusted trend analysis use MAENGDE or SMAENGDE.
- `varegr` categories are mutually exclusive groups that sum to TOT: FØDE + BEKLÆD + ANDRE ≈ TOT. Do not sum TOT with the sub-categories.
- No dim table link — all columns are inline coded. No join needed.