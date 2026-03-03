<fact tables>
<table>
id: fro
description: Frøproduktion efter afgrøde, enhed og tid
columns: afgrode, maengde4, tid (time), indhold (unit -)
tid range: 1989-01-01 to 2024-01-01
</table>
<table>
id: halm1
description: Halmudbytte og halmanvendelse efter område, afgrøde, enhed, anvendelse og tid
columns: omrade, afgrode, enhed, anvendelse, tid (time), indhold (unit -)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: hst5
description: Prognose for vinterafgrøder til høst efter afgrøde, enhed og tid
columns: afgrode, enhed, tid (time), indhold (unit 1.000 ha)
tid range: 2000-01-01 to 2025-01-01
</table>
<table>
id: hst77
description: Høstresultat efter område, afgrøde, enhed og tid
columns: omrade, afgrode, maengde4, tid (time), indhold (unit -)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: hst1920
description: Høstresultat (historisk) efter afgrøde og tid
columns: afgrode, tid (time), indhold (unit -)
tid range: 1920-01-01 to 1981-01-01
</table>
<table>
id: korn
description: Anvendelsen af korn efter afgrøde, periode, oprindelse, type og tid
columns: afgrode, periode, oprind, type, tid (time), indhold (unit Mio. kg)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: korn2
description: Lager og omsætning af korn efter afgrøde, aktører og tid
columns: afgrode, ak, tid (time), indhold (unit Mio. kg)
tid range: 2000-01-01 to 2024-07-01
</table>
<table>
id: vhus1
description: Væksthuse efter område, strukturforhold og tid
columns: omrade, struk, tid (time), indhold (unit -)
tid range: 1993-01-01 to 2023-01-01
</table>
<table>
id: vhus2
description: Væksthussektorens forbrug efter produktion, væksthusareal i kvadratmeter (m2), areal og forbrug og tid
columns: prod, vaekst, areal2, tid (time), indhold (unit -)
tid range: 2002-01-01 to 2023-01-01
</table>
<table>
id: gartn1
description: Produktion af frugt og grønt efter område, enhed, afgrøde og tid
columns: omrade, tal, afgrode, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For harvest results by region: use hst77 (2006–, 30 crop codes, 5 measures including area/yield/production/foderværdi). For national-level harvest going back to 1920: use hst1920 (area and production encoded in afgrode codes, no separate unit column).
- For winter crop forecasts: hst5 has both prognose and høstet areal side by side — filter enhed=4A for actual, 3A for forecast.
- For grain balance sheet (imports, exports, feed use, milling): use korn (national, 1995–, calendar year and crop year). For grain stocks and trader flows at monthly frequency: use korn2 (2000–monthly).
- For straw yield and use by region: halm1 (2006–). Has enhed (area vs. weight) and anvendelse (total vs. specific uses) — both need filtering.
- For seed crop production: fro (national, 1989–, grass legumes and grass species).
- For greenhouse sector: vhus1 for structural stats by region (number of farms, area by age/heating/construction type). vhus2 for resource consumption (area/water/energy) by production type and greenhouse size class — national only.
- For market garden fruit and vegetable production by region: gartn1 (2003–, 53 crop codes, filter tal for area vs. production).
- Shared omrade pattern: halm1, hst77, vhus1, gartn1 all join dim.nuts with the same 12 omrade codes. INNER JOIN gives 10 labeled geographies (5 regioner + 5 agricultural landsdele: Bornholm, Fyn, Sydjylland, Østjylland, Vestjylland). omrade=0 (Hele landet) and omrade=15 (unmapped aggregate) are not in dim.nuts — handle separately for national totals.
- Measurement selector warning: every table with multiple measures per row (fro.maengde4, halm1.enhed, hst5.enhed, hst77.maengde4, vhus2.areal2, gartn1.tal) requires filtering to one value. Forgetting this silently multiplies the result.
- Map: halm1, hst77, vhus1, gartn1 support choropleth maps via /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Note only 5 of 11 landsdele are present (agricultural regions). Exclude omrade=0.