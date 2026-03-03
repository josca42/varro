table: fact.uddakt10
description: Uddannelsesaktivitet efter bopælsområde, uddannelse, alder, køn, status og tid
measure: indhold (unit Antal)
columns:
- bopomr: join dim.nuts on bopomr=kode [approx]; levels [1, 3]
- uddannelse: values [TOT=I alt, H10=H10 Grundskole, H1010=H1010 Grundskole til og med 6. klasse, H1020=H1020 Grundskole 7.-9. klasse, H1030=H1030 Grundskole 10. klasse ... H8035=H8035 Naturvidenskab, Ph.d., H8039=H8039 Samfundsvidenskab, Ph.d., H8059=H8059 Teknisk videnskab, Ph.d., H8080=H8080 Jordbrug, natur og miljø, Ph.d., H8090=H8090 Sundhedsvidenskab, Ph.d.]
- alder: values [TOT=Alder i alt, -5=-5 år, 6=6 år, 7=7 år, 8=8 år ... 36=36 år, 37=37 år, 38=38 år, 39=39 år, 40-=40 år-]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- fstatus is a measurement selector — always filter to exactly one value: B=enrolled on 1 October, F=completed, T=new entrants. Forgetting this multiplies counts by 3.
- bopomr joins dim.nuts. Use niveau=1 for 5 regioner or niveau=3 for 99 kommuner. ColumnValues("nuts", "titel", for_table="uddakt10") shows available codes.
- Unmatched bopomr codes: '0' = national total (Hele landet, ~1.18M students in 2024), '998' and '999' = special/unknown categories (~8,060 each, not in dim.nuts). Sum of the 5 regions is 8,060 short of the national total — that gap sits in 998/999. For a national aggregate without a dim join, use bopomr='0'.
- uddannelse is hierarchical: TOT → top-level (H10, H15, H20, H29, H30, H35, H40, H50, H60, H70, H80) → sub-codes (e.g. H1010, H1020, H1030 within H10). Top-level codes sum to TOT. Do not mix levels when aggregating — filter to one level or use TOT.
- Minimal filter for a national student count: WHERE fstatus='B' AND bopomr='0' AND uddannelse='TOT' AND alder='TOT' AND kon='10'.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.