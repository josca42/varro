<fact tables>
<table>
id: sygedp01
description: Sygedagpenge efter kommune, køn, alder, ydelsesmodtager, enhed og tid
columns: dffekom, koen, alerams, ydelsesmodtager, maengde6, tid (time), indhold (unit -)
tid range: 2020-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Only one table (sygedp01), covering 2020–2024 by kommune, køn, alder, and ydelsesmodtager type.
- maengde6 controls what is measured: 0=antal personer, 5=fuldtidspersoner, 10=antal dage, 15=beløb (tusind kr.), 20/25=delvist genoptaget arbejde variants. Always filter to one value — omitting it multiplies results by 6.
- Geography is at landsdel (niveau 2) or kommune (niveau 3) — no regional (niveau 1) breakdown. dffekom='0' is a national total not in dim.nuts.
- ydelsesmodtager distinguishes lønmodtagere (LR/LD), selvstændige, and ledige. TOT and LTOT are aggregates — don't sum across all values.
- Map: sygedp01 supports choropleth maps at kommune (niveau 3) via /geo/kommuner.parquet or landsdel (niveau 2) via /geo/landsdele.parquet — merge on dffekom=dim_kode.