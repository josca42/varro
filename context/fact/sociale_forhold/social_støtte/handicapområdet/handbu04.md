table: fact.handbu04
description: Handicapindsatser til børn og unge mellem 0-17 år efter indsats, alder, køn og tid
measure: indhold (unit Antal)
columns:
- indsatser: values [100=Handicapindsatser i alt, 110=Børn og unge der modtager handicapindsatser i alt, 1=Særlige dagtilbud til børn (SEL § 32 / BL § 82.1), 3=Særlige klubtilbud til større børn og unge (SEL § 36 / BL § 82.2), 2=Hjemmetræning af børn (SEL § 32a / BL § 82.3), 8=Andre tilbud efter barnets lov eller  dagtilbudsloven (BL § 82.4) (2024-), 7=Ledsageordning til børn og unge mellem 12 og 18 år, som ikke kan færdes alene (SEL § 45 / BL § 89.1), 4=Personlig og praktisk hjælp (SEL §44/83 / BL § 90.1), 5=Afløsning eller aflastning af forældre eller andre nære pårørende (SEL 44/84.1 / BL § 90.2), 6=Vedligeholdelsestræning, herunder hjælp til at vedligeholde fysiske eller psykiske færdigheder (SEL §44/86.2 / BL § 90.3)]
- alder: values [IALT=Alder i alt, 0005=0-5 år, 0611=6-11 år, 1217=12-17 år, 999=Uoplyst alder]
- kon: values [0=I alt, D=Drenge, P=Piger, 9=Uoplyst køn]
- tid: date range 2022-01-01 to 2024-01-01
notes:
- No dim joins. Same indsatser logic as handbu03: types 1–8 are specific intervention types, 100=total interventions, 110=unique children. Pick one level — do not mix.
- alder has IALT — do not sum across all alder values. Filter to alder='IALT' for totals or SUM only individual bands.
- kon=0 is "I alt" — do not sum 0+D+P+9. Filter to kon=0 for totals or SUM D+P+9 (adding 9=uoplyst if desired).
- National data only; for breakdown by region use handbu01 (by kommune/kon) or handbu02 (by kommune/alder) or handbu03 (by landsdel).
