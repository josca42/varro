table: fact.bil62
description: Familiernes bilkøb (faktiske tal) efter købstype, familietype, købsmønster og tid
measure: indhold (unit Antal)
columns:
- koebtype: values [32=Nye biler (2007 - ), 31=Nye biler (1999 - 2006)]
- famtyp: values [FAIA=Familier i alt, FAUB=Familier uden børn, FAMB=Familier med børn, PAUB=Par uden børn, PAMB=Par med børn, PAFA=Parfamilier i alt, IHJB=Ikke-hjemmeboende børn, ENIA=Enlige i alt, ENUB=Enlige uden børn, ENMB=Enlige med børn]
- koebmoens: values [10000=Familier i alt, 10010=Familier der Ikke har købt bil i alt, 10020=Familier der har købt bil i alt, 10030=Familier der har købt 1 bil i alt, 10040=Familier der har købt personbil ... 10142=Familier der har købt 1 personbil og leaset 2 personbiler, 10144=Familier der har købt 2 varebiler og leaset 1 personbiler, 10146=Familier der har købt 1 varebil og leaset 2 personbiler, 10148=Familier der har købt 1 varebil, 1 personbil og leaset 1 personbil, 10149=Familier der har købt eller leaset mere end 3 biler]
- tid: date range 1999-01-01 to 2024-01-01
notes:
- koebtype splits the time series at a methodology break: 31=Nye biler (1999–2006), 32=Nye biler (2007–2024). The split is clean — each year has exactly one koebtype. For a long time series, UNION both: (... WHERE koebtype=31 AND tid<='2006-01-01') UNION ALL (... WHERE koebtype=32 AND tid>='2007-01-01'). Never filter to both koebtype in the same query without unioning — it causes overcounting.
- famtyp has a hierarchy: FAIA=alle familier i alt, then two mutually exclusive aggregates (PAFA=parfamilier, ENIA=enlige), each further split (PAFA→PAUB+PAMB, ENIA→ENUB+ENMB+IHJB). IHJB=ikke-hjemmeboende børn is an edge case sub-category. For a simple total use famtyp=FAIA.
- koebmoens same hierarchy as bil600: use 10020 for "bought car".
