table: fact.anbaar2
description: Anbragte børn og unge pr. 31. december efter foranstaltning, alder, køn og tid
measure: indhold (unit Antal)
columns:
- foran: values [0=I alt, 101=Afgørelse med samtykke , 102=Afgørelse uden samtykke , 103=Foreløbig afgørelse, 104=Dom (idømt foranstaltning), 105=Dom (afsoning), 106=Surrogat for varetægtsfængsling, 107=Udlændinge under 15 år (udlændingelovens §36 og 37 / BL § 62, stk. 2, 4), 108=Ankestyrelsens afgørelse, 109=Afgørelse med samtykke, ungdomskriminalitet, 110=Afgørelse uden samtykke, ungdomskriminalitet, 111=Foreløbig afgørelse, ungdomskriminalitet, 112=Afgørelse uden samtykke, udlænding  (udlændingeloven § 62.1 / BL § 62, stk. 2,5), 113=Foreløbig afgørelse, udlænding, 114=Afgørelse med samtykke, ufødt barn (2024-), 115=Afgørelse uden samtykke, ufødt barn (2024-), 99=Uoplyst]
- alder1: values [0=I alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 19=19 år, 20=20 år, 21=21 år, 22=22 år, 999=Uoplyst alder]
- kon: values [0=I alt, D=Drenge, P=Piger, 9=Uoplyst køn]
- tid: date range 2011-01-01 to 2024-01-01

notes:
- alder1 contains BOTH individual ages (0, 1, 2 … 22) AND the total (also code 0=I alt). This creates an ambiguity: the doc shows "0=I alt" and "0=0 år" — in practice the total uses code 0 and individual age 0 is also 0. Filter WHERE alder1='0' for total, but be aware that this returns the aggregate row, not infants. To get infants aged 0, there is no clean way — use the age-group tables (anbaar16) instead.
- foran: code 0 = I alt, codes 101-115 are specific legal bases, 99=uoplyst. Filter to foran=0 for totals.
- kon: total is code 0 (not 'TOT'). Drenge=D, Piger=P.
- No geographic breakdown — national totals only. For regional breakdown use anbaar16 (landsdele) or anbaar12/13 (kommuner).