table: fact.kmsta001
description: Befolkningen 1. januar efter sogn, herkomst, folkekirkemedlemsskab og tid
measure: indhold (unit Antal)
columns:
- sogn: values [7001=7001 Vor Frue (Københavns Kommune), 7002=7002 Helligånds (Københavns Kommune), 7003=7003 Trinitatis (Københavns Kommune), 7004=7004 Sankt Andreas (Københavns Kommune), 7007=7007 Sankt Johannes (Københavns Kommune) ... 9357=9357 Torkilstrup-Lillebrænde Sogn (Guldborgsund Kommune), 9358=9358 Gråsten-Adsbøl Sogn (Sønderborg Kommune), 9359=9359 Søndbjerg-Odby Sogn (Struer Kommune), 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- herkomst: join dim.herkomst on herkomst=kode [approx]; levels [1]
- fkmed: values [F=Medlem af Folkekirken, U=Ikke medlem af Folkekirken]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/herkomst.md

notes:
- herkomst uses a 5-category scheme that does NOT match dim.herkomst (which has 4 codes: 1,2,3,9). Do NOT join to dim.herkomst — use ColumnValues("kmsta001", "herkomst") for labels instead.
- The 5 herkomst codes: 1=Personer med dansk oprindelse, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande. The coding combines origin type (1=dansk, 2=indvandrer, 3=efterkommer) with region (4=vestlig, 5=ikke-vestlig).
- These 5 codes are exhaustive (no IALT total) — sum all 5 for total population of a sogns.
- fkmed: F=Medlem, U=Ikke-Medlem. Both present for each combination.
- 2292 distinct sogns including 0='Uden placerbar adresse' and 9999='Uden fast bopæl'. Exclude for geographic analysis.
- Map: context/geo/sogne.parquet — merge on sogns=dim_kode. Exclude sogns IN (0, 9999).
