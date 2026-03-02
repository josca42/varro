table: fact.bane401
description: National jernbanetransport af gods efter enhed, pålæsningsregion, aflæsningsregion og tid
measure: indhold (unit -)
columns:
- enhed: values [75=1000 ton, 76=Mio. tonkm]
- paregion: join dim.nuts on paregion=kode; levels [1]
- afregion: join dim.nuts on afregion=kode; levels [1]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- paregion and afregion both join dim.nuts. Only niveau=1 codes are used (the 5 Danish regions: 81 Nordjylland, 82 Midtjylland, 83 Syddanmark, 84 Hovedstaden, 85 Sjælland). No further geographic detail.
- Code 0 (I ALT = all regions) appears in both columns but is not in dim.nuts. An INNER JOIN silently excludes it, which is usually correct when you want the region-to-region matrix. To get national totals, filter WHERE paregion=0 AND afregion=0 instead.
- enhed is a measurement selector: 75=1000 ton, 76=Mio. tonkm. Always filter to one.
- This is an origin-destination matrix. Rows with paregion=0 OR afregion=0 are marginal totals (all-origin or all-destination), not additional shipments — do not sum them with the region-level rows.
- Use ColumnValues("nuts", "titel", for_table="bane401") to confirm which codes are present (only the 5 regions + aggregate 0).
- Annual data from 2007. National transport only — no international flow data in this table.
- Map: context/geo/regioner.parquet — merge on paregion=dim_kode (origin) or afregion=dim_kode (destination) for choropleth by region. Exclude paregion=0 / afregion=0 (marginal totals).