table: fact.folk1e
description: Befolkningen den 1. i kvartalet efter område, køn, alder, herkomst og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [IALT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- herkomst: values [TOT=I alt, 1=Personer med dansk oprindelse, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande]
- tid: date range 2008-01-01 to 2025-07-01
dim docs: /dim/nuts.md

notes:
- omrade=0 is the national total ("I alt") — not in dim.nuts. dim.nuts covers niveau=1 (5 regioner) and niveau=3 (99 kommuner).
- herkomst encodes the west/non-west split inline: TOT=I alt, 1=dansk oprindelse, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande. No dim join.
- alder has individual years (0–125) with IALT as total. No aggregate age bands.
- 4 dimension columns (omrade, kon, alder, herkomst). Filter non-target dims: omrade=0, kon='TOT', alder='IALT', herkomst='TOT'.
- To get total indvandrere: filter herkomst IN (24, 25) or use herkomst='TOT' and subtract 1 and 34+35.  Simpler: use folk1c herkomst=4 (but note folk1c ends 2020).
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.