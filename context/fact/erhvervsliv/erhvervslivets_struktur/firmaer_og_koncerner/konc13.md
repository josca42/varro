table: fact.konc13
description: Aktive firmaer der indgår i koncerner efter branche (DB07 10-grp.), enhed og tid
measure: indhold (unit -)
columns:
- branche0710: values [TOT=TOT Erhverv i alt, 1=1 Landbrug, skovbrug og fiskeri, 2=2 Industri, råstofindvinding og forsyningsvirksomhed, 3=3 Bygge og anlæg, 4=4 Handel og transport mv., 5=5 Information og kommunikation, 6=6 Finansiering og forsikring, 7=7 Ejendomshandel og udlejning, 8=8 Erhvervsservice, 9=9 Offentlig administration, undervisning og sundhed, 10=10 Kultur, fritid og anden service, 11=11 Uoplyst aktivitet]
- enhed: values [AFI=Firmaer (antal), AFU=Fuldtidsansatte (antal)]
- tid: date range 2022-01-01 to 2023-01-01

notes:
- enhed has only two values here: AFI=firmaer (antal), AFU=fuldtidsansatte (antal). No OMS unlike other gf/fgf tables. Always filter to one value.
- branche0710 is fully inline (TOT + 10 sector codes with full Danish labels). No dim join needed.
- Only 2022–2023. Use to see which sectors have the most firms/employees participating in business groups (koncerner).