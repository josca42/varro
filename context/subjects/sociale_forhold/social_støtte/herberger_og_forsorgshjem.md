<fact tables>
<table>
id: herfor2
description: Personer på herberger og forsorgshjem efter alder, ophold, køn og tid
columns: alerams, ophold2, kon, tid (time), indhold (unit Antal)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: herfor1
description: Personer på herberger og forsorgshjem efter alder, overnatning, køn og tid
columns: alerams, overnat, kon, tid (time), indhold (unit Antal)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: herfor3
description: Ophold på herberger og forsorgshjem efter overnatning, alder, køn og tid
columns: overnat, alerams, kon, tid (time), indhold (unit Antal)
tid range: 2021-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- The most important split: herfor1/herfor2 count PEOPLE; herfor3 counts STAYS. For "how many people stayed at a shelter?", use herfor1 or herfor2. For "how many stays lasted more than 120 days?", use herfor3. Mixing them up will give inflated person counts.
- herfor1 vs herfor2: same people, different cross-tabulation. herfor1 breaks down by duration of stay (overnat: 1 day → hele året). herfor2 breaks down by number of stays in the year (ophold2: 1 stay → 6+). Use herfor1 for duration questions, herfor2 for frequency-of-use questions.
- All three tables cover 2021–2024 (annual data), have the same age groups (18-24 through 60+), and use the same gender codes (kon: TOT/1/2).
- herfor1 and herfor2 have no TOT row for their categorical columns (alerams, overnat, ophold2). To get a total person count, SUM(indhold) WHERE kon='TOT'. herfor3 has TOT for both overnat and alerams — filter WHERE overnat='TOT' AND alerams='TOT' AND kon='TOT' for total stays.
- No regional breakdown in any of these tables. For regional homeless statistics, look elsewhere.