table: fact.fodie
description: Levendefødte efter område, moders herkomst, moders oprindelsesland, moders statsborgerskab, moders alder, barnets køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- moherk: values [5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- mooprind: join dim.lande_psd on mooprind=kode; levels [3]
- mostat: join dim.lande_psd on mostat=kode; levels [3]
- modersalder: values [10=10 år, 11=11 år, 12=12 år, 13=13 år, 14=14 år ... 60=60 år, 61=61 år, 62=62 år, 63=63 år, 64=64 år]
- barnkon: values [D=Drenge, P=Piger]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/lande_psd.md, /dim/nuts.md
notes:
- 6 dimension columns, none with IALT/TOT totals. This table is wide — to get national total births, use omrade='0' and SUM across remaining dimensions (moherk × mooprind × mostat × modersalder × barnkon all multiply together). Usually GROUP BY a target dimension and fix the rest.
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (99 kommuner). Code '0' is a national aggregate not in dim.nuts — use for Denmark totals without a join. Filter d.niveau when joining to avoid mixing granularities.
- moherk has 4 mutually exclusive categories (0=Uoplyst, 3=Efterkommere, 4=Indvandrere, 5=Dansk oprindelse). No aggregate total — sum all 4 for a complete count.
- mooprind and mostat both join dim.lande_psd at niveau 3 only (individual countries). dim.lande_psd has 265 niveau-3 codes but fact.fodie uses only 195 for mooprind and 184 for mostat. Always use ColumnValues("lande_psd", "titel", for_table="fodie") — it drastically reduces the list. Hierarchy: niveau 1=continents, niveau 2=regions, niveau 3=countries. Only niveau 3 is present in the fact table.
- moherk and mooprind/mostat are strongly correlated: mothers with mooprind=Danmark (5100) will have moherk=5. When filtering to a specific country of origin, moherk is largely redundant.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
