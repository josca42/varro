table: fact.skib95
description: Søulykker med danske skibe efter uheldstype, skibstype, omfang og tid
measure: indhold (unit Antal)
columns:
- utype: values [0=SØULYKKER I ALT, 3000=Kæntring/slagside, 3010=Kollision, 3011=Brand eller eksplosion, 3012=Skrogskade, 3015=Kontakt, 3020=Skade på skib eller udstyr, 3025=Vandindtrængen (inkl. forlis), 3030=Grundstødning/stranding, 3035=Kontrolsvigt, 3040=Hændelse uden ulykke, 3090=Uoplyst]
- skibtype: values [41110=Fragtskib, 41120=Passagerskib, 41130=Fiskefartøj, 41140=Serviceskib, 41150=Fartøj til indre vandveje, 41190=Ukendt]
- omfang: values [10=Mindre hændelse, 15=Mindre alvorlig, 20=Alvorlig, 25=Meget alvorlig]
- tid: date range 2014-01-01 to 2024-01-01

notes:
- Covers accidents involving **Danish-registered ships** regardless of where they occurred (contrast with skib96 which covers all ships in Danish waters).
- utype=0 (SØULYKKER I ALT) is the aggregate of all accident types. The other 10 utype values are mutually exclusive accident categories; they sum to utype=0.
- omfang (severity) is a mutually exclusive cross-cutting dimension: 10=Mindre hændelse, 15=Mindre alvorlig, 20=Alvorlig, 25=Meget alvorlig. There is no aggregate/total omfang value — sum over all omfang values to get the total count for a utype+skibtype combination.
- skibtype has no aggregate total row — all 6 values are leaf categories (Fragtskib, Passagerskib, Fiskefartøj, Serviceskib, Fartøj til indre vandveje, Ukendt). Sum over all skibtype to get totals.
- To count total maritime accidents in a year: filter utype=0 and sum over all omfang and all skibtype. Or use utype=0 with a specific skibtype+omfang combination for a targeted breakdown.