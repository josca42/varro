table: fact.skib13
description: Danske skibe 1. januar efter skibstype, alder, enhed og tid
measure: indhold (unit -)
columns:
- skibtype: values [40005=SKIBE I ALT, 40031=Tankskibe, 40039=Tørlastskibe, 40060=PASSAGERSKIBE OG FÆRGER, 40071=Fiskerfartøjer, 40130=Skibe i øvrigt]
- alder1: values [IALT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 2529=25-29 år, 3049=30-49 år, 50OV=50 år og derover, UOPLYST=Uoplyst alder]
- enhed: values [6000=Skibe (antal), 6500=Bruttotonnage (BT)]
- tid: date range 1994-01-01 to 2025-01-01

notes:
- enhed is a unit selector: 6000=Skibe (antal), 6500=Bruttotonnage (BT). Always filter to one enhed.
- alder1=IALT is the total. Age groups are 5-year bands (codes are text: '0-4', '5-9', ..., '2529', '3049', '50OV'). Note the non-standard coding for 25-29 ('2529') and 30-49 ('3049').
- alder1=UOPLYST (unknown age) exists — include or exclude depending on whether you want a complete count.