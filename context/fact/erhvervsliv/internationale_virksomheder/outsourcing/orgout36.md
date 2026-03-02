table: fact.orgout36
description: Firmaers international outsourcing efter destination efter funktioner, destination og tid
measure: indhold (unit Antal)
columns:
- funktioner: values [CTOT=Funktioner i alt, CBF=Kernefunktioner, SBF=Hjælpefunktioner]
- destina: values [SINT=International outsourcing i alt, EU272020=EU27 (2020), OEU=Europa udenfor EU, CH=Kina, IN=Indien, USCA=USA og Canada, OL=Øvrige lande]
- tid: date range 2009 to 2024

notes:
- tid is int4range (survey waves). Filter with: WHERE tid = '[2021,2024)'::int4range for the most recent wave.
- destina: counts overlap — a firm can outsource to multiple destinations, so individual destinations sum to more than SINT (e.g. in [2021,2024): EU272020=398 + OEU=140 + ... = 824 > SINT=428). SINT is the correct total. Never sum across destination values.
- funktioner: same CTOT/CBF/SBF hierarchy as orgout11. CTOT ≠ CBF+SBF (firms can outsource both function types).