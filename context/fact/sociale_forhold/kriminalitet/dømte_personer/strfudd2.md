table: fact.strfudd2
description: Skyldige personer i alderen 15-79 år efter overtrædelsens art, uddannelse og tid
measure: indhold (unit Antal)
columns:
- overtraed: join dim.overtraedtype on overtraed=kode [approx]; levels [1, 3]
- uddannelse: values [TOT=I alt, 10=Grundskole, 20=Gymnasial uddannelse, 35=Erhvervsuddannelse, 40=Videregående uddannelse, 00=Uoplyst uddannelse]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/overtraedtype.md
notes:
- overtraed covers ONLY Straffelov (penal code) — Færdselslov and Særlov are not in this table.
- Both niveau 1 (1 code: "Straffelov") and niveau 3 (~81 subcategories) appear as separate rows. Filter WHERE d.niveau=3 for subcategory breakdown, or niveau=1 for the single "Straffelov" total. Mixing both levels silently double-counts.
- 7 unmatched 8-digit codes exist in the fact table (not in dim.overtraedtype); excluded by the JOIN, affects a small minority of rows.
- uddannelse: TOT=I alt is aggregate; the 5 substantive categories sum to TOT.
