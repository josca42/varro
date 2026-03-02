table: fact.bebrit11
description: Befolkningens internetkøb fordelt på internetforhandlere efter type, forhandlere og tid
measure: indhold (unit Pct.)
columns:
- type: values [10=I alt, 40=Alder: 16-19 år, 50=Alder: 20-39 år, 60=Alder: 40-59 år, 70=Alder: 60-74 år ... 210=Indkomst: 0-49.999 kr., 220=Indkomst: 50.000-99.999 kr., 230=Indkomst: 100.000-199.999 kr., 240=Indkomst: 200.000-299.999 kr., 250=Indkomst: 300.000 og derover]
- forhand: values [10=Danske internetforhandlere, 20=Internetforhandlere inden for EU, ikke danske, 30=Internetforhandlere uden for EU, 40=Ved ikke (Internetforhandlernes nationalitet er ukendt)]
- tid: date range 2008-01-01 to 2023-01-01
notes:
- type is a demographic selector: type='10' = national total. Never sum across type values.
- forhand values (retailer nationality) are NOT mutually exclusive — a person can buy from multiple retailer types in the same year. Do not sum across forhand values.
- Time series ends in 2023 — no 2024 or 2025 data.
- All values are percentages of the 16-74 year old population.
