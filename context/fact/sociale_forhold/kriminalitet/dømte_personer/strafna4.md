table: fact.strafna4
description: Skyldige personer efter overtrædelsens art, oprindelsesland og tid
measure: indhold (unit Antal)
columns:
- overtraed: join dim.overtraedtype on overtraed=kode [approx]; levels [1, 3]
- ieland: values [0=I alt, 5100=Danmark, 5126=Belgien, 5754=Bosnien-Hercegovina, 5128=Bulgarien ... 5468=Vietnam, 5502=Australien, 7100=Øvrige lande i alt, 7200=Øvrige lande, vestlige, 7300=Øvrige lande, ikke-vestlige]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/overtraedtype.md
notes:
- overtraed covers ONLY Straffelov (penal code) — Færdselslov and Særlov are not in this table.
- Both niveau 1 (1 code: "Straffelov") and niveau 3 (~85 subcategories) appear as separate rows. Filter WHERE d.niveau=3 for subcategories or niveau=1 for the Straffelov total. Mixing both double-counts.
- 7 unmatched 8-digit codes not in dim.overtraedtype are excluded by the JOIN.
- ieland: 0=I alt (total), individual country codes (e.g. 5100=Danmark), plus sub-aggregate codes 7100=Øvrige lande i alt, 7200=Øvrige lande vestlige, 7300=Øvrige lande ikke-vestlige — all coexist at the same level. Pick one consistent level. Use ColumnValues("strafna4", "ieland") to browse.
