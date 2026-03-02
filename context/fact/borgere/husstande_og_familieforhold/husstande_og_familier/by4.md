table: fact.by4
description: Husstande 1. januar efter byområder og landdistrikter, husstandstype, antal børn og tid
measure: indhold (unit Antal)
columns:
- byer: values [1100=000-01100 Hovedstadsområdet, 10100101=101-00101 Københavns Kommune, 10101100=101-01100 København (del af Hovedstadsområdet), 10199999=101-99999 Landdistrikter, 14700147=147-00147 Frederiksberg Kommune ... 86018377=860-18377 Lørslev, 86018378=860-18378 Tårs, 86018403=860-18403 Rakkeby, 86099997=860-99997 Uden fast bopæl, 86099999=860-99999 Landdistrikter]
- hustyp: values [M=Enlige mænd, K=Enlige kvinder, PAR=Ægtepar, PA=Et par i øvrigt, AND=Andre husstande i øvrigt]
- antborn: values [2000=Ingen børn, 2010=Har børn]
- tid: date range 2010-01-01 to 2025-01-01

notes:
- byer is an inline coded column with 1829 unique byområde codes — no dim table join. The codes encode municipality + sub-area (e.g., 10101100 = "101-01100 København (del af Hovedstadsområdet)"). The only top-level aggregate is byer=1100 (Hovedstadsområdet); all other codes are specific byområder or landdistrikter.
- antborn has only 2 values: 2000=Ingen børn, 2010=Har børn. No total. To get all households regardless of children, SUM across both antborn values.
- hustyp has 5 values (AND=Andre husstande i øvrigt, not AH as in fam55n). No total — SUM to aggregate across all types.
- Use ColumnValues("by4", "byer") with fuzzy_match_str to find byer codes by place name, e.g. ColumnValues("by4", "byer", fuzzy_match_str="Aarhus").