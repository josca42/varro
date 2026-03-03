table: fact.uddakt11
description: Uddannelsesaktivitet efter institutionens beliggenhedsområde, uddannelse, alder, køn, status og tid
measure: indhold (unit Antal)
columns:
- omrade1: join dim.nuts on omrade1=kode; levels [1, 3]
- uddannelse: values [TOT=I alt, H10=H10 Grundskole, H1010=H1010 Grundskole til og med 6. klasse, H1020=H1020 Grundskole 7.-9. klasse, H1030=H1030 Grundskole 10. klasse ... H8035=H8035 Naturvidenskab, Ph.d., H8039=H8039 Samfundsvidenskab, Ph.d., H8059=H8059 Teknisk videnskab, Ph.d., H8080=H8080 Jordbrug, natur og miljø, Ph.d., H8090=H8090 Sundhedsvidenskab, Ph.d.]
- alder: values [TOT=Alder i alt, -5=-5 år, 6=6 år, 7=7 år, 8=8 år ... 36=36 år, 37=37 år, 38=38 år, 39=39 år, 40-=40 år-]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade1 is institution location (where the school is), not student residence — use uddakt10 for residence-based analysis.
- omrade1 joins dim.nuts. Filter niveau=1 for 5 regioner or niveau=3 for 99 kommuner.
- Unmatched omrade1='0' = national total, not in dim.nuts. Use directly for national aggregates without a join.
- fstatus is a measurement selector — always filter to exactly one value: B=enrolled Oct 1, F=completed, T=new entrants.
- uddannelse is hierarchical (same as uddakt10): TOT → H10…H80 (top level) → sub-codes. Don't mix levels.
- Minimal filter for a national student count: WHERE fstatus='B' AND omrade1='0' AND uddannelse='TOT' AND alder='TOT' AND kon='10'.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade1=dim_kode. Exclude omrade1=0.