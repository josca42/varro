<fact tables>
<table>
id: strafna3
description: Skyldige personer efter køn, alder, oprindelsesland og tid
columns: koen, alder, ieland, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: strfsoc1
description: Skyldige personer efter køn, alder, socioøkonomisk status og tid
columns: koen, alder, socio, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: strfudd1
description: Skyldige personer i alderen 15-79 år efter køn, alder, uddannelse og tid
columns: koen, alder, uddannelse, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: strfudd2
description: Skyldige personer i alderen 15-79 år efter overtrædelsens art, uddannelse og tid
columns: overtraed, uddannelse, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: strafna4
description: Skyldige personer efter overtrædelsens art, oprindelsesland og tid
columns: overtraed, ieland, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: strfsoc2
description: Skyldige personer efter overtrædelsens art, socioøkonomisk status og tid
columns: overtraed, socio, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: strafna5
description: Skyldige personer efter oprindelsesland, afgørelsestype og tid
columns: ieland, afgorelse, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: strafna6
description: Skyldige personer efter område, køn, alder, national oprindelse og tid
columns: omrade, kon, alder, herkomst1, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2023-01-01
</table>
<table>
id: strafna7
description: Skyldige personer efter område, overtrædelsens art og tid
columns: omrade, overtraed, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2023-01-01
</table>
<table>
id: strafna8
description: Skyldige personer efter område, afgørelsestype og tid
columns: omrade, afgorelse, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2023-01-01
</table>
<table>
id: strafna9
description: Skyldige personer efter køn, alder, herkomst og tid
columns: koen, alder, herkomst, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: strfna10
description: Skyldige personer efter overtrædelsens art, herkomst og tid
columns: overtraed, herkomst, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: strfna11
description: Skyldige personer efter afgørelsestype, herkomst og tid
columns: afgorelse, herkomst, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: strfna12
description: Skyldige personer efter køn, alder, herkomst, statsborgerskab og tid
columns: koen, alder, herkomst, statsb, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2023-01-01
</table>
<table>
id: strfna13
description: Skyldige personer efter statsborgerskab, overtrædelsens art og tid
columns: statsb, overtraed, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2023-01-01
</table>
<table>
id: strfna14
description: Skyldige personer efter statsborgerskab, herkomst, afgørelsestype og tid
columns: statsb, herkomst, afgorelse, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2023-01-01
</table>
</fact tables>
notes:
- All tables measure "skyldige personer" (convicted persons) per year — counts of people, not offences.
- Time coverage varies: strafna3/4/5/9/strfna10/11 from 2000, strafna6/7/8 from 2005, strfsoc1/2/strfudd1/2 from 2015, strfna12/13/14 from 2018. For long time series on origin/herkomst, use strafna9 (2000–).

By breakdown dimension:
- By age + gender: strafna3 (+ country of origin), strafna9 (+ herkomst), strfsoc1 (+ socio), strfudd1 (+ education), strfna12 (+ herkomst + statsb, from 2018)
- By region (omrade): strafna6 (+ gender/age/herkomst1), strafna7 (+ crime type), strafna8 (+ verdict)
- By crime type (overtraed): strfudd2, strafna4, strfsoc2, strafna7, strfna10, strfna13 — ALL cover Straffelov ONLY, not Færdselslov or Særlov
- By verdict (afgorelse): strafna5 (+ country), strafna8 (+ region), strfna11 (+ herkomst), strfna14 (+ statsb + herkomst). NOTE: strfna14 uses a different afgorelse coding (800-series) than the others (11/12/2/3/4/5/511).

Origin/nationality dimensions — three different columns used across tables:
- ieland (country of origin): strafna3/4/5 — ~50 individual countries + aggregate codes (0=I alt, 7100/7200/7300)
- herkomst (origin category): strafna9/strfna10/strfna11 use {TOT, 1, 21, 24, 25, 31, 34, 35} with a 2-level hierarchy (21=24+25, 31=34+35); strfna12/strfna14 use a simplified {3, 4, 5} with no total
- statsb (citizenship): strfna12/strfna13/strfna14 — DANSK/VEST/IKKEVEST

Shared gotchas:
- overtraed tables have BOTH niveau 1 ("Straffelov") and niveau 3 subcategories as separate rows — always filter by niveau when joining dim.overtraedtype or you double-count.
- omrade (nuts) tables include code 0 (I alt) which is not in dim.nuts — filter to niveau 1 or 3.
- herkomst (in strafna9/strfna10/strfna11) is hierarchical — 21=Indvandrere i alt includes 24+25; 31=Efterkommere i alt includes 34+35. Pick one hierarchy level.
- Most tables have koen=M/K only (no total). strfna12 is the exception with koen=TOT.
- socio (strfsoc1/strfsoc2) uses a simplified custom coding (not SOCIO13). Treat as inline values, not a dim join.
- Map: strafna6, strafna7, strafna8 have omrade (dim.nuts niveau 1/3) and support choropleth maps via /geo/regioner.parquet or /geo/kommuner.parquet. Kommune-level data can also be aggregated to 12 politikredse via dim.politikredse — use /geo/politikredse.parquet.
