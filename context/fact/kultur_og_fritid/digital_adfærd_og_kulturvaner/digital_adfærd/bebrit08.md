table: fact.bebrit08
description: Internetkøb inden for sidste år efter type, produkt og tid
measure: indhold (unit Pct.)
columns:
- type: values [10=I alt, 40=Alder: 16-19 år, 50=Alder: 20-39 år, 60=Alder: 40-59 år, 70=Alder: 60-74 år ... 210=Indkomst: 0-49.999 kr., 220=Indkomst: 50.000-99.999 kr., 230=Indkomst: 100.000-199.999 kr., 240=Indkomst: 200.000-299.999 kr., 250=Indkomst: 300.000 og derover]
- produkt: values [10=Rejseprodukter (2008), 102=Nyt internet-/teleabbonement , 20=Billetter til teater, koncerter mv, 30=Tøj, sport- og fritidsudstyr, 32=Sportsudstyr (dog undtaget sportstøj) ... 230=Abonnementer på el-, vand- eller varmeforsyning, dagrenovation eller lign., 240=Transporttjenester gennem en virksomhed, 250=Booket overnatning eller weekendophold gennem hotel eller rejsebureau, 260=E-bøger eller lydbøger som downloads, 120=Andet]
- tid: date range 2008-01-01 to 2025-01-01
notes:
- type is a demographic selector: type='10' = national total. Never sum across type values.
- produkt values are NOT mutually exclusive — respondents tick all product categories bought in the past year. Values sum to 323% for the total population. Each row is an independent % of population who bought that product type online. Never sum across produkt values.
- All values are percentages of the 16-74 year old population.
