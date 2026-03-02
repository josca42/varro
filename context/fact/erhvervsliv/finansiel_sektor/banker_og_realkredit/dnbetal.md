table: fact.dnbetal
description: Forudbestemte og betingede betalinger i relation til international likviditet efter egensektor, instrument, datatype, betalingsfrist og tid
measure: indhold (unit Mia. kr.)
columns:
- egensektor: join dim.esr_sekt on egensektor::text=kode [approx]
- instrument: values [FIN=Finansielle derivater, i alt, TOT=I alt, AND=Andre instrumenter end lån, værdipapirer og finansielle derivater (Kun sektor=1210), LIT=Lån og indskud i valuta, i alt (Kun sektor=1210), REP=Repoer og reverse repoer (Kun sektor=1210), STG=Statgaranterede enheders gæld (Kun sektor=1311), OBL=Værdipapirer, obligationer mv. i valuta (Kun sektor=1311)]
- data: values [B=Betingede betalinger, netto (Kun sektor= Statslig forvaltning), A=Forudbestemte indbetalinger, i alt, P=Forudbestemte indbetalinger, andet, E=Forudbestemte udbetalinger, afdrag, T=Forudbestemte udbetalinger, renter, W=Forudbestemte udbetalinger, andet]
- betalfrist: values [1=Op til en måned, 3=over 1 mnd og op til 3 mnd., 4=Mellem 3 og 12 måneder, A=Alle - ikke fordelt]
- tid: date range 1999-12-01 to 2025-09-01
dim docs: /dim/esr_sekt.md

notes:
- egensektor has only 2 values: 1210 (Centralbanker = Nationalbanken) and 1311 (Statslig forvaltning). These 4-digit codes do NOT join to dim.esr_sekt (which uses 2-digit codes). The dim link is incorrect; treat as inline values.
- instrument availability depends on egensektor: AND, LIT, REP apply only to sektor=1210 (Nationalbanken); STG, OBL apply only to sektor=1311 (Statslig forvaltning); FIN and TOT apply to both. Filter accordingly.
- data distinguishes payment type: A=predetermined inflows total, P=other predetermined inflows, E=amortization (outflow), T=interest (outflow), W=other outflows, B=conditional net payments (only for sektor=1311). These are not additive to each other in a simple way — consult egensektor and payment type context.
- betalfrist is a time-to-payment horizon: 1=≤1 month, 3=1-3 months, 4=3-12 months, A=all horizons (aggregate). Filter to betalfrist='A' for the total or pick a time horizon.
- Unit is mia. kr. (billions), not millions like most other tables in this subject.