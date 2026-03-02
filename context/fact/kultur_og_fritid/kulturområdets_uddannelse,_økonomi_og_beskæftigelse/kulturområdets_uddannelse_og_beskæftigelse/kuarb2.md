table: fact.kuarb2
description: Ansatte på kulturarbejdspladser efter kulturemne, alder, herkomst og tid
measure: indhold (unit Antal)
columns:
- kulturemne: join dim.kulturemner on kulturemne::text=kode [approx: Fact int64 vs dim object KODE; top-level codes 1-6 match semantically]; levels [1]
- alder: values [-15=Under 16 år, 16-19=16-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-66=65-66 år, 67-=67 år og derover]
- herkams: values [0=I alt, 10=Personer med dansk oprindelse, 20=Indvandrere, 30=Efterkommere]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/kulturemner.md

notes:
- kulturemne: uses numeric codes that are a mix of niveau=1 codes (2–6 match dim directly) and numeric equivalents of K-prefix niveau=2 codes (9→K09, 10→K10, etc.). The join is unreliable for the full code set. Use inline ColumnValues for kulturemne labels rather than joining dim.kulturemner.
- alder has 13 age bands with no total row — summing all gives total employee count. No age aggregate column exists.
- herkams=0 is the total across all origin groups; filter when drilling down.