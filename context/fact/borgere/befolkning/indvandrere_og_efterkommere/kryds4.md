table: fact.kryds4
description: Befolkningen 1. januar efter Hovedpersons herkomst, forældres fødeland og statsborgerskab, hovedpersonens alder og tid
measure: indhold (unit Antal)
columns:
- hoher: join dim.herkomst on hoher=kode [approx]
- ffodstat: values [BB01=Begge født i Danmark og danske statsborgere, BB02=Begge født i Danmark og udenlandske statsborgere, BB03=Begge født i udlandet og danske statsborgere, BB04=Begge født i udlandet og udenlandske statsborgere, BB05=Begge forældre er ukendte, E01=En født i Danmark og dansk statsborger / En født i Danmark og udenlandsk statsborger, E02=En født i Danmark og dansk statsborger / En født i udlandet og dansk statsborger, E03=En født i Danmark og dansk statsborger / En født i udlandet og udenlandsk statsborger, E04=En født i Danmark og udenlandsk statsborger / En født i udlandet og dansk statsborger, E05=En født i Danmark og udenlandsk statsborger / En født i udlandet og udenlandsk statsborger, E06=En født i udlandet og dansk statsborger / En født i udlandet og udenlandsk statsborger, E07=En født i Danmark og dansk statsborger / En ukendt forælder, E08=En født i Danmark og udenlandsk statsborger / En ukendt forælder, E09=En født i udlandet og dansk statsborger / En ukendt forælder, E10=En født i udlandet og udenlandsk statsborger / En ukendt forælder]
- hoald: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- tid: date range 2019-01-01 to 2025-01-01
dim docs: /dim/herkomst.md

notes:
- hoher does NOT join dim.herkomst (0% match). The fact table uses codes 24/25/34/35/999 (west/non-west split of indvandrere/efterkommere + 999 for uoplyst). dim.herkomst has codes 1/2/3/9. Treat hoher as inline: 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige, 34=Efterkommere fra vestlige, 35=Efterkommere fra ikke-vestlige, 999=Uoplyst/øvrige.
- No total row for hoher — SUM across hoher groups for all-herkomst counts.
- ffodstat codes describe combined parent birth country and citizenship (BB01-05=begge forældre, E01-10=én forældre). Same structure as kryds2. Sum across all ffodstat values to get totals.
- hoald has individual years (0–125) with no total row.
- Like kryds2 but covers indvandrere and efterkommere (west/non-west breakdown) instead of dansk oprindelse.