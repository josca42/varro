<fact tables>
<table>
id: fakom
description: Folkeafstemninger efter valgresultat, område og tid
columns: valres, omrade, tid (time), indhold (unit Antal)
tid range: 2014-01-01 to 2022-01-01
</table>
<table>
id: fapct
description: Folkeafstemninger efter valgresultat og tid
columns: valres, tid (time), indhold (unit Pct.)
tid range: 1971-01-01 to 2022-01-01
</table>
<table>
id: fabpct
description: Folkeafstemninger efter valgresultat og tid
columns: valres, tid (time), indhold (unit Antal)
tid range: 1971-01-01 to 2022-01-01
</table>
<table>
id: fa22tot
description: Folkeafstemning om Danmarks deltagelse i det europæiske samarbejde om sikkerhed og forsvar ved at afskaffe EU-forsvarsforbeholdet 2022 efter valgresultat, område og tid
columns: valres, omrade, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2022-01-01
</table>
<table>
id: fa22tota
description: Folkeafstemning om Danmarks deltagelse i det europæiske samarbejde om sikkerhed og forsvar ved at afskaffe EU-forsvarsforbeholdet 2022 efter valgresultat, område og tid
columns: valres, omrade, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2022-01-01
</table>
</fact tables>

notes:
- For regional breakdown by kommune: use fakom (99 kommuner via dim.nuts, 3 referendums: 2014, 2015, 2022).
- For the 2022 EU-forsvarsforbeholdet at finer election geography (storkredse/opstillingskredse): use fa22tot (106 areas). For polling station level: use fa22tota (1462 afstemningssteder).
- For long historical series (all referendums since 1971): use fabpct (national counts) or fapct (national percentages). Neither has geographic breakdown.
- All tables with Ja/Nej have aggregate valres codes (GYLD_IALT, UGYLD_IALT, etc.) that must be filtered out to avoid double-counting. Always select a specific valres — 434284=Ja, 434285=Nej, VAELG=vælgere.
- fa22tot and fa22tota cover the same 2022 referendum. fa22tot uses a custom election geography hierarchy (not NUTS) with integer codes; there is no dim table — use ColumnValues to browse omrade labels.
- Map: fakom supports choropleth at kommune level (/geo/kommuner.parquet). fa22tot supports storkredse choropleth (/geo/storkredse.parquet, omrade 10-19, subtract 9). fa22tota polling station codes do not match afstemningsomraader dagi_ids — no geo join available.