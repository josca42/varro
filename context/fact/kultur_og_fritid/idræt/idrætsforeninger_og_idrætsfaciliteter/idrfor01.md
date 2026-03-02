table: fact.idrfor01
description: Idrætsforeninger og medlemmer efter område, organisation, nøgletal og tid
measure: indhold (unit Antal)
columns:
- blstkom: join dim.nuts on blstkom=kode [approx]; levels [2, 3]
- organisation: values [100=I alt, 101=DIF - Danmarks Idrætsforbund, 102=DGI, 103=Dansk Firmaidrætsforbund]
- aktp: values [104=Foreninger, 105=Medlemmer]
- tid: date range 2014-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- aktp selects the measure type: 104=Foreninger (number of clubs), 105=Medlemmer (number of members). Always filter to one aktp value — these are two separate metrics, not a dimension to sum over.
- organisation=100 is NOT the sum of 101+102+103. Clubs and members can belong to multiple organisations simultaneously (e.g. a club in both DIF and DGI), so summing orgs double-counts. Use organisation=100 for the deduplicated national total.
- blstkom joins dim.nuts at niveaus 2 (11 landsdele) and 3 (98 kommuner). Filter d.niveau to avoid mixing levels. blstkom=0 is the national total; blstkom=99 is unknown/unspecified municipality — exclude it for geographic analysis.
- Example: total members by landsdel for latest year: JOIN dim.nuts ON blstkom=kode AND niveau=2, filter organisation=100 (I alt) and aktp=105.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/landsdele.parquet (niveau 2) — merge on blstkom=dim_kode. Exclude blstkom IN (0, 99).