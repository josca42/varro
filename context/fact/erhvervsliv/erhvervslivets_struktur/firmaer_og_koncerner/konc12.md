table: fact.konc12
description: Koncerner i Danmark efter koncernstørrelse (firmaer), enhed og tid
measure: indhold (unit -)
columns:
- koncern: values [AF=I alt, DF=2 firmaer, FF=3-5 firmaer, GF=6-9 firmaer, HF=10-19 firmaer, IF=20-49 firmaer, KF=50 eller flere firmaer]
- enhed: values [15=Koncerner, 16=Fuldtidsansatte i koncern, 17=Firmaer i koncern]
- tid: date range 2022-01-01 to 2023-01-01

notes:
- enhed determines what indhold counts: 15=antal koncerner, 16=fuldtidsansatte i koncern, 17=firmaer i koncern. Always filter to one.
- koncern = size by number of firms within the group. AF = total. 6 size buckets from 2 firms up to 50+.
- Like konc11 but sized by firm count rather than employee count. Use both tables together if you need the full picture of group structure.