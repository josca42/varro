table: fact.ligeii2
description: Ligestillingsindikator for personindkomst efter aldersgrupper, indkomsttype, enhed, indikator og tid
measure: indhold (unit -)
columns:
- aldgrp: values [TOT=Alder i alt, U20=Under 20 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6569=65-69 år, 70OV=70 år og derover]
- indkomsttype: values [IND1=Disponibel indkomst, ekskl. børnefamilieydelser og boligstøtte, IND2=Indkomst før skat, ekskl. børnefamilieydelser og boligstøtte, IND3=Erhvervsindkomst, IND4=Offentlige overførsler, ekskl. børnefamilieydelser og boligstøtte, IND5=Børnefamilieydelser og boligstøtte, IND6=Private pensioner, IND7=Formueindkomst (brutto) og anden indkomst]
- enhed: values [1=Gennemsnit, 2=Median]
- indikator: values [LAK1=Mænd (kr.), LAK2=Kvinder (kr.), LAK3=Indkomstgab (pct.)]
- tid: date range 1991-01-01 to 2023-01-01
notes:
- indikator has three semantically distinct values: LAK1=men's income (kr.), LAK2=women's income (kr.), LAK3=gender gap (%). Filter to one — never sum across them.
- enhed selector (gennemsnit vs. median). Always filter to one.
- aldgrp='TOT' is the total. No geography breakdown.
- indkomsttype uses short IND1-IND7 codes (not the 100-290 series). IND1=disponibel indkomst ekskl. børnefamilieydelser og boligstøtte.
- Goes back to 1991. For gender gap by socioøkonomisk status use ligeii1.
