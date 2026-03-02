table: fact.skib96
description: Søulykker i dansk farvand efter uheldstype, skibstype, omfang, registreringsland og tid
measure: indhold (unit Antal)
columns:
- utype: values [0=SØULYKKER I ALT, 3000=Kæntring/slagside, 3010=Kollision, 3011=Brand eller eksplosion, 3012=Skrogskade, 3015=Kontakt, 3020=Skade på skib eller udstyr, 3025=Vandindtrængen (inkl. forlis), 3030=Grundstødning/stranding, 3035=Kontrolsvigt, 3040=Hændelse uden ulykke, 3090=Uoplyst]
- skibtype: values [41110=Fragtskib, 41120=Passagerskib, 41130=Fiskefartøj, 41140=Serviceskib, 41150=Fartøj til indre vandveje, 41190=Ukendt]
- omfang: values [10=Mindre hændelse, 15=Mindre alvorlig, 20=Alvorlig, 25=Meget alvorlig]
- reg: values [1142=Danmark, 1145=Grønland, 1148=Udlandet]
- tid: date range 2014-01-01 to 2024-01-01

notes:
- Covers accidents **in Danish waters** regardless of ship nationality (contrast with skib95 which covers Danish-registered ships anywhere in the world).
- utype, skibtype, and omfang behave identically to skib95: utype=0 is the aggregate total; omfang and skibtype have no aggregate row and must be summed over.
- reg (registreringsland) has 3 mutually exclusive values: 1142=Danmark, 1145=Grønland, 1148=Udlandet. There is no total/aggregate reg value — sum over all reg to get totals across all registration countries.
- To get all accidents in Danish waters for a given year: filter utype=0, then sum over all reg, skibtype, and omfang. To break down by ship origin: group by reg (excluding aggregate utype/skibtype/omfang).
- reg=1148 (Udlandet) often dominates for larger vessel types like fragtskibe, reflecting international shipping in Danish waters.