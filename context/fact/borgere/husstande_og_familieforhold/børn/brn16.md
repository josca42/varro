table: fact.brn16
description: Børn fordelt på alle søskende - antal og kombination efter område, alder, familietype, antal søskende, kombination af søskende og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år, 5=5 år, 6=6 år, 7=7 år, 8=8 år, 9=9 år, 10=10 år, 11=11 år, 12=12 år, 13=13 år, 14=14 år, 15=15 år, 16=16 år, 17=17 år]
- famtype: values [0=Udeboende, 1=Begge forældre, 2=Enlig mor, 3=Mor og partner, 4=Enlig far, 5=Far og partner]
- antsos: values [0=Ingen søskende, 1=1 søster eller bror, 2=2 søskende, 3=3 søskende, 4=4 søskende, 5=5 søskende, 6=6 søskende, 7=7+ søskende]
- kombsos: values [0=Enebarn, 1=Kun papsøskende, 10=Kun halvsøskende, 11=Halv- og papsøskende, 100=Kun helsøskende, 101=Hel- og papsøskende, 110=Hel- og halvsøskende, 111=Hel- halv- og papsøskende]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/nuts.md
notes:
- omrade has three groups: '0' (national total, not in dim.nuts — use omrade='0' directly), niveau 1 (5 regioner), niveau 3 (99 kommuner). Filter to one niveau when joining dim.nuts.
- kombsos uses same binary positional code as brn15: hundreds=helsøskende, tens=halvsøskende, ones=papsøskende. E.g. 100=only full siblings, 011=half- and step-siblings.
- This table counts ALL siblings regardless of cohabitation, unlike brn15 which only counts cohabiting siblings. For full sibship size, use this table; for household sibling composition, use brn15.
- famtype=0 means "Udeboende" (child not living with any family).
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
