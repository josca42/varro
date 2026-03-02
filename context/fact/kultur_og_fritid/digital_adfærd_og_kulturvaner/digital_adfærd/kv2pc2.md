table: fact.kv2pc2
description: Forbrug af podcasts efter betaling, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- betaling: values [42960=Betaler for podcasts via podcasttjeneste, 42970=Betaler for podcasts på anden vis]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- kon='10' = køn i alt; alder='TOT' = alder i alt. Filter to these for national totals.
- betaling has only 2 values (via podcasttjeneste / på anden vis). These are NOT mutually exclusive — a listener can pay in both ways. Do not sum.
- 2024 data only. Note: this table covers paying podcast consumers only — non-listeners are not represented.
