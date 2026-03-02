table: fact.boern5
description: Indskrevne børn i fritidsordninger efter område, pasningstilbud, ejerform, alder og tid
measure: indhold (unit Antal)
columns:
- amt: join dim.nuts on amt=kode; levels [3]
- paskat: values [PTOT=Pasningstilbud i alt, 63=SFO, 62=Fritidshjem, 75=Fritids-, junior- og ungdomsklub]
- ejerform: values [TOTA=Ejerform i alt, 74=Kommunal, 76=Selvejende og privat]
- alder1: values [IALT=Alder i alt, 04=Under 5 år, 5=5 år, 6=6 år, 7=7 år, 8=8 år, 9=9 år, 10=10 år, 11=11 år, 12=12 år, 13=13 år, 14=14 år, 15=15 år, 16=16 år, 17=17 år, 18=18 år]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- amt contains kode 0 (national total, not in dim.nuts) and niveau 3 (98 kommuner) only — no regional breakdown. Use ColumnValues("nuts", "titel", for_table="boern5") to see available municipalities.
- 4 dimensions with aggregate rows: paskat=PTOT, ejerform=TOTA, alder1=IALT. To get a simple total children count: WHERE paskat='PTOT' AND ejerform='TOTA' AND alder1='IALT'. Forgetting any one inflates by 3-4x.
- alder1 'Under 5 år' (04) is a group covering pre-school aged children in afterschool care; individual ages start at 5. The age range spans 5-18 with no other groupings — aggregate in SQL with CASE if age groups are needed.
- This table covers fritidsordninger (SFO, fritidshjem, ungdomsklubber) — not dagpasning (vuggestuer, børnehaver). For dagtilbud enrolled children use boern2/pboern2.
- Map: context/geo/kommuner.parquet — merge on amt=dim_kode. Exclude amt=0.
