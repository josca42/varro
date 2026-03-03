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
- herkomst does NOT join dim.herkomst. The fact table uses codes 1/24/25/34/35 (west/non-west split, like folk1e), but dim.herkomst has codes 1/2/3/9 (Dansk/Indvandrere/Efterkommere/Uoplyst). The [approx] flag and 20% match rate confirm this. Treat herkomst as inline: 1=dansk oprindelse, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande.
- No total row for herkomst — SUM across herkomst groups for all-herkomst counts. No total for fkmed (F/U only).
- søgn codes include 0 ("Uden placerbar adresse") and 9999 ("Uden fast bopæl") as special categories, not geographic units.
- This is the only table in the subject with parish-level (søgn) geography — use for very fine-grained geographic analysis of church membership by herkomst.
- Map: /geo/sogne.parquet — merge on sogn=dim_kode. Exclude sogn IN (0, 9999).