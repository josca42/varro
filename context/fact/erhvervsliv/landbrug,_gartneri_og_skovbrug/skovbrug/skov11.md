table: fact.skov11
description: Skovarealet efter område, bevoksning og tid
measure: indhold (unit ha)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2]
- bevoksning: values [200=Skovareal i alt, 205=Hjælpearealer, 210=Skovbevokset, 215=Midlertidigt ubevokset, 220=Løvtræ i alt, 225=Bøg, 230=Eg, 235=Ask, 240=Ær, 245=Birk, 250=Andet løvtræ, 255=Nåletræ i alt, 260=Rødgran, 265=Sitkagran, 275=Fyrrearter, 280=Nordmannsgran, 285=Nobilis, 270=Andre ædelgranarter, 290=Andet nåletræ, 295=Ukendt]
- tid: date range 1990-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts, but codes 0 and 15 are not in dim.nuts. ColumnValues("nuts", "titel", for_table="skov11") reveals: 0=Hele landet, 15="Landsdelene Byen København, Københavns omegn o..." (a combined Copenhagen/Sjælland landsdel aggregate). Code 15 is only present for years 1990–2015; from 2016 onward only omrade=0 and regions 81–85 are available.
- The 5 landsdele present (4=Bornholm, 7=Fyn, 8=Sydjylland, 9=Østjylland, 10=Vestjylland) are NOT exhaustive — they exclude the Copenhagen/Sjælland area. Do not sum these 5 without also including omrade=15. For years before 2016, use omrade=15 + the 5 landsdele for a complete Jylland/Øerne/Sjælland split. For 2016+, use regions 81–85 (niveau 1) for a complete breakdown.
- To avoid mixing hierarchy levels, filter omrade to either: niveau 1 (81–85, 5 regioner) OR the group of [4,7,8,9,10,15] (5 landsdele + combined Sjælland), not both. Use ColumnValues("nuts", "titel", for_table="skov11") to confirm what's available.
- bevoksning is hierarchical — do not sum across all codes. Hierarchy: 200=Skovareal i alt → {205=Hjælpearealer, 210=Skovbevokset → {215=Midlertidigt ubevokset, 220=Løvtræ i alt → {225=Bøg, 230=Eg, 235=Ask, 240=Ær, 245=Birk, 250=Andet løvtræ}, 255=Nåletræ i alt → {260=Rødgran, 265=Sitkagran, 270=Andre ædelgranarter, 275=Fyrrearter, 280=Nordmannsgran, 285=Nobilis, 290=Andet nåletræ}, 295=Ukendt}}. Use 200 for national total, 220/255/295 for species-group breakdown, or individual species codes for detail.
- 295=Ukendt is at the same level as 220 (løvtræ) and 255 (nåletræ), not a subcategory of nåletræ. 220 + 255 + 295 + 215 = 210 (skovbevokset).
- Map: context/geo/landsdele.parquet (niveau 2) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN (0, 15).