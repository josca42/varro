table: fact.dnifubal
description: Investeringsfondenes ultimobalance efter balancepost, investeringsfondstype og tid
measure: indhold (unit Mio. kr.)
columns:
- balpostnat1: values [AA98=Aktiv: Indskud, AV00=Aktiv: Obligationer, AA00=Aktiv: Aktier, AI00=Aktiv: Andele i investeringsfonde, AA97=Aktiv: Finansielle derivater, AA96=Aktiv: Øvrige, PP98=Passiv: Lån, PV00=Passiv: Investorernes formue, PP97=Passiv: Finansielle derivater, PP96=Passiv: Øvrige]
- investfond: values [XX=Total, AIF=Kapitalforeninger (AIF), UCITS=Investeringsforeninger (UCITS)]
- tid: date range 2018-01-01 to 2025-09-01

notes:
- investfond has XX=Total, AIF=Kapitalforeninger, UCITS=Investeringsforeninger. Filter to one type or use XX for the combined total. Forgetting this triples counts.
- balpostnat1 has 10 individual balance sheet line items — no aggregate total row. Aktiver: AA98 (Indskud), AV00 (Obligationer), AA00 (Aktier), AI00 (Andele i investeringsfonde), AA97 (Finansielle derivater), AA96 (Øvrige). Passiver: PP98 (Lån), PV00 (Investorernes formue), PP97 (Finansielle derivater), PP96 (Øvrige). To compute total aktiver or total passiver, SUM the relevant prefix group in SQL.
- Typical query: filter investfond to desired type, pick one or more balpostnat1 items, and aggregate over tid.