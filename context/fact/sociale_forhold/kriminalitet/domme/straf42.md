table: fact.straf42
description: Strafferetlige afgørelser efter national oprindelse, overtrædelsens art, afgørelsestype, alder, køn og tid
measure: indhold (unit Antal)
columns:
- herkomst1: values [0=I alt, 80=Dansk statsborger, 81=Asylansøger, 82=Udlænding med ulovligt ophold, 83=Udlænding med opholdstilladelse, 84=Turister og udlændinge med visum, 85=Uoplyst mv.]
- overtraed: values [TOT=Overtrædelsens art i alt, 1=Straffelov i alt, 1000=Uoplyst straffelov, 11=Seksualforbrydelser i alt, 1110=Blodskam mv. ... 3845=Love vedrørende forsvaret o.l., 3850=Love vedrørende offentlige forsyninger, 3855=Love vedrørende spil, bevilling, næring, 3865=Særlovgivning i øvrigt, 3870=Uoplyst særlovgivning]
- afgorelse: values [000=Afgørelsestype i alt, 1=1 Dom til frihedsstraf, 11=11 Ubetinget frihedsstraf, 111=111 Ubetinget dom alene, 112=112 Delvis betinget dom ... 514=514 Frifindelse, 515=515 Straf bortfaldet, 516=516 Militær straf, 517=517 Ingen tillægsstraf (§89), 518=518 Anden afgørelse i øvrigt]
- alder: values [TOT=Alder i alt, UA=Uoplyst alder, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70-79=70-79 år, 80-=80 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder, VIRKSOMHEDER=Virksomheder]
- tid: date range 1995-01-01 to 2024-01-01

notes:
- Same column structure and overcounting risks as straf40, with an extra herkomst1 dimension. Filter herkomst1='0' for national total; codes 80-85 are mutually exclusive categories (dansk statsborger, asylansøger, ulovligt ophold, opholdstilladelse, visum, uoplyst).
- overtraed and afgorelse are both inline hierarchical — filter to one level in each (see straf40 notes). herkomst1='0' is the aggregate for the whole category.
- To get a simple total: WHERE herkomst1='0' AND overtraed='TOT' AND afgorelse='000' AND alder='TOT' AND kon='TOT'.
- Only from 1995 (straf40 goes back to 1980).
