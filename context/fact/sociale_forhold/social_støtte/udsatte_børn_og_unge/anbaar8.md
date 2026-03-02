table: fact.anbaar8
description: Iværksatte anbringelser af børn og unge efter landsdel, foranstaltning, alder, køn og tid
measure: indhold (unit Antal)
columns:
- landdel: join dim.nuts on landdel=kode [approx]; levels [2]
- foran: values [0=I alt, 101=Afgørelse med samtykke , 102=Afgørelse uden samtykke , 103=Foreløbig afgørelse, 104=Dom (idømt foranstaltning), 105=Dom (afsoning), 106=Surrogat for varetægtsfængsling, 107=Udlændinge under 15 år (udlændingelovens §36 og 37 / BL § 62, stk. 2, 4), 108=Ankestyrelsens afgørelse, 109=Afgørelse med samtykke, ungdomskriminalitet, 110=Afgørelse uden samtykke, ungdomskriminalitet, 111=Foreløbig afgørelse, ungdomskriminalitet, 112=Afgørelse uden samtykke, udlænding  (udlændingeloven § 62.1 / BL § 62, stk. 2,5), 113=Foreløbig afgørelse, udlænding, 114=Afgørelse med samtykke, ufødt barn (2024-), 115=Afgørelse uden samtykke, ufødt barn (2024-), 99=Uoplyst]
- alder1: values [IALT=Alder i alt, 0005=0-5 år, 0611=6-11 år, 1217=12-17 år, 1800=18 år og derover, 999=Uoplyst alder]
- kon: values [0=I alt, D=Drenge, P=Piger, 9=Uoplyst køn]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- FLOW table (iværksatte = newly initiated placements in the year), not a stock. Compare to anbaar16 which is the stock (pr. 31. december).
- landdel joins dim.nuts at niveau 2 (11 landsdele, codes 1-11). Code 0 = national total.
- foran: same full legal basis list as anbaar2/anbaar16 (code 0=I alt). alder1 uses age groups (IALT, 0005, 0611, 1217, 1800). kon: 0=I alt, D/P.
- For total new placements by landsdel: WHERE foran='0' AND alder1='IALT' AND kon='0'.
- Map: context/geo/landsdele.parquet — merge on landdel=dim_kode. Exclude landdel=0.