table: fact.kv2mk6
description: Forbrug af koncerter efter spillestedets placering, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- spilplac: values [30390=I lokalområdet (din by eller din omegn), 30400=I Danmark uden for lokalområdet, 30410=I udlandet]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey percentages (single year 2024). spilplac values are NOT mutually exclusive — a respondent can attend concerts at multiple venue types. Sums exceed 100% (e.g. lokalområde 67% + Danmark udenfor 63% + udlandet 12% = 142%). Never sum across spilplac.
- kon='10' and alder='TOT' give the overall totals. Filter these when breaking down by gender/age.