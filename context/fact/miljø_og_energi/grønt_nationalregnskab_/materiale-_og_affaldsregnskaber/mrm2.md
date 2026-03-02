table: fact.mrm2
description: Materialestrømsregnskab efter materialetype, indikator og tid
measure: indhold (unit Ton)
columns:
- mater: values [MFA0=I alt, MFA1=1 Biomasse, MFA11=1.1 Primære afgrøder og produkter heraf, MFA111=1.1.1 Korn, MFA112=1.1.2 Rodfrugter og rodknolde ... MFA4232=4.2.3.2 Vandtransport bunkring, MFA4233=4.2.3.3  Lufttransport bunkring, MFA43=4.3  Øvrige produkter hovedsagelig fra fossil energi, MFA5=5 Andre produkter, MFA6=6 Affald til endelig anvendelse og deponering]
- indikator: values [10=Dansk ressourceindvinding, 20=Import, 30=Direkte materialeinput, 40=Eksport, 50=Indenlandsk materialeanvendelse, 60=Fysisk handelsbalance]
- tid: date range 1993-01-01 to 2023-01-01
notes:
- indikator is a flow-type selector (6 values): 10=Dansk ressourceindvinding, 20=Import, 30=Direkte materialeinput, 40=Eksport, 50=Indenlandsk materialeanvendelse, 60=Fysisk handelsbalance. Always filter to one — summing across indicators is meaningless.
- mater has 73 hierarchical codes: MFA0=total, MFA1–MFA6=level-1 categories (Biomasse, Metalmalme, Ikke-metalliske mineraler, Fossil energi, Andre produkter, Affald), then sub-levels. Filter to a consistent level to avoid double-counting. For a top-level breakdown use MFA1–MFA6 (exclude MFA0). For totals only, use MFA0 and filter indikator.
- Longest time series in this subject: 1993–2023 (annual).
