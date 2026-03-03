<fact tables>
<table>
id: bost63
description: Boligstøtte efter område, ydelsestype, måned, enhed og tid
columns: omrade, ydelsestype, mnd, enhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: bost64
description: Boligstøtte efter alder, ydelsestype, måned, enhed og tid
columns: alder, ydelsestype, mnd, enhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- bost63 = regional breakdown (99 kommuner via dim.nuts niveau 3); bost64 = age-group breakdown (14 groups, 18+). Same time range (2007–2024), same ydelsestype and enhed structure.
- Both tables cover the same three benefit types: Boligsikring (for ordinary tenants/co-owners/owners), Boligtillæg for Førtidspensionister, and Boligydelse (for pensioners). Use ydelsestype='1000' for all types combined.
- enhed is a measurement selector present in both tables — always filter to one: 3000=antal modtagerhusstande, 3010–3040=payment amount statistics (mean, lower quartile, median, upper quartile). Forgetting this silently multiplies counts by 5.
- ydelsestype is hierarchical in both tables: 1000 (total) > 1010/1060/1120 (benefit-type aggregates) > individual subtypes by housing form. Pick one level and don't sum across it.
- mnd (month 1–12) must always be filtered — these are stock figures per month, not flows.
- Neither table has gender breakdown. For questions combining geography and age, these tables must be used separately (no single table has both dimensions).
- Map: bost63 supports choropleth maps at kommune level via /geo/kommuner.parquet (merge on omrade=dim_kode, exclude omrade=0). bost64 has no geographic dimension.