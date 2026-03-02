table: fact.skolm03
description: MGK-elever på musikskoler efter MGK-centre, alder og køn og tid
measure: indhold (unit Antal)
columns:
- mgk: values [MTOT=MGK-centre i alt, 2150=MGK Hovedstaden, 2155=MGK Sankt Annæ Gymnasium, 2157=MGK Sjælland, 2160=MGK Fyn, 2165=MGK Nordjylland, 2170=MGK Midt- og Vestjylland, 2175=MGK Østjylland, 2180=MGK Sydjylland]
- alderk: values [KTOT=Køn og alder i alt, 2100=18 år og derunder, 2105=19-21 år, 2110=22 år og derover, 2115=Mænd, 2120=Kvinder]
- tid: date range 2021 to 2025

notes:
- MGK = Musikalsk Grundkursus, the pre-conservatory talent track. Only 8 centres in Denmark.
- alderk mixes age groups and gender in a single column. KTOT=total, 2100/2105/2110=age groups, 2115/2120=gender. Do not sum across all alderk values — age groups and gender groups overlap. Filter to either KTOT, one age group, or one gender group at a time.
- mgk='MTOT' is the national total across all centres. No dim join needed for this table.