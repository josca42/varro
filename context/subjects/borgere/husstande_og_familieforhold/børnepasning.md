<fact tables>
<table>
id: boern8
description: Normeringer i kommunale og selvejende daginstitutioner, institutionslignende puljeordninger og dagpleje efter kommune, pasningstilbud og tid
columns: kommunedk, paskat, tid (time), indhold (unit Antal)
tid range: 2023-01-01 to 2024-01-01
</table>
<table>
id: boern2
description: Fuldtidsomregnet indskrevne børn i kommunale og selvejende daginstitutioner, puljeordninger og dagpleje efter område, pasningstilbud og tid
columns: blstkom, paskat, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: boern1
description: Fuldtidsomregnet pædagogisk personale i kommunale og selvejende daginstitutioner, institutionslignende puljeordninger og dagpleje efter område, stillingskategori, uddannelse og tid
columns: omrade, overens, uddannelse, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: pboern2
description: Fuldtidsomregnet indskrevne børn i private dagtilbudsinstitutioner efter område, pasningstilbud og tid
columns: blstkom, paskat, tid (time), indhold (unit Antal)
tid range: 2021-01-01 to 2023-01-01
</table>
<table>
id: pboern1
description: Fuldtidsomregnet pædagogisk personale i private dagtilbudsinstitutioner efter område, stillingskategori, uddannelse og tid
columns: omrade, overens, uddannelse, tid (time), indhold (unit Antal)
tid range: 2021-01-01 to 2023-01-01
</table>
<table>
id: boern5
description: Indskrevne børn i fritidsordninger efter område, pasningstilbud, ejerform, alder og tid
columns: amt, paskat, ejerform, alder1, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: boern61
description: Fuldtidsomregnet pædagogisk personale i kommunale skolefritidsordninger efter område, stillingskategori og tid
columns: amt, stilkat, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: dagtil4
description: Modtagere af tilskud vedr. privat pasning og pasning af egne børn efter område, tilskudsart, berørte og tid
columns: omrade, tilskudsart, berort, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: boern11
description: Fuldtidsomregnet pædagogisk personale ansat for statslige puljemidler efter kommune, stillingskategori og tid
columns: kommunedk, overens, tid (time), indhold (unit Antal)
tid range: 2023-01-01 to 2024-01-01
</table>
<table>
id: boern10
description: Fuldtidsomregnet børn oprykket til børnehave, før den 1. i måneden, efter de er fyldt tre år efter kommune og tid
columns: kommunedk, tid (time), indhold (unit Antal)
tid range: 2023-01-01 to 2024-01-01
</table>
<table>
id: boern4
description: Institutioner og enheder efter område, pasningstilbud, ejerform og tid
columns: blstkom, pastil, ejerform, tid (time), indhold (unit Antal)
tid range: 2017-01-01 to 2024-01-01
</table>
<table>
id: res88
description: Årstakster i børnepasning efter område, foranstaltningsart og tid
columns: omrade, institution, tid (time), indhold (unit Kr.)
tid range: 2007-01-01 to 2025-01-01
</table>
</fact tables>
notes:
- For enrolled children in dagtilbud (dagpleje, vuggestue, børnehave): use boern2 (kommunale + selvejende, 2015-2024) or pboern2 (private only, 2021-2023). To get the combined total, add them. Both use paskat=TOT for the all-types total.
- For enrolled children in fritidsordninger (SFO, fritidshjem, ungdomsklubber): use boern5 (2015-2024). Separate table from boern2/pboern2.
- For pedagogical staff counts: boern1 (kommunale + selvejende, 2015-2024) and pboern1 (private, 2021-2023) — both have overens x uddannelse cross-classification with TOT for each. NOTE: overens codes differ between the two tables (3-digit in boern1 vs 2-digit in pboern1 for same categories). For SFO staff use boern61.
- For staffing norms (normeringer): boern8 (2023-2024 only). indhold is a ratio (children per normeret staff), not a headcount — do not confuse with boern1/pboern1 counts.
- For institution counts: boern4 (2017-2024, kommuneniveau only). ejerform=0 is the aggregate — always filter to avoid double-counting.
- For childcare rates (prices in Kr.): res88 (2007-2025). Longest series in subject. Rates per institution type per municipality — not counts.
- For alternative childcare subsidies (private care, caring for own children): dagtil4 (2008-2024). Longest series in subject for this topic. No total rows — tilskudsart and berort are orthogonal.
- For state pool staff: boern11 (2023-2024 snapshot). For early-promotion tracking: boern10 (2023-2024 snapshot). Both are narrow specialist tables.
- All tables share a common pattern: geographic kode 0 = national total, not in dim.nuts. When joining to dim.nuts, kode 0 will not match — use LEFT JOIN or filter WHERE d.niveau IS NOT NULL to exclude it.
- Tables with geographic levels [1, 3] have both region (niveau 1, kode 81-85) and kommunal (niveau 3) data in the same column. Tables with only [3] have kommunal data only (no regional rollup in the fact table).
- Map: All 12 tables support choropleth maps at kommune level via context/geo/kommuner.parquet. boern8, boern2, boern1, pboern2, pboern1, boern11, boern10 also support region level via context/geo/regioner.parquet.
