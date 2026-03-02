table: fact.rasie11
description: Arbejdsstyrken til ledighedspct-beregning (ultimo november) efter herkomst, oprindelsesland, alder, køn og tid
measure: indhold (unit Antal)
columns:
- herkomst: values [TOT=I alt, DAN=Dansk oprindelse, IND=Indvandrere / efterkommere, UOP=Uoplyst herkomst]
- ieland: join dim.lande_uhv on ieland=kode [approx]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2023-01-01
dim docs: /dim/lande_uhv.md

notes:
- ieland does NOT join dim.lande_uhv. Uses the same custom 39-code origin-country classification as aul03/aulk03 (30=Dansk oprindelse, 1=Vestlige lande, 2=Ikke-vestlige lande, TOT=I alt, etc.). Use ColumnValues("rasie11", "ieland"). Do not join dim.lande_uhv.
- herkomst and ieland overlap: herkomst=DAN corresponds to ieland='30'; herkomst=IND is the aggregate for all non-Danish origin. For origin-country breakdown use ieland; for simple DAN/IND split use herkomst.
- koen column (note spelling) has TOT. This table is the workforce denominator for computing origin-country unemployment rates. Pair with aul03/aulk03 for rates.
- Annual snapshots (ultimo november). Stopped 2023.