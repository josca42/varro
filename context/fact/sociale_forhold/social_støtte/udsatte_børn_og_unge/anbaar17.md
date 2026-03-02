table: fact.anbaar17
description: Iværksatte anbringelser af børn og unge efter landsdel, anbringelsessted, alder, køn og tid
measure: indhold (unit Antal)
columns:
- landdel: join dim.nuts on landdel=kode [approx]; levels [2]
- anbringelse: values [0=I alt, 1=Netværksplejefamilie, 21=Almindelig plejefamlie, 22=Kommunal plejefamilie, 26=Plejefamilie efter §76 a (unge med funktionsnedsættelse), 23=Almen plejefamilie, 24=Forstærket plejefamilie, 25=Specialiseret plejefamlie, 9=Døgninstitution, almindelig afdeling, 7=Delvis lukket døgninstitution eller delvis lukket afdeling på åben døgninstitution, 8=Døgninstitution, sikret afdeling, 27=Opholdssted for børn og unge, 11=Kost- og eller efterskole, 6=Eget værelse, kollegium, kollegielignende opholdssted, 99=Uoplyst]
- alder1: values [IALT=Alder i alt, 0005=0-5 år, 0611=6-11 år, 1217=12-17 år, 1800=18 år og derover, 999=Uoplyst alder]
- kon: values [0=I alt, D=Drenge, P=Piger, 9=Uoplyst køn]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- FLOW table (iværksatte = newly initiated placements), like anbaar8 but broken down by anbringelsessted instead of legal basis.
- landdel joins dim.nuts at niveau 2 (11 landsdele). Code 0 = national total.
- anbringelse code 0 = I alt. alder1 uses age groups. kon: 0=I alt, D/P.
- For total new placements by landsdel and placement type: WHERE alder1='IALT' AND kon='0'.
- Map: context/geo/landsdele.parquet — merge on landdel=dim_kode. Exclude landdel=0.