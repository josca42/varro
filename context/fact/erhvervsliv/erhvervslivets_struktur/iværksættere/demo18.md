table: fact.demo18
description: Erhvervsdemografi efter firmastørrelse (fuldtidsansatte), enhed og tid
measure: indhold (unit Antal)
columns:
- firmstr: values [30=Ingen ansatte, 31=Under 10 ansatte, 32=10 eller flere ansatte]
- maengde4: values [AFU=Fuldtidsansatte (antal), NYE=Nye firmaer (antal)]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- firmstr has 3 exhaustive size bands with no TOT row — it is safe to sum across all 3 to get a national total (30=ingen ansatte, 31=under 10 FTE, 32=10+ FTE).
- maengde4 is a measurement selector — filter to one: AFU=fuldtidsansatte, NYE=nye firmaer. Note firmstr=30 (ingen ansatte) always has AFU=0 by definition.
- Simple table with no dimension joins needed.