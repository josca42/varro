table: fact.konc11
description: Koncerner i Danmark efter koncernstørrelse (fuldtidsansatte), enhed og tid
measure: indhold (unit -)
columns:
- koncernstor: values [AF=I alt, B=0 ansatte, C=1 ansat, E=2-9 ansatte, H=10-19 ansatte, I=20-49 ansatte, J=50-99 ansatte, L=100-999 ansatte, M=1.000 og derover]
- enhed: values [15=Koncerner, 16=Fuldtidsansatte i koncern, 17=Firmaer i koncern]
- tid: date range 2022-01-01 to 2023-01-01

notes:
- enhed determines what indhold counts: 15=antal koncerner, 16=fuldtidsansatte i koncern, 17=firmaer i koncern. Always filter to one — all three are stacked in the same table.
- koncernstor = size by employee count. AF = total (I alt). 8 size buckets from 0 up to 1000+.
- Only 2022–2023 data. Very small table — use for questions about the size distribution of business groups by employee count.