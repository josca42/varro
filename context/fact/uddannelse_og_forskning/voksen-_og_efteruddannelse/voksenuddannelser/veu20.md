table: fact.veu20
description: Kursusdeltagelse ved voksen og efteruddannelse efter uddannelsesområde, bopælsområde, alder, køn, tidsangivelse, enhed og tid
measure: indhold (unit Antal)
columns:
- fuddomr: values [TOT=I alt, H10=H10 Grundskole, H1040=H1040 Grundskolefag for voksne, H104010=H104010 Almen voksenuddannelse, enkeltfag, H10401010=H10401010 Almen voksenuddannelse, enkeltfag ... H80306010=H80306010 Konservering - restaurering uden nærmere angivelse, Ph.d., H8059=H8059 Teknisk videnskab, Ph.d., H805910=H805910 Teknisk videnskab uden nærmere angivelse, Ph.d., H80591010=H80591010 Teknisk videnskab uden nærmere angivelse, Ph.d., H70901510=H70901510 Ergoterapi, LVU]
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- alder: values [0000=Alder i alt, 25UN=Under 25 år, 2539=25-39 år, 4059=40-59 år, 6099=60 år og derover]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- tidspunkter: values [22=Skoleår, 11=Kalenderår]
- overnat1: values [11=Kursister, 13=Årselever]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- overnat1 and tidspunkter are both measurement selectors — every dimension combination appears 4 times (2×2). Always filter both: e.g. overnat1='11' (Kursister) AND tidspunkter='11' (Kalenderår). Forgetting either silently doubles the count.
- bopomr joins dim.nuts with 3 hierarchy levels: niveau 1 = 5 regioner, niveau 2 = landsdele, niveau 3 = kommuner. Use ColumnValues("nuts", "titel", for_table="veu20") to browse. Filter WHERE d.niveau=3 for kommuner or d.niveau=1 for regioner to avoid mixing levels. bopomr='0' means "Hele landet" (national total, not in dim.nuts). bopomr='996' means "Uoplyst region" (also not in dim.nuts). Use bopomr='0' for national totals without a join.
- fuddomr is a 4-level inline hierarchy encoded in code length: 3 chars = niveau 1 (~13 codes, e.g. H10, H20), 5 chars = niveau 2 (~70 codes, e.g. H1040), 7 chars = niveau 3 (~324 codes), 9 chars = niveau 4 (~454 codes). Mixing levels massively overcounts. Use fuddomr='TOT' for all education areas, or filter by code length (e.g. WHERE length(fuddomr)=3 AND fuddomr!='TOT') for a clean L1 breakdown.
- To get a single national total for a year: WHERE kon='10' AND alder='0000' AND overnat1='11' AND tidspunkter='11' AND bopomr='0' AND fuddomr='TOT' AND tid='2023-01-01' → returns one row.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr IN (0, 996).