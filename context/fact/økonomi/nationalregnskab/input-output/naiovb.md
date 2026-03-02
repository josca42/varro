table: fact.naiovb
description: Importkorrigerede vækstbidrag efter anvendelse og tid
measure: indhold (unit Procentpoint)
columns:
- anvendelse: values [AIAE=Endelig anvendelse i alt, ACP=Privat forbrug i alt, ACPA=A Fødevarer mv., ACPB=B Drikkevarer og tobak mv., ACPC=C Beklædning og fodtøj ... ABI5134=ICT udstyr, andre maskiner og inventar samt våbensystemer, ABI5170=Intellektuelle rettigheder mv., AL5253=Lagerforøgelser mv., AE6000=Eksport, A998CP=- Heraf turistindtægter mv.]
- tid: date range 2006-01-01 to 2024-01-01

notes:
- No dimension joins. The 31 `anvendelse` codes are self-contained final demand categories (e.g. AIAE=Endelig anvendelse i alt, ACP=Privat forbrug, ABI=Investeringer, AE6000=Eksport). Use ColumnValues("naiovb", "anvendelse") to see all.
- Values are percentage points (vækstbidrag = growth contributions). They are not additive across all categories — AIAE is the summary "endelig anvendelse" total; ACP/ABI/etc. are sub-components. Don't sum indiscriminately.
- No `prisenhed` column; values are already import-corrected volume growth contributions. Simple to query: just filter `anvendelse` to the category of interest.