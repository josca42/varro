table: fact.dnsosb
description: Statsfinanser og -gæld, beholdninger efter instrument og tid
measure: indhold (unit Mia. kr.)
columns:
- instrument: values [2000.0=Bruttogæld - I alt, 2010.0=Bruttogæld - Fastforrentet, 2020.0=Bruttogæld - Variabelt forrentet, 2040.0=Bruttogæld - Restløbetid < 1 år, 2050.0=Bruttogæld - Restløbetid 1-2 år ... 2400.0=Statens indestående i Nationalbanken, 2500.0=Statslige fonde - I alt, 2510.0=Statslige fonde - Statspapirer, 2520.0=Statslige fonde - Andre papirer end statspapirer, 3000.0=Statsgæld - I alt]
- tid: date range 1990-12-01 to 2025-09-01
notes:
- Unit is Mia. kr. (billions), not Mio. kr. like most other tables in this subject.
- These are stock (beholdning) values — point-in-time positions at end of period, not flows.
- instrument: 37 codes with multiple aggregates. 2000.0=Bruttogæld I alt; 3000.0=Statsgæld I alt (a different concept). Codes have .0 float suffix. Sub-codes under 2000 (2010, 2020, 2040, ...) are breakdowns of bruttogæld — don't sum them with 2000.0.
- Monthly data (1990-12–2025-09). For transactions/flows, see dnsost.
