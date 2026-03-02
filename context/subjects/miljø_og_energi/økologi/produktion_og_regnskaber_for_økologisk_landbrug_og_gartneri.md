<fact tables>
<table>
id: oeko11
description: Økologiske bedrifter og arealer efter økologisk status, afgrøde og tid
columns: oekostatus, afgrode, tid (time), indhold (unit -)
tid range: 2012-01-01 to 2024-01-01
</table>
<table>
id: ani7
description: Mælkeproduktion og anvendelse efter enhed og tid
columns: enhed, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: ani8
description: Ægproduktion og produktionsformer efter enhed og tid
columns: enhed, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: jord1
description: Resultatopgørelse for alle bedrifter (gennemsnit) efter bedriftstype region standardoutput, kvartilgruppe, regnskabsposter og tid
columns: bedriftstand, kvartil, regnskposter, tid (time), indhold (unit Gns.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: jord2
description: Resultatopgørelse for heltidsbedrifter (gennemsnit) efter bedriftstype årsværk, kvartilgruppe, regnskabsposter og tid
columns: bedriftaars, kvartil, regnskposter, tid (time), indhold (unit Gns.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: jord4
description: Familiernes økonomi for heltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
columns: brugstype, kvartil, regnskposter, tid (time), indhold (unit Gns.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: jord3
description: Resultatopgørelse for deltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
columns: brugstype, kvartil, regnskposter, tid (time), indhold (unit Gns.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: jord5
description: Familiernes økonomi for deltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
columns: brugstype, kvartil, regnskposter, tid (time), indhold (unit Gns.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: jord6
description: Nøgletal for alle bedrifter (gennemsnit) efter bedriftstype region standardoutput, kvartilgruppe, regnskabsposter og tid
columns: bedriftstand, kvartil, regnskposter, tid (time), indhold (unit Gns.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: jord7
description: Nøgletal for alle heltidsbedrifter (gennemsnit) efter bedriftstype årsværk, kvartilgruppe, regnskabsposter og tid
columns: bedriftaars, kvartil, regnskposter, tid (time), indhold (unit Gns.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: jord8
description: Nøgletal for deltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
columns: brugstype, kvartil, regnskposter, tid (time), indhold (unit Gns.)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: jord9
description: Energiforbrug for heltidsbedrifter (gennemsnit) efter bedriftstype, kvartilgruppe, regnskabsposter og tid
columns: brugstype, kvartil, regnskposter, tid (time), indhold (unit Gns.)
tid range: 2008-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For organic area and farm counts: use oeko11 (2012–2024). oekostatus=225 is the total; 210/215/220 break down by conversion stage (not started, under conversion, fully converted). afgrode selects crop type (ha) or bedrifter count (only under oekostatus=225). Don't sum all oekostatus values — 225 already includes 210+215+220.
- For organic milk: use ani7, enhed='OKO' (series from 1993). For organic eggs: ani8, enhed='OKOAEG' (volume), SALG3 (price). Both ani tables are measurement-selector tables — filter to one enhed per query, never sum across them.
- For farm income statements (resultatopgørelse): jord1 = all farms; jord2 = heltidsbedrifter; jord3 = deltidsbedrifter. All three share the same 238 regnskposter account items and cover 2008–2024. Use farm-type code 3 for organic (bedriftstand/bedriftaars/brugstype='3').
- For family economy: jord4 = heltidsbedrifter (3 farm types, continuous to 2024); jord5 = deltidsbedrifter (organic series ends 2019, only combined "Jordbrug" from 2020).
- For key ratios (nøgletal — soliditetsgrad, gældsprocent, lønningsevne, etc.): jord6 = all farms; jord7 = heltidsbedrifter; jord8 = deltidsbedrifter. Report ratio values directly — do not sum or average them.
- For energy consumption: jord9 = heltidsbedrifter only. ENERGIFORBRUG I ALT (regnskposter=4500) and greenhouse items are only available for Gartneri farm types (brugstype 4, 538–575). Landbrug/Konventionelt/Økologisk (brugstype 1–3) only have agricultural energy sub-items (no single total row).
- Table naming pattern: jord1+jord6 = all farms (resultatopgørelse + nøgletal), jord2+jord7 = heltidsbedrifter, jord3+jord8 = deltidsbedrifter, jord4+jord5 = familiernes økonomi for heltids/deltids.
- DISCONTINUED: jord3, jord5, jord8 all lose farm-type breakdown after 2019. From 2020 only the combined brugstype=0 ("Jordbrug") exists for part-time farms. For recent organic vs. conventional comparisons in part-time farms, use jord1/jord6 (all farms) and filter to bedriftstand=3 instead.
- All jord tables are per-farm averages (Gns.), not population totals. regnskposter=0 gives antal bedrifter in the sample.