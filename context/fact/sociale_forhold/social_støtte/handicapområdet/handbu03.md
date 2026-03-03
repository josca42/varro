table: fact.handbu03
description: Handicapindsatser til børn og unge mellem 0-17 år efter landsdel, indsats og tid
measure: indhold (unit Antal)
columns:
- landsdel: join dim.nuts on landsdel=kode; levels [2]
- indsatser: values [100=Handicapindsatser i alt, 110=Børn og unge der modtager handicapindsatser i alt, 1=Særlige dagtilbud til børn (SEL § 32 / BL § 82.1), 3=Særlige klubtilbud til større børn og unge (SEL § 36 / BL § 82.2), 2=Hjemmetræning af børn (SEL § 32a / BL § 82.3), 8=Andre tilbud efter barnets lov eller  dagtilbudsloven (BL § 82.4) (2024-), 7=Ledsageordning til børn og unge mellem 12 og 18 år, som ikke kan færdes alene (SEL § 45 / BL § 89.1), 4=Personlig og praktisk hjælp (SEL §44/83 / BL § 90.1), 5=Afløsning eller aflastning af forældre eller andre nære pårørende (SEL 44/84.1 / BL § 90.2), 6=Vedligeholdelsestræning, herunder hjælp til at vedligeholde fysiske eller psykiske færdigheder (SEL §44/86.2 / BL § 90.3)]
- tid: date range 2022-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- landsdel joins dim.nuts at niveau=2 (11 landsdele). landsdel=0 is a national total not in dim.nuts — use it for Denmark-wide figures.
- indsatser has 10 values: types 1–8 (specific indsatstyper) plus 100=Handicapindsatser i alt and 110=unique children receiving them. Sum of types 1–8 ≈ 100 (not exact due to rounding/other). Never mix 100/110 with individual types in a SUM — pick one level.
- Use 110 for "how many children", 100 for "how many interventions", types 1–8 for breakdowns by intervention type. A child can receive multiple types, so summing types 1–8 will exceed 110.
- Map: /geo/landsdele.parquet — merge on landsdel=dim_kode. Exclude landsdel=0.
