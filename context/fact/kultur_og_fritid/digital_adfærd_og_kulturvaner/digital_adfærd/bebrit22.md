table: fact.bebrit22
description: Køb af it-udstyr - procent af befolkningen (16-74 år) efter type, overvejelse ved køb og tid
measure: indhold (unit Pct.)
columns:
- type: values [10=I alt, 40=Alder: 16-19 år, 50=Alder: 20-39 år, 60=Alder: 40-59 år, 70=Alder: 60-74 år ... 210=Indkomst: 0-49.999 kr., 220=Indkomst: 50.000-99.999 kr., 230=Indkomst: 100.000-199.999 kr., 240=Indkomst: 200.000-299.999 kr., 250=Indkomst: 300.000 og derover]
- overv: values [4090=Prisen, 4100=Mærke, design eller størrelse, 4110=Udstyrets harddrive, 4120=Ecodesign eller miljøvenligt design, 4130=Mulighed for at øge produktets levetid ved at tilkøbe ekstra garantier, 4140=Produktets energiforbrug, 4150=Fabrikant eller sælger af produktet tilbyder returnering, 4160=Har ikke overvejet noget af ovenstående, 4170=Har ikke købt udstyr, 4180=Ved ikke]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- type is a demographic selector: type='10' = national total. Never sum across type values.
- overv (purchase considerations) values are NOT mutually exclusive — respondents tick all factors considered when buying IT equipment. Never sum across overv values.
- overv='4160' means "Has not considered any of the above"; overv='4170' means "Has not bought equipment". These are informational exclusions, not a total.
- 2024 data only (single time point).
