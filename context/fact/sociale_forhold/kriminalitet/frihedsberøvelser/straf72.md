table: fact.straf72
description: Anholdelser efter bopæl i Danmark, overtrædelsens art og tid
measure: indhold (unit Antal)
columns:
- bopdk: values [0=I alt, 90=Personer med bopæl i Danmark, 91=Personer uden bopæl i Danmark]
- overtraed: join dim.overtraedtype on overtraed=kode::text [approx: OVERTRÆD is object type while overtraedtype.KODE is int64. Values appear numeric but stored as strings.]; levels [1, 2, 3]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/overtraedtype.md

notes:
- overtraed joins dim.overtraedtype the same way as straf70: `f.overtraed::text = d.kode::text`, niveau 1–3 are all present in the fact table. Always filter `WHERE d.niveau = X`. The 29% unmatched codes are aggregate/range codes (see straf70 notes for full breakdown) — they drop out automatically when joining the dim.
- bopdk: 0=I alt (total), 90=bopæl i Danmark, 91=uden bopæl i Danmark. Filter bopdk='0' for overall totals or choose 90/91 for the split. Only two substantive values.
- No demographic breakdown (kon/alder) — use straf70 for that cross-tabulation.
- Sample query — arrests by offense type and residency:
  SELECT d.titel, f.bopdk, SUM(f.indhold)
  FROM fact.straf72 f
  JOIN dim.overtraedtype d ON f.overtraed::text = d.kode::text AND d.niveau = 2
  WHERE f.bopdk IN ('90', '91')
  GROUP BY d.titel, f.bopdk;