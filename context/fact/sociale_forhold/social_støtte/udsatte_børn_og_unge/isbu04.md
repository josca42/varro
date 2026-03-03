table: fact.isbu04
description: Aktive indsatser og støtte til børn og unge pr. 31. december efter landsdel, indsats, alder, køn og tid
measure: indhold (unit Antal)
columns:
- landsdel: join dim.nuts on landsdel=kode; levels [2]
- indsatser: values [3=INDSATSER OG STØTTE I ALT, 5=TIDLIGT FOREBYGGENDE INDSATSER EFTER LOV OM SOCIAL SERVICE / BARNETS LOV, 6=INDSATSER OG STØTTE EFTER LOV OM SOCIAL SERVICE / BARNETS LOV, 7=INDSATSER EFTER LOV OM BEKÆMPELSE AF UNGDOMSKRIMINALITET]
- alder: values [IALT=Alder i alt, 0005=0-5 år, 0611=6-11 år, 1217=12-17 år, 1800=18 år og derover, 999=Uoplyst alder]
- kon: values [0=I alt, D=Drenge, P=Piger, 9=Uoplyst køn]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- STOCK table (pr. 31. december = active on Dec 31), with age and gender breakdown at landsdel level.
- indsatser has 4 high-level codes: 3=I alt, 5=Tidligt forebyggende, 6=SEL/BL, 7=Ungdomskriminalitetsloven. Codes 5+6+7 roll up into 3.
- landsdel joins dim.nuts at niveau 2 (11 landsdele). Code 0 = national total.
- alder: IALT + 4 age groups + 999. kon: 0=I alt, D/P.
- For totals: WHERE indsatser=3 AND alder='IALT' AND kon='0'.
- Map: /geo/landsdele.parquet — merge on landsdel=dim_kode. Exclude landsdel=0.