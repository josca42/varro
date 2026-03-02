table: fact.formue16
description: Formue efter percentil, prisenhed, alder og tid
measure: indhold (unit -)
columns:
- percentil: values [P1=Percentil 1, P2=Percentil 2, P3=Percentil 3, P4=Percentil 4, P5=Percentil 5 ... P95=Percentil 95, P96=Percentil 96, P97=Percentil 97, P98=Percentil 98, P99=Percentil 99]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- alder: values [1802=18 år og derover, 1829=18-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8089=80-89 år, 9099=90 år og derover]
- tid: date range 2020-01-01 to 2023-01-01

notes:
- indhold is the nettoformue threshold at each percentile (kr.), not a count. P50 is the median, P25 is lower quartile, P75 is upper quartile. Each percentile value is independent — never sum across percentiles.
- prisenhed must be filtered: 5=faste priser or 6=nominelle priser. Omitting doubles row counts.
- 99 percentiles (P1-P99) available. To reproduce the median from formue11: filter alder='1802', prisenhed=5, percentil='P50'.
- Shorter time series: 2020-2023 only.
- No gender, region, socio, origin, or family type breakdown. For those dimensions use formue11-14/17.
