table: fact.skib17
description: Danske skibe i udenlandsk register efter alder, enhed og tid
measure: indhold (unit -)
columns:
- alder: values [IALT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 2529=25-29 år, 3049=30-49 år, 50OV=50 år og derover, UOPLYST=Uoplyst alder]
- enhed: values [6000=Skibe (antal), 6500=Bruttotonnage (BT)]
- tid: date range 2017-01-01 to 2025-01-01

notes:
- enhed is a unit selector: 6000=Skibe (antal), 6500=Bruttotonnage (BT). Always filter to one enhed.
- alder=IALT is the total. Age groups use the same text coding as skib13 (5-year bands: '2529'=25-29 år, '3049'=30-49 år, '50OV'=50 år og derover).
- Covers only Danish ships in foreign registers (2017–2025). Complementary to skib13 (ships in Danish registers) for age analysis.