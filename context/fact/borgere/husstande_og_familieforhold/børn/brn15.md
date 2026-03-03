table: fact.brn15
description: Børn fordelt på søskende de bor sammen med - antal og kombination efter område, alder, familietype, antal søskende, kombination af søskende og tid
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
- kombsos uses a binary positional code: hundreds digit = helsøskende present (1/0), tens digit = halvsøskende present (1/0), ones digit = papsøskende present (1/0). E.g. 100=only full siblings, 011=half- and step-siblings, 111=all three types.
- This table counts only siblings the child lives together with ("bor sammen med"). Compare with brn16 which counts ALL siblings regardless of cohabitation.
- antsos and kombsos are independent dimensions — filter both to get a specific sibling situation.
- famtype=0 means "Udeboende" (child not living with any family).
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
