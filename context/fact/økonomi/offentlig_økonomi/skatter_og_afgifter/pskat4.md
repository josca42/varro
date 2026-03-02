table: fact.pskat4
description: Slutskat efter område, indkomstskattetype og tid
measure: indhold (unit 1.000 kr.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- indkomst: values [1=Skattepligtige personer (antal), 2=Skattepligtig indkomst, 3=Arbejdsmarkedsbidrag, 4=Bundskat, 5=Topskat, 6=Udligningsskat, 7=Sundhedsbidrag, 8=Kommuneskat, 9=Kirkeskat, 10=Skat for begrænset skattepligt, 11=Virksomhedsskat, 12=Forskerskat, 13=Aktieindkomstskat, 14=Ejendomsværdiskat, 17=Grundskyld, 15=Slutskat i alt, 16=Gennemsnitlig slutskat pr. skattepligtig person (kr.)]
- tid: date range 2011-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- omrade only has niveau=3 (98 kommuner) — no regional aggregates in dim.nuts. omrade='0' is a national total (not in dim.nuts). Use ColumnValues("nuts","titel",for_table="pskat4") to see the 98 kommuner available.
- indkomst mixes units within the same column: indkomst=1 is antal persons (raw number), indkomst=2–15 are amounts in 1.000 kr., indkomst=16 is kr. per person (average). Always filter to exactly one indkomst value per query.
- indkomst=15 (Slutskat i alt) = sum of individual tax types 3–14 (not verified, but follows from the label). For total tax burden by kommune: WHERE indkomst='15'.
- For per-capita analysis: divide indkomst=15 by indkomst=1 (or use indkomst=16 directly for average slutskat per person).
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
