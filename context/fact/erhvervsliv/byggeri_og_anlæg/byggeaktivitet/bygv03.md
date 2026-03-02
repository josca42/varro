table: fact.bygv03
description: Landstal for boliger i det samlede boligbyggeri (ikke korrigeret for forsinkelser) efter byggefase, anvendelse, bygherreforhold og tid
measure: indhold (unit Antal)
columns:
- bygfase: values [2=Påbegyndt byggeri, 3=Fuldført byggeri, 4=Byggeri under opførelse, 1=Tilladt byggeri]
- anvend: join dim.byganv on anvend=kode::text [approx]; levels [2, 3]
- bygherre: values [10+30+40+90=Private, I/S, A/S, ApS og lign., 20=Almene boligselskaber, 41=Private andelsboligforeninger, SK=Offentlig myndighed, UOPL=Uoplyst]
- tid: date range 1981-01-01 to 2024-01-01
dim docs: /dim/byganv.md
notes:
- National totals only — no regional breakdown. Goes back to 1981 (longer series than bygv33 which starts 2006). For regional data use bygv33.
- anvend joins dim.byganv at niveauer 2 and 3. Codes '009' (boligbyggeri i alt) and 'UOPL' are not in the dim — '009' is an aggregate for all residential types; exclude when summing subtypes.
- bygherre uses combined and custom codes that do NOT join to dim.bygherre: '10+30+40+90' (combined private), '20' (almene boligselskaber), '41' (private andelsboligforeninger), 'SK' (stat og kommuner), 'UOPL'. Use inline values, not dim join.
- bygfase has 4 mutually exclusive phases — always filter to one when aggregating.
