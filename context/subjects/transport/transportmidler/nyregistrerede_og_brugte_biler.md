<fact tables>
<table>
id: bil5
description: Nyregistrerede motorkøretøjer efter køretøjstype og tid
columns: biltype, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2025-09-01
</table>
<table>
id: bil55
description: Nyregistrerede personbiler efter registreringsform og tid
columns: regbil, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-09-01
</table>
<table>
id: bil6
description: Nyregistreringer, brugtvognshandel og bestand mv. efter køretøjstype, enhed og tid
columns: biltype, enhed, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2025-09-01
</table>
<table>
id: bil50
description: Nyregistrerede personbiler efter ejerforhold, bil segment, enhed og tid
columns: ejer, bilseg, enhed, tid (time), indhold (unit -)
tid range: 2004-01-01 to 2025-09-01
</table>
<table>
id: bil51
description: Nyregistrerede personbiler efter ejerforhold, drivmiddel og tid
columns: ejer, driv, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2025-09-01
</table>
<table>
id: bil53
description: Nyregistrerede motorkøretøjer efter område, køretøjstype, brugerforhold, drivmiddel og tid
columns: omrade, biltype, brug, driv, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2025-10-01
</table>
<table>
id: bil56
description: Brugte personbiler efter enhed, ejerforhold, drivmiddel og tid
columns: enhed, ejer, driv, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2025-10-01
</table>
<table>
id: bil57
description: Brugte personbiler efter sæsonkorrigering og tid
columns: saeson, tid (time), indhold (unit Antal)
tid range: 2004-01-01 to 2025-09-01
</table>
<table>
id: ee1
description: Nyregistrerede personbiler efter energieffektivitet, ejerforhold, drivmiddel og tid
columns: energi, ejer, driv, tid (time), indhold (unit -)
tid range: 1997-07-01 to 2024-06-01
</table>
<table>
id: ee2
description: Nyregistrerede benzindrevne personbiler efter kilometer pr. liter, ejerforhold og tid
columns: km, ejer, tid (time), indhold (unit Antal)
tid range: 1997-07-01 to 2024-01-01
</table>
<table>
id: ee3
description: Nyregistrerede dieseldrevne personbiler efter kilometer pr. liter, ejerforhold og tid
columns: km, ejer, tid (time), indhold (unit Antal)
tid range: 1997-07-01 to 2024-01-01
</table>
<table>
id: tema9013
description: Biler og deres C02-udledning efter enhed og tid
columns: enhed, tid (time), indhold (unit Indeks)
tid range: 1990-01-01 to 2024-01-01
</table>
</fact tables>
notes:
- For new registrations by vehicle type (personbiler, varebiler, motorcykler, etc.) from 1992: bil5. Simple biltype×tid, but beware biltype includes both raw and seasonally-adjusted series in the same column — pick one.
- For new personbil registrations by fuel type (benzin/diesel/el/hybrid): bil51 (from 2011). For regional breakdown by fuel type and vehicle type: bil53 (from 2018, joins dim.nuts).
- For new personbil registrations by ownership (leasing vs. direct, husholdning vs. erhverv): bil55 (from 2007). For segment breakdown (mini/SUV/MPV etc.) with prices and engine stats: bil50 (from 2004).
- For combined view (new registrations + used car trade + fleet stock) across vehicle types: bil6 (from 2000). Has enhed selector — always filter to one enhed or counts multiply by 6.
- For used personbil trade with fuel-type breakdown: bil56 (from 2011). For used-car trade with seasonal adjustment going back to 2004: bil57.
- For fuel efficiency of newly registered cars: ee1 (average efficiency, multiple metrics, 1997-2024). ee2 (petrol distribution, 1997-2024) and ee3 (diesel distribution, 1997-2024) for distribution analysis.
- For CO2 and car stock trends indexed to 2000: tema9013. Note the enhed=448 fuel efficiency series is missing from the database — use ee1 instead.
- Only bil53 has regional breakdown (kommuner/landsdele/regioner via dim.nuts join). All other tables are national-level only.
- Map: bil53 supports choropleth maps at all three NUTS levels — use /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1), merging on omrade=dim_kode. Exclude omrade IN (0, 99).
- Common pitfall across this subject: many tables have measurement-selector columns (enhed in bil6/bil50/bil56, energi in ee1, saeson in bil57, regbil in bil55) where the same dimension combination repeats once per selector value. Always filter to one selector value.
