<fact tables>
<table>
id: bane91
description: Dræbte og tilskadekomne ved jernbanetrafik efter banenet, personkategori, personskade og tid
columns: bane, pkategori, uheld, tid (time), indhold (unit Antal)
tid range: 1993-01-01 to 2024-01-01
</table>
<table>
id: bane92
description: Dræbte og tilskadekomne ved jernbanetrafik efter banenet, uheldstype, personskade og tid
columns: bane, utype, uheld, tid (time), indhold (unit Antal)
tid range: 2002-01-01 to 2024-01-01
</table>
<table>
id: skib95
description: Søulykker med danske skibe efter uheldstype, skibstype, omfang og tid
columns: utype, skibtype, omfang, tid (time), indhold (unit Antal)
tid range: 2014-01-01 to 2024-01-01
</table>
<table>
id: skib96
description: Søulykker i dansk farvand efter uheldstype, skibstype, omfang, registreringsland og tid
columns: utype, skibtype, omfang, reg, tid (time), indhold (unit Antal)
tid range: 2014-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Railway vs maritime: bane91/bane92 cover jernbane (train) accidents; skib95/skib96 cover maritime (ship) accidents. These are independent topics.
- bane91 vs bane92: both cover the same railway networks and time range but slice differently. bane91 breaks down by person category (passagerer, ansatte, andre); bane92 breaks down by accident type (kollision, afsporing, uheld i overskæring, etc.). bane91 goes back to 1993; bane92 only to 2002. Use bane91 for "who was affected", bane92 for "what happened".
- skib95 vs skib96: different scope. skib95 = accidents involving Danish-flagged ships (anywhere in the world). skib96 = accidents in Danish waters (all ship nationalities) with an added reg (registration country) dimension. For "accidents in Denmark's waters", use skib96. For "accidents involving Danish ships", use skib95.
- All four tables: use the aggregate code (bane=10010 or utype=0) to get totals; filter to specific codes for breakdowns. Never sum across both aggregate and sub-codes.
- bane91/bane92: uheld has only 2 values (Dræbte=1, Alvorligt tilskadekomne=2) — no aggregate. Sum them for total casualties.
- skib95/skib96: omfang (severity) has no aggregate — sum over all 4 values. skibtype also has no aggregate — sum all 6 to get totals.
- bane code 10120 (ANDRE BANER) is documented but absent from the actual data.