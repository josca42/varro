table: fact.kryds2
description: Personer med dansk oprindelse 1. januar efter Hovedpersons fødeland, forældres fødeland og statsborgerskab, hovedpersonens alder og tid
measure: indhold (unit Antal)
columns:
- hofod: values [0=I alt, 5100=Danmark, 5122=Albanien, 5124=Andorra, 5706=Belarus ... 5532=Østtimor, 5599=Øer i Stillehavet, 5103=Statsløs, 5999=Uoplyst, 9999=Uoplyst land]
- ffodstat: values [BB01=Begge født i Danmark og danske statsborgere, BB02=Begge født i Danmark og udenlandske statsborgere, BB03=Begge født i udlandet og danske statsborgere, BB04=Begge født i udlandet og udenlandske statsborgere, BB05=Begge forældre er ukendte, E01=En født i Danmark og dansk statsborger / En født i Danmark og udenlandsk statsborger, E02=En født i Danmark og dansk statsborger / En født i udlandet og dansk statsborger, E03=En født i Danmark og dansk statsborger / En født i udlandet og udenlandsk statsborger, E04=En født i Danmark og udenlandsk statsborger / En født i udlandet og dansk statsborger, E05=En født i Danmark og udenlandsk statsborger / En født i udlandet og udenlandsk statsborger, E06=En født i udlandet og dansk statsborger / En født i udlandet og udenlandsk statsborger, E07=En født i Danmark og dansk statsborger / En ukendt forælder, E08=En født i Danmark og udenlandsk statsborger / En ukendt forælder, E09=En født i udlandet og dansk statsborger / En ukendt forælder, E10=En født i udlandet og udenlandsk statsborger / En ukendt forælder]
- hoald: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- tid: date range 2019-01-01 to 2025-01-01

notes:
- This table is restricted to persons with dansk oprindelse only (kryds4 covers all herkomst groups with similar structure).
- hofod uses country codes matching dim.lande_psd (niveau=3). hofod=0 is the "I alt" total.
- ffodstat codes describe the combined birth country and citizenship of both parents (BB=begge/both, E=en/one). There are 15 codes. Filter to one specific parent-combination when querying; summing across all ffodstat values gives the total of persons with dansk oprindelse.
- hoald has individual years (0–125) with no total row. SUM across alder to get all-age counts.
- Use for: "how many persons with Danish origin have parents who both hold foreign citizenship?"