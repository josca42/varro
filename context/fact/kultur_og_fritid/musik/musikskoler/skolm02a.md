table: fact.skolm02a
description: Elevers aktiviteter på musikskoler efter kommune, fag, alder, køn og tid
measure: indhold (unit Antal)
columns:
- komk: join dim.kommunegrupper on komk=kode; levels [2]
- faget: values [TOT=Fag i alt, 855=Sang, 860=Strygeinstrument, 875=Træblæser, 880=Messingblæser, 885=Slagtøj, 890=Tasteinstrument, 920=Strengeinstrument, 900=Øvrige musikfag, 910=Øvrige kunstfag, 930=Sammenspil, 940=Forskole, 999=Uoplyst]
- alder: values [TOT=Alder i alt, 0003=0-3 år, 0406=4-6 år, 0709=7-9 år, 1014=10-14 år, 1519=15-19 år, 2024=20-24 år, 2500=25 år og derover, UOPLYST=Uoplyst alder]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, 9=Uoplyst køn]
- tid: date range 2021 to 2025
dim docs: /dim/kommunegrupper.md

notes:
- komk joins dim.kommunegrupper at niveau 2 (98 kommuner). komk='0' is the national total, not in the dim.
- This table counts aktiviteter (subject enrollments), not unique students. A student enrolled in 3 subjects counts 3 times. Use skolm02b for unique student headcounts.
- TOT rows present for faget, alder, and kon. Filter all three to avoid overcounting: use faget='TOT', alder='TOT', kon='TOT' for simple totals, or pick one dimension and filter the others to their TOT.
- Map: context/geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0.