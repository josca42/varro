table: fact.anbaar16
description: Anbragte børn og unge pr. 31. december efter landsdel, anbringelsessted, foranstaltning, alder, køn og tid
measure: indhold (unit Antal)
columns:
- landdel: join dim.nuts on landdel=kode [approx]; levels [2]
- anbringelse: values [0=I alt, 1=Netværksplejefamilie, 21=Almindelig plejefamlie, 22=Kommunal plejefamilie, 26=Plejefamilie efter §76 a (unge med funktionsnedsættelse), 23=Almen plejefamilie, 24=Forstærket plejefamilie, 25=Specialiseret plejefamlie, 9=Døgninstitution, almindelig afdeling, 7=Delvis lukket døgninstitution eller delvis lukket afdeling på åben døgninstitution, 8=Døgninstitution, sikret afdeling, 27=Opholdssted for børn og unge, 11=Kost- og eller efterskole, 6=Eget værelse, kollegium, kollegielignende opholdssted, 99=Uoplyst]
- foran: values [0=I alt, 101=Afgørelse med samtykke , 102=Afgørelse uden samtykke , 103=Foreløbig afgørelse, 104=Dom (idømt foranstaltning), 105=Dom (afsoning), 106=Surrogat for varetægtsfængsling, 107=Udlændinge under 15 år (udlændingelovens §36 og 37 / BL § 62, stk. 2, 4), 108=Ankestyrelsens afgørelse, 109=Afgørelse med samtykke, ungdomskriminalitet, 110=Afgørelse uden samtykke, ungdomskriminalitet, 111=Foreløbig afgørelse, ungdomskriminalitet, 112=Afgørelse uden samtykke, udlænding  (udlændingeloven § 62.1 / BL § 62, stk. 2,5), 113=Foreløbig afgørelse, udlænding, 114=Afgørelse med samtykke, ufødt barn (2024-), 115=Afgørelse uden samtykke, ufødt barn (2024-), 99=Uoplyst]
- alder1: values [IALT=Alder i alt, 0005=0-5 år, 0611=6-11 år, 1217=12-17 år, 1800=18 år og derover, 999=Uoplyst alder]
- kon: values [0=I alt, D=Drenge, P=Piger, 9=Uoplyst køn]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Most granular placed-children stock table: landsdel × anbringelsessted × foran × alder1 × kon. Must filter all five dimensions to avoid overcounting.
- landdel joins dim.nuts at niveau 2 (11 landsdele, koder 1-11). Code 0 = national total (not in dim). Code 12 = unknown/abroad (~43 rows, very small counts, safe to exclude for national analyses).
- alder1 here uses age GROUPS (IALT, 0005, 0611, 1217, 1800, 999) — unlike anbaar2/anbaar15 which use single years. Filter to IALT for age totals.
- kon: total is code 0 (not 'TOT'). Drenge=D, Piger=P.
- foran and anbringelse both have code 0 = I alt. To get total placed children by landsdel: WHERE foran=0 AND anbringelse=0 AND alder1='IALT' AND kon='0'.
- ColumnValues("nuts", "titel", for_table="anbaar16") returns the 11 landsdele.
- Map: context/geo/landsdele.parquet — merge on landdel=dim_kode. Exclude landdel=0.