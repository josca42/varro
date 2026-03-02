table: fact.kv2mk4
description: Forbrug af musik efter oprindelsesland, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- oprindland: values [42070=Lytter mest til danske bands, orkestre eller kunstnere, 42080=Lytter mest til udenlandske bands, orkestre eller kunstnere, 42090=Lytter cirka lige meget til danske og udenlandske bands, orkestre eller kunstnere]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Single survey year (2024) — no time series.
- indhold is a percentage (Pct.). oprindland categories are mutually exclusive (sum to exactly 100 for any kon/alder): respondents pick one preference. Safe to read as a distribution.
- Only 3 values: 42070 (mostly Danish, 10%), 42080 (mostly foreign, 32%), 42090 (about equal, 58%). The "about equal" category dominates.
- Filter to kon=10 AND alder='TOT' for population totals.