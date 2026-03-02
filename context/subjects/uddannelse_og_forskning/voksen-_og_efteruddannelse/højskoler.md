<fact tables>
<table>
id: veuhoj11
description: Kursusdeltagelse i lange højskolekurser efter uddannelsesområde, alder, køn, institutionstype, tidsangivelse, enhed og tid
columns: fuddomr, alder, kon, insttyp, tidspunkter, overnat1, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: veuhoj21
description: Kursusdeltagelse i korte højskolekurser efter uddannelsesområde, alder, køn, institutionstype, tidsangivelse, enhed og tid
columns: fuddomr, alder, kon, insttyp, tidspunkter, overnat1, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: fohoj01
description: Antallet af højskolekursister efter kursustype, køn, alder, herkomst, enhed, tidsangivelse og tid
columns: kursus, kon, alder, herkomst, enhed, tidspunkter, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: fohoj02a
description: Antallet af højskolekursister på mellemlange og lange kurser efter køn, alder, højest fuldførte uddannelse i familien, enhed, tidsangivelse og tid
columns: kon, alder, hoej_udd_fam, enhed, tidspunkter, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: fohoj02b
description: Antallet af højskolekursister på mellemlange og lange kurser efter køn, alder, ækvivaleret disponibel indkomst i familien, enhed, tidsangivelse og tid
columns: kon, alder, aekvi_fam_indkomst, enhed, tidspunkter, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: fohoj03a
description: Antallet af højskolekursister på korte kurser efter køn, alder, højest fuldførte uddannelse, enhed, tidsangivelse og tid
columns: kon, alder, hfudd2, enhed, tidspunkter, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: fohoj03b
description: Antallet af højskolekursister på korte kurser efter køn, alder, personlig indkomst, enhed, tidsangivelse og tid
columns: kon, alder, pers_indk, enhed, tidspunkter, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: fohoj04
description: Antallet af højskolekursister efter kursustype, bopælsområde, køn, institution, enhed, tidsangivelse og tid
columns: kursus, bopland, kon, insti, enhed, tidspunkter, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All tables share the same measurement selector pattern: `enhed`/`overnat1` (11=Kursister, 13=Årselever) and `tidspunkter` (11=Kalenderår, 22=Skoleår). Failing to filter either one doubles all counts. Both columns are smallint — use integer literals.
- The fohoj* tables (2016–2024) are the newer series with richer demographic breakdowns (herkomst, education, income). The veuhoj* tables (2005/2011–2024) are the older series with education area (fuddomr) and institution type breakdowns. They cannot be directly compared.
- Course length split: veuhoj11=lange kurser, veuhoj21=korte kurser. For fohoj tables: fohoj02a/02b cover mellemlange+lange, fohoj03a/03b cover korte, fohoj01/fohoj04 cover all three types (with kursus column: 40=Kort, 50=Mellemlangt, 60=Langt).
- For geographic breakdown (by landsdel): only fohoj04 has bopland. No table has regional breakdown for veuhoj tables.
- For education area breakdown (fuddomr: folkehøjskole vs husholdningskurser etc.): use veuhoj11 (lange) or veuhoj21 (korte). fuddomr is hierarchical — do not mix levels.
- For herkomst (origin): only fohoj01.
- For socioeconomic context (education level, income): fohoj02a (family education, lange+mellemlange), fohoj02b (family income, lange+mellemlange), fohoj03a (own education, korte), fohoj03b (personal income, korte).
- 2024 data: for fohoj01 and fohoj04, only Skoleår (tidspunkter=22) is available in 2024. For Kalenderår, use 2023 or earlier.
- veuhoj11/21 alder total is `'0'`; fohoj01 alder total is `'0000'`; fohoj02a/02b/03a/03b alder total is `'TOT'`. Each table has its own alder coding scheme.
- Map: fohoj04 supports landsdel choropleth via context/geo/landsdele.parquet — merge on bopland=dim_kode (bopland 1–11, exclude 0 and 99). No other table has geographic breakdown.