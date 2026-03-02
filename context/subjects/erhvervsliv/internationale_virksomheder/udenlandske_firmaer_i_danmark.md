<fact tables>
<table>
id: ifatsf10
description: Udenlandsk ejede firmaer efter branche, land, enhed og tid
columns: erhverv, land, enhed, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: ifatsf20
description: Udenlandsk ejede firmaer efter lande, enhed og tid
columns: lande, enhed, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- ifatsf10: use when you need breakdown by industry (erhverv) or ownership type (Danish vs. foreign). Has 8 industry groups + total. No country-of-origin detail.
- ifatsf20: use when you need breakdown by country of origin (which country owns the foreign firms). Has 5 individual countries (DE, NL, NO, SE, US), UK separately, EU27/EU27UK aggregate, and U1 (others). No industry breakdown.
- Both tables cover 2019–2023 and share the same three measures via enhed: ANTFIR (firm count), XOM (revenue mio. DKK), VAERK (FTE). Always filter enhed to one value.
- EU27 (2019) and EU27UK (2020–2023) in ifatsf20 represent the same aggregate concept — DST renamed it after Brexit. Time-series comparisons across this boundary should use EU27UK for 2020+ and EU27 for 2019.