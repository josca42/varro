table: fact.gasrg
description: Fysisk balance for naturgasreserverne efter balanceposter og tid
measure: indhold (unit Mia. Nm3)
columns:
- balpost: values [1=Primobeholdning (1), 11=Primobeholdning - heraf igangværende og besluttet indvinding, 12=Primobeholdning  - heraf planlagt indvinding, 13=Primobeholdning - heraf mulig indvinding, 20=Indvinding, 201=Indvinding - heraf reinjiceret, 22=Nettoproduktion (2), 221=Nettoproduktion - heraf afbrændt, 222=Nettoproduktion  - heraf eget forbrug, 223=Nettoproduktion - heraf solgt, 3=Nye fund og anden økonomisk opståen (+)/forsvinden (-) (3), 4=Ultimoheholdning (4)=(1)-(2)+(3), 41=Ultimobeholdning - heraf igangværende og besluttet indvinding, 42=Ultimobeholdning - heraf planlagt udvinding, 43=Ultimobeholdning - heraf mulig indvinding]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- balpost has a multi-level hierarchy: 11/12/13 are sub-items of 1; 201 is a sub-item of 20 (total extraction); 221/222/223 are sub-items of 22 (nettoproduktion). Never mix parent and child codes in a sum.
- Accounting identity: 4 = 1 - 22 + 3 (ultimo = primo - net production + new finds). Note: balpost=20 is gross extraction, 22 is net after reinjection. Use 22 for balance calculations.
- For extraction analysis: use balpost='22' (nettoproduktion) or drill into 221/222/223 for breakdown by end-use (flared/own use/sold).
- More granular than olierg due to the extra extraction breakdown (20/22/201/221/222/223). Still comparable period: 1990–2024.