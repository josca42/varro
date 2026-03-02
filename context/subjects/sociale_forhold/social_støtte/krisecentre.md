<fact tables>
<table>
id: krise1
description: Ophold og beboere på krisecentre efter bopælsregion, varighed, beboerstatus og tid
columns: bopreg, kmdr, bebostat, tid (time), indhold (unit Antal)
tid range: 2017-01-01 to 2024-01-01
</table>
<table>
id: krise2
description: Ophold og beboere på krisecentre efter herkomst, varighed, beboerstatus og tid
columns: herkams, kmdr, bebostat, tid (time), indhold (unit Antal)
tid range: 2017-01-01 to 2024-01-01
</table>
<table>
id: krise3
description: Ophold og beboere på krisecentre efter alder, varighed, beboerstatus og tid
columns: alder1, kmdr, bebostat, tid (time), indhold (unit Antal)
tid range: 2017-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All three tables cover 2017–2024 and share the same bebostat and kmdr columns. The only difference is the breakdown dimension: krise1=bopælsregion, krise2=herkomst, krise3=alder. Pick the table that matches the breakdown needed.
- bebostat is a measurement selector present in all tables — not a category for summing. Values: 1=Ophold (stays/episodes), 2=Ophold med børn (stays with accompanying children), 3=Kvinder (adult women), 4=Børn (accompanying children), 35=Mænd (adult men, 2024 only), 38=Uoplyst køn (2024 only). Always filter to a single bebostat value.
- kmdr (varighed/duration) has a TOT aggregate and 6 mutually exclusive bands. Use kmdr='TOT' unless you need a breakdown by duration of stay.
- krise1 (region): bopreg has 5 NUTS niveau=1 regioner (81–85). bopreg=0 is the national total, bopreg=996 is uoplyst. Exclude bopreg='0' when summing across regions.
- Map: krise1 supports choropleth at region level via context/geo/regioner.parquet — merge on bopreg=dim_kode. krise2 and krise3 have no geographic dimension.
- krise2 (herkomst): herkams=T is the total; T, 7, 8, 0 — exclude T when summing.
- krise3 (alder): alder1=IALT is the total; exclude IALT when summing across age bands. Ages cover adults (18+) only for the main resident categories.