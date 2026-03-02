table: fact.strfna10
description: Skyldige personer efter overtrædelsens art, herkomst og tid
measure: indhold (unit Antal)
columns:
- overtraed: join dim.overtraedtype on overtraed=kode [approx]; levels [1, 3]
- herkomst: values [TOT=I alt, 1=Personer med dansk oprindelse, 21=Indvandrere i alt, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 31=Efterkommere i alt, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/overtraedtype.md
notes:
- overtraed covers ONLY Straffelov — both niveau 1 and 3 appear as separate rows. Filter WHERE d.niveau=3 for subcategory breakdown or niveau=1 for the Straffelov total. Mixing double-counts.
- herkomst is hierarchical: 21=Indvandrere i alt (sum of 24+25), 31=Efterkommere i alt (sum of 34+35). TOT=1+21+31. Pick one consistent level — {1,21,31} or {1,24,25,34,35} — not both.
