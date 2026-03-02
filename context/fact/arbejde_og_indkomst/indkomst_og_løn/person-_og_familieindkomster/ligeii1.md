table: fact.ligeii1
description: Ligestillingsindikator for personindkomst efter socioøkonomisk status, indkomsttype, enhed, indikator og tid
measure: indhold (unit -)
columns:
- socio: join dim.socio on socio=kode; levels [3]
- indkomsttype: values [IND1=Disponibel indkomst, ekskl. børnefamilieydelser og boligstøtte, IND2=Indkomst før skat, ekskl. børnefamilieydelser og boligstøtte, IND3=Erhvervsindkomst, IND4=Offentlige overførsler, ekskl. børnefamilieydelser og boligstøtte, IND5=Børnefamilieydelser og boligstøtte, IND6=Private pensioner, IND7=Formueindkomst (brutto) og anden indkomst]
- enhed: values [1=Gennemsnit, 2=Median]
- indikator: values [LAK1=Mænd (kr.), LAK2=Kvinder (kr.), LAK3=Indkomstgab (pct.)]
- tid: date range 1994-01-01 to 2023-01-01
dim docs: /dim/socio.md
notes:
- indikator has three semantically distinct values that must NEVER be summed: LAK1=men's income (kr.), LAK2=women's income (kr.), LAK3=gender gap (%). Filter to one indikator.
- enhed selector (gennemsnit vs. median). Always filter to one.
- socio joins dim.socio at niveau 3, but three codes are NOT in dim.socio: 100, 115, 130 (same custom aggregates as indkp104). An INNER JOIN silently drops them.
- indkomsttype here uses short IND1-IND7 codes (different from the 100-290 series in most other tables).
- No geography breakdown. For gender gap by age group use ligeii2.
