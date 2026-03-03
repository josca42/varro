table: fact.uddakt20
description: Uddannelsesaktivitet i grundskolen efter uddannelse, alder, herkomst, national oprindelse, køn, grundskoleinstitutionstype, bopælsområde, status og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [TOT=I alt, U20=U20 0. klassetrin, U21=U21 1. klassetrin, U22=U22 2. klassetrin, U23=U23 3. klassetrin, U24=U24 4. klassetrin, U25=U25 5. klassetrin, U26=U26 6. klassetrin, U27=U27 7. klassetrin, U28=U28 8. klassetrin, U29=U29 9. klassetrin, U30=U30 10. klassetrin]
- alder: values [TOT=Alder i alt, -5=-5 år, 6=6 år, 7=7 år, 8=8 år, 9=9 år, 10=10 år, 11=11 år, 12=12 år, 13=13 år, 14=14 år, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20-=20 år og derover]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- herkomst1: values [TOT=I alt, 1=Danmark, 2=Vestlige lande, 9=Ikke-vestlige lande, 000=Uoplyst national oprindelse]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- grundskol: values [0=I alt, 1011=Efterskoler, 1012=Folkeskoler, 1013=Friskoler og private grundskoler, 1014=Kommunale ungdomsskoler og ungdomskostskoler, 1015=Specialskoler for børn, 1016=Dagbehandlingstilbud og behandlingshjem, 1999=Andre skoler]
- bopomr: join dim.nuts on bopomr=kode; levels [1, 3]
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- tid: date range 2005-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- This table has 8 dimension columns. For a simple national total, filter all non-target columns: uddannelse='TOT', alder='TOT', herkomst='TOT', herkomst1='TOT', kon='10', grundskol='0', bopomr='0', fstatus='B'. Missing any one inflates the result.
- fstatus is a critical selector: B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang. These are mutually exclusive statuses — always filter to exactly one.
- bopomr joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (99 kommuner). Niveau 2 (landsdele) is absent. Use WHERE d.niveau=1 for regions or d.niveau=3 for municipalities. Code 0 = national total (not in dim); codes 998 and 999 are special aggregates (not in dim) — skip these unless specifically needed.
- herkomst and herkomst1 are two independent breakdowns of origin. herkomst: 5=dansk oprindelse, 4=indvandrere, 3=efterkommere. herkomst1: 1=Danmark, 2=vestlige lande, 9=ikke-vestlige lande. Don't cross both in the same query without filtering the other to TOT.
- uddannelse codes U20–U30 map to klassetrin 0–10. TOT sums all levels.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.