table: fact.strfna13
description: Skyldige personer efter statsborgerskab, overtrædelsens art og tid
measure: indhold (unit Antal)
columns:
- statsb: values [DANSK=Dansk, VEST=Vestligt, IKKEVEST=Ikke-vestligt]
- overtraed: join dim.overtraedtype on overtraed=kode [approx]; levels [1, 3]
- tid: date range 2018-01-01 to 2023-01-01
dim docs: /dim/overtraedtype.md
notes:
- overtraed covers ONLY Straffelov — both niveau 1 and 3 appear as separate rows. Filter WHERE d.niveau=3 for subcategory breakdown or niveau=1 for the Straffelov total. Mixing double-counts.
- statsb has 3 values (DANSK, VEST, IKKEVEST) — no total row. Sum all 3 for total.
