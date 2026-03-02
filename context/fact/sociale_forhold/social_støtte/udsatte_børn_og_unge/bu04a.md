table: fact.bu04a
description: Støtte til børn og unge pr. 31. december (nettoopgørelse) efter område, foranstaltning, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [2]
- foran: values [1.0=Udsatte børn og unge i alt, 2.0=Børn og unge der modtager støttende indsatser i alt, 3.0=Indsatser og støtte i alt, 4.0=Personrettede forebyggende foranstaltninger i alt (til 2018), 5.0=Børn og unge med personrettede forebyggende foranstaltninger i alt (til 2018) ... 462.0=Støtteperson uden for familie/netværk for barnet eller den unge under anbringelsen (BL §53.2, fra 2024), 463.0=Venskabsfamilie fra familie/netværk for barnet eller den unge under anbringelsen (BL §54.1, fra 2024), 464.0=Venskabsfamilie uden for familie/netværk for barnet eller den unge under anbringelsen (BL §54.2, fra 2024), 498.0=Familiebehandling (jf. lov om bekæmpelse af ungdomskriminalitet §13.1.4), 499.0=Kontaktperson for hele familien (jf. lov om bekæmpelse af ungdomskriminalitet §13.1.7. Til 2023)]
- alder: values [IALT=Alder i alt, 0005=0-5 år, 0611=6-11 år, 1217=12-17 år, 1800=18 år og derover, 999=Uoplyst alder]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder, 9=Uoplyst køn]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 2 (11 landsdele). Code 0 = national total (not in dim), code 99 = unknown region (tiny, ignore). Always filter to one omrade or join dim to get titles.
- foran has 65 hierarchical codes. Codes 1, 2, 3 are top-level totals: 1=Udsatte børn og unge i alt, 2=Børn med støttende indsatser, 3=Indsatser og støtte i alt. Code 3 can exceed code 1 because one child can have multiple indsatser. Codes 107+ are specific intervention types — subcategories that roll up into the top codes. Never sum across multiple foran codes; pick one code.
- alder: IALT=all ages, 0005/0611/1217/1800 are age groups, 999=unknown. Filter to IALT for totals.
- kon uses TOT/M/K/9 (unlike anbaar tables which use 0/D/P/9). Filter to TOT for totals.
- To get total udsatte children by landsdel in 2024: WHERE foran=1 AND alder='IALT' AND kon='TOT' AND tid='2024-01-01'
- Map: context/geo/landsdele.parquet — merge on omrade=dim_kode. Exclude omrade=0.