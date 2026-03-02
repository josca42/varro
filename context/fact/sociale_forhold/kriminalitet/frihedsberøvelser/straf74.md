table: fact.straf74
description: Anholdelser efter overtrædelsens art, uddannelse og tid
measure: indhold (unit Antal)
columns:
- overtraed: join dim.overtraedtype on overtraed=kode::text [approx: OVERTRÆD is object type with AVA suffixes while overtraedtype.KODE is int64. Values like 111AVA need AVA stripped.]; levels [1, 2, 3]
- uddannelse: values [TOT=I alt, 10=Grundskole, 20=Gymnasial uddannelse, 35=Erhvervsuddannelse, 40=Videregående uddannelse, 00=Uoplyst uddannelse]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/overtraedtype.md

notes:
- overtraed joins dim.overtraedtype the same way as straf70/72: `f.overtraed::text = d.kode::text`, niveau 1–3 are all present. Always filter `WHERE d.niveau = X`. Unmatched aggregate/range codes drop out on the join.
- uddannelse: TOT=I alt, 10=Grundskole, 20=Gymnasial, 35=Erhvervsuddannelse, 40=Videregående, 00=Uoplyst. Filter uddannelse='TOT' for offense-only totals; 00 is substantive (unknown education), not a total.
- No demographic breakdown (kon/alder) — use straf70 for that.
- Sample query — arrests for property crimes by education level:
  SELECT d.titel, f.uddannelse, SUM(f.indhold)
  FROM fact.straf74 f
  JOIN dim.overtraedtype d ON f.overtraed::text = d.kode::text AND d.niveau = 2
  WHERE f.uddannelse != 'TOT'
  GROUP BY d.titel, f.uddannelse;