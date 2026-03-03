<fact tables>
<table>
id: frdk125
description: Befolkningsfremskrivning 2025 for hele landet efter herkomst, køn, alder og tid
columns: herkomst, kon, alder, tid (time), indhold (unit Antal)
tid range: 2025-01-01 to 2070-01-01
</table>
<table>
id: frld125
description: Befolkningsfremskrivning 2025 efter region/landsdel, alder, køn og tid
columns: regland, alder, kon, tid (time), indhold (unit Antal)
tid range: 2025-01-01 to 2050-01-01
</table>
<table>
id: frkm125
description: Befolkningsfremskrivning 2025 efter kommune, alder, køn og tid
columns: kommunedk, alder, kon, tid (time), indhold (unit Antal)
tid range: 2025-01-01 to 2050-01-01
</table>
<table>
id: frdk225
description: Nøgletal 2025: Fremskrivning af befolkningens bevægelser efter herkomst, bevægelsesart og tid
columns: herkomst, bevaegelse, tid (time), indhold (unit Antal)
tid range: 2025-01-01 to 2070-01-01
</table>
<table>
id: frld225
description: Nøgletal 2025: Fremskrivning af befolkningens bevægelser efter landsdel, bevægelsesart og tid
columns: landsdel, bevaegelse, tid (time), indhold (unit Antal)
tid range: 2025-01-01 to 2050-01-01
</table>
<table>
id: frkm225
description: Nøgletal 2025: Fremskrivning af befolkningens bevægelser efter kommune, bevægelsesart og tid
columns: kommunedk, bevaegelse, tid (time), indhold (unit Antal)
tid range: 2025-01-01 to 2050-01-01
</table>
<table>
id: frdk325
description: Forudsætninger vedrørende fertilitet til befolkningsfremskrivningen 2025 efter alder, herkomst og tid
columns: alder, herkomst, tid (time), indhold (unit Fertilitetskvotient)
tid range: 2025-01-01 to 2069-01-01
</table>
<table>
id: frdk425
description: Forudsætninger vedrørende dødelighed til befolkningsfremskrivningen 2025 efter køn, alder, dødelighedstavle og tid
columns: kon, alder, tavle, tid (time), indhold (unit -)
tid range: 2025-01-01 to 2069-01-01
</table>
<table>
id: frdk525
description: Forudsætninger vedrørende vandringer til befolkningsfremskrivningen 2025 efter køn, alder, herkomst, bevægelse og tid
columns: kon, alder, herkomst, bevaegelsev, tid (time), indhold (unit Antal)
tid range: 2025-01-01 to 2069-01-01
</table>
<table>
id: frbev25
description: Befolkningens udvikling efter bevægelsesart, køn og tid
columns: bevaegelse, kon, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2024-01-01
</table>
<table>
id: frgnsk25
description: Befolkningens udvikling efter bevægelsesart, alder, køn og tid
columns: bevaegelse, alder, kon, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- The 2025 forecast series splits into three geographic levels: national (frdk*25), region/landsdel (frld*25), kommune (frkm*25). The middle digit: 1=befolkningstal, 2=nøgletal/bevægelser, 3-5=forudsætninger.
- For projected population counts by herkomst/køn/alder: frdk125 (national, to 2070), frld125 (region+landsdel, to 2050), frkm125 (99 kommuner, to 2050).
- For projected population movements (fødte, døde, til/fraflytning, vandring): frdk225 (national + herkomst), frld225 (landsdel only), frkm225 (kommune).
- frdk225/frld225/frkm225 have a bevaegelse column mixing stock (B01=befolkning primo) and flow measures. Never sum across bevaegelse — pick the specific type you need (B02=levendefødte, B03=døde, B08=indvandrede, B09=udvandrede, B11=tilvækst).
- Assumptions tables (forudsætninger): frdk325=fertilitet (fertilitetskvotient by alder+herkomst), frdk425=dødelighed, frdk525=vandringer. All national only.
- frdk425 has a tavle column (measurement selector): tavle=2 is dødshyppighed pr. 100.000, tavle=3 is middellevetid. Always filter to one value — both appear for every kon/alder/tid row, so leaving it unfiltered doubles all counts.
- herkomst in frdk125/frdk225 uses inline codes 999/24/25/34/35 (splitting by vestlig/ikke-vestlig) — NOT joinable to dim.herkomst. In frdk325/frdk525 it uses F3-F12 (further split by statsborgerskab). Use ColumnValues("frdk125", "herkomst") or ColumnValues("frdk325", "herkomst") to decode.
- frld125 mixes regioner (niveau 1, kode 81-85) and landsdele (niveau 2, kode 1-11) in the same regland column. Filter WHERE d.niveau=1 for regions or d.niveau=2 for landsdele to avoid double-counting.
- Historical actual data (1992-2024) for comparison: frbev25 (bevægelser by køn, no age) and frgnsk25 (bevægelser by køn+alder). Both are real past data, not forecasts — useful for validating forecast assumptions.
- Map: frkm125 and frkm225 support kommune-level choropleth via /geo/kommuner.parquet (merge on kommunedk=dim_kode). frld125 supports region/landsdel via /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) (merge on regland=dim_kode). frld225 uses /geo/landsdele.parquet (merge on landsdel=dim_kode).