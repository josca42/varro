table: fact.und1
description: Underretninger vedr. børn efter administrationskommune, underrettere, alder, køn og tid
measure: indhold (unit Antal)
columns:
- admkom: join dim.nuts on admkom=kode [approx]; levels [3]
- underretere: values [0=I alt, 1=Mellemkommunal underretning eller anden kommunal forvaltning, 2=Skole eller andet uddannelsessted, 3=Dagpleje, daginstitution, fritidshjem, ungdomsklub eller SFO, 4=Sundhedsvæsenet, 5=Sundhedsplejerske eller tandlæge, 6=Politi eller domstol, 7=Familie, barn selv eller bekendtskabskreds (-2023), 8=Anonym, 9=Anbringelsessted, 10=Foreninger, frivillige organisationer, krise-, misbrugs- og asylcentre, 12=Barnet eller den unge selv (2024-), 13=Familie eller bekendtskabskreds (2024-), 11=Andre, 99=Uoplyst]
- alder1: values [00=I alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 16=16 år, 17=17 år, 18=18 år, U0=Ufødt, 999=Uoplyst alder]
- kon: values [0=I alt, D=Drenge, P=Piger, 9=Uoplyst køn, U=Uoplyst køn, ufødt]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Counts NOTIFICATIONS (underretninger), not children. One child can receive multiple notifications. For children-by-notification-count use und2 instead.
- admkom joins dim.nuts at niveau 3 (kommuner). Code 0 = national total, code 998 = unknown municipality.
- alder1 uses single years 0-18 plus '00'=I alt, 'U0'=ufødt, '999'=uoplyst. Note the total is '00' (two-digit string) not 0.
- underretere: code 0 = I alt. Note that codes 7 (Familie/barn/bekendtskab) split into 12 (barnet selv) and 13 (familie/bekendtskab) from 2024 — break in series for those categories.
- kon has an extra value U=Uoplyst køn (ufødt) for unborn children (alder1='U0').
- For total notifications by kommune: WHERE underretere='0' AND alder1='00' AND kon='0'.
- Map: context/geo/kommuner.parquet — merge on admkom=dim_kode. Exclude admkom=0 and admkom=998.