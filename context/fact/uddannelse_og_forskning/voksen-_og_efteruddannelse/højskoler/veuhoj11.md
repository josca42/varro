table: fact.veuhoj11
description: Kursusdeltagelse i lange højskolekurser efter uddannelsesområde, alder, køn, institutionstype, tidsangivelse, enhed og tid
measure: indhold (unit Antal)
columns:
- fuddomr: values [TOT=I alt, H15=H15 Forberedende uddannelser, H1510=H1510 Højskoleforløb, H151010=H151010 Folke- og ungdomshøjskolekurser, H15101020=H15101020 Ungdomshøjskolekursus, H15101030=H15101030 Folkehøjskolekursus, alment, H15101040=H15101040 Folkehøjskolekursus, gymnastik / idræt, H15101050=H15101050 Folkehøjskolekursus for handicappede, H15101060=H15101060 Folkehøjskolekursus, andre, H1520=H1520 Introducerende og erhvervsrettede forløb, H152010=H152010 Husholdnings- og håndarbejdskurser, H15201010=H15201010 Husholdningskursus, alment, H15201020=H15201020 Husholdningskursus, andre, H15201030=H15201030 Håndarbejdskursus, H152050=H152050 Andre erhvervsrettede forløb, H15205010=H15205010 Kreativ basis, grafisk åben uddannelse]
- alder: values [0000=Alder i alt, 9920=Under 20 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- insttyp: values [0=Højskoler i alt, 101=Almene og grundtvigske højskoler, 102=Ungdomshøjskoler, 107=Frie fagskoler, 108=Seniorhøjskoler]
- tidspunkter: values [22=Skoleår, 11=Kalenderår]
- overnat1: values [11=Kursister, 13=Årselever]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- `tidspunkter` (11=Kalenderår, 22=Skoleår) and `overnat1` (11=Kursister, 13=Årselever) are both measurement selectors. Every combination is present — failing to filter either one doubles the result. Always specify both, e.g. `AND tidspunkter=11 AND overnat1=11`. Both columns are smallint.
- `fuddomr` is hierarchical with 4 levels: TOT → H15 → H1510 → H151010 → leaf codes. In practice TOT=H15 (all areas are under Forberedende uddannelser). H1510 and H151010 have identical counts, as do H1520 and H152010. Do not mix levels. To get a breakdown by course type, use only the leaf codes: H15101020, H15101030, H15101040, H15101050, H15101060 (folkehøjskole types) and H15201010, H15201020, H15201030 (husholdnings/håndarbejds types).
- `alder` total code is `'0'` (not `'0000'`). `insttyp` is a smallint — filter as `insttyp=0` for total.
- insttyp 108 (Seniorhøjskoler) has no data in recent years; only 101, 102, and 107 are present in later data.
- Simple total query example: `SELECT tid, indhold FROM fact.veuhoj11 WHERE fuddomr='TOT' AND alder='0' AND kon='TOT' AND insttyp=0 AND tidspunkter=11 AND overnat1=11 ORDER BY tid`