table: fact.statusu6
description: 18-25 årige efter uddannelsesstatus, uddannelse, grundskolens beliggenhed og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- uddannelse: values [TOT=I alt, H00=Ingen ungdomsuddannelse, H20=H20 Gymnasiale uddannelser, H29=H29 Erhvervsfaglige grundforløb, H30=H30 Erhvervsfaglige uddannelser, H99=Andre højere uddannelser]
- grundbel: join dim.nuts on grundbel=kode; levels [3]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- grundbel joins dim.nuts at niveau 3 (98 kommuner). Use ColumnValues("nuts", "titel", for_table="statusu6") to see the 98 municipalities present.
- Two codes are not in dim.nuts: grundbel=0 (I alt, national total) and grundbel=98 (not a municipality — likely "Uoplyst"/abroad, ~60k persons in 2024). A plain INNER JOIN will automatically exclude both; an OUTER JOIN will carry them as NULL. When mapping by kommune, use JOIN and you get clean results.
- 3 dimension columns (uddstat, uddannelse, grundbel). To get completion rates by municipality: filter uddstat='FULDFOERT', uddannelse='TOT', join dim.nuts on grundbel=kode WHERE niveau=3.
- This is the only statusu table with geographic breakdown (by municipality of primary school). Note: geography is the school's location, not the student's home municipality.
- Map: context/geo/kommuner.parquet — merge on grundbel=dim_kode. Exclude grundbel=0 (national total) and grundbel=98 (Uoplyst/abroad).