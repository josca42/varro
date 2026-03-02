table: fact.byg91
description: Omkostningsindeks for dagrenovation, slamsugning og lastvognskørsel efter indekstype, enhed og tid
measure: indhold (unit Indeks)
columns:
- indekstype: values [DAG=Dagrenovation, DAGUB=Dagrenovation ekskl. brændstof (2022K2 - ), SLAM=Slamsugning, SLAMUB=Slamsugning ekskl. brændstof (2022K2 - ), LAST=Lastvognskørsel, LASTUV=Lastvognskørsel ekskl. vejafgift (2025K1 - ), LASTUB=Lastvognskørsel ekskl. brændstof (2022K2 - ), LASTUBV=Lastvognskørsel ekskl. brændstof og vejafgift (2025K1 - )]
- tal: values [100=Indeks, 210=Ændring i forhold til kvartalet før (pct.), 310=Ændring i forhold til samme kvartal året før (pct.)]
- tid: date range 1997-01-01 to 2025-04-01

notes:
- `tal` is a measurement selector — always filter it. `100`=index level, `210`=quarter-on-quarter change (%), `310`=year-on-year change (%). Omitting this filter mixes index values with percentage changes in the same result.
- `indekstype` has uneven time coverage: DAG and SLAM go back to 1997K1; LAST only from 2021K2; the "UB" variants (ekskl. brændstof) from 2022K2; LASTUV and LASTUBV only have 2 quarters (2025K1–2025K2).
- Naming pattern: suffix `UB` = ekskl. brændstof (excluding fuel), `UV` = ekskl. vejafgift (excluding road tax), `UBV` = both excluded. Use this to navigate the 8 indekstype codes.
- Sample query — index level for the three main series, most recent 8 quarters:
  ```sql
  SELECT tid, indekstype, indhold
  FROM fact.byg91
  WHERE tal = '100' AND indekstype IN ('DAG', 'SLAM', 'LAST')
  ORDER BY tid DESC, indekstype;
  ```