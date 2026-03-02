table: fact.bdf11
description: Bedrifter efter område, enhed, bedriftstype, areal og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2]
- tal: values [ANTAL=Bedrifter (antal), AREAL=Samlet dyrket areal (ha)]
- bedrift: values [B10=Alle bedrifter, B15=Bedrifter, korn og industrifrø, B30=Bedrifter, agerbrug i øvrigt, B31=Bedrifter, gartneri og væksthus, B32=Bedrifter, gartneri og friland, B33=Bedrifter, frugttræer og planteskole, B34=Bedrifter, blandet gartneri, B41=Bedrifter, malkekvæg, B42=Bedrifter, kvæg opdræt/fedning, B49=Bedrifter, grovfoderædende husdyr i øvrigt, B50=Svinebedrifter, B52=Bedrifter med fjerkræ, B54=Bedrifter, pelsdyr, B58=Bedrifter, blandede husdyrhold, B60=Øvrige bedrifter]
- areal1: values [AIALT=I alt, A00=Uden dyrket areal, A5=0,1 - 4,9 ha, A10=5,0 - 9,9 ha, A15=10,0 - 14,9 ha ... A200=175,0 - 199,9 ha, A250=200,0 - 249,9 ha, A300=250,0 - 299,9 ha, A400=300,0 - 399,9 ha, A500=400,0 ha og derover]
- tid: date range 2010-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts using plain integer codes (no zero-padding). niveau 1 (81-85 = 5 regioner), niveau 2 (4=Bornholm, 7=Fyn, 8=Sydjylland, 9=Østjylland, 10=Vestjylland). Code 0 = Hele landet and 15 = unmatched custom agricultural aggregate (likely Sjælland og øerne) — neither is in dim.nuts. Not all 11 standard landsdele are present; only 5 are reported at niveau 2.
- tal is a measure-type selector: ANTAL (bedrifter count) or AREAL (ha). Always filter to one. Mixing them produces nonsense sums.
- bedrift is the farm-type filter: B10=Alle bedrifter, B15-B60 are specific types. Filter to B10 for totals. Specific types are NOT mutually exclusive (one farm can appear in multiple) — sum only over B10 or a single type.
- areal1 contains AIALT (total across all sizes) plus size brackets. Filter to AIALT unless you want a specific size class.
- To get total farm counts nationally by farm type: WHERE tal='ANTAL' AND areal1='AIALT' AND omrade=0 AND bedrift='B10'. Each of these 4 filters is required to avoid overcounting.
- Map: context/geo/regioner.parquet (niveau 1, omrade 81-85) or context/geo/landsdele.parquet (niveau 2, omrade 4,7,8,9,10 — 5 of 11 landsdele only) — merge on omrade=dim_kode. Exclude omrade IN (0, 15).