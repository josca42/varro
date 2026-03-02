<fact tables>
<table>
id: bts101
description: Modtagere af børnefamilieydelser og børnetilskud efter område, tilskudsart, køn, antal børn, enhed og tid
columns: omrade, tilskudsart, kon, antborn, enhed, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2024-10-01
</table>
<table>
id: bts102
description: Modtagere af børnefamilieydelser og børnetilskud efter tilskudsart, familietype, antal børn, enhed og tid
columns: tilskudsart, famtype, antborn, tal, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2024-10-01
</table>
</fact tables>

notes:
- For regional breakdown (by kommune): use bts101. It has omrade (98 kommuner via dim.nuts niveau 3), kon, and antborn. omrade=0 is the national total; omrade=997 is uoplyst.
- For family-type breakdown (enlige vs. par): use bts102. It has famtype (AFA/EMB/PMB/UBF) but no regional column.
- Both tables cover 2017–2024 (quarterly) and share the same tilskudsart and antborn coding.
- Both tables have a measurement selector that must always be filtered: bts101 uses enhed (105=antal, 120=gns. udbetaling), bts102 uses tal (30=antal familier, 35=gns. udbetaling, 40=andel i promille). Forgetting this filter silently multiplies counts.
- tilskudsart 1000 (Børneydelse) is the main universal benefit paid to virtually all families with children. The others are targeted supplements.
- Map: bts101 supports kommune-level choropleth maps via context/geo/kommuner.parquet (merge on omrade=dim_kode; exclude omrade IN (0, 997)).