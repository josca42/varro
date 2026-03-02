table: fact.bil63
description: Familiernes bilkøb (andele og fordelinger) efter enhed, familietype, købsmønster og tid
measure: indhold (unit Pct.)
columns:
- maengde4: values [50=Procentfordelingen, 60=Andel af det totale bilkøb]
- famtype: values [FAIA=Familier i alt, FAUB=Familier uden børn, FAMB=Familier med børn, PAUB=Par uden børn, PAMB=Par med børn, PAFA=Parfamilier i alt, IHJB=Ikke-hjemmeboende børn, ENIA=Enlige i alt, ENUB=Enlige uden børn, ENMB=Enlige med børn]
- koebmoens: values [10000=Familier i alt, 10010=Familier der Ikke har købt bil i alt, 10020=Familier der har købt bil i alt, 10030=Familier der har købt 1 bil i alt, 10040=Familier der har købt personbil ... 10142=Familier der har købt 1 personbil og leaset 2 personbiler, 10144=Familier der har købt 2 varebiler og leaset 1 personbiler, 10146=Familier der har købt 1 varebil og leaset 2 personbiler, 10148=Familier der har købt 1 varebil, 1 personbil og leaset 1 personbil, 10149=Familier der har købt eller leaset mere end 3 biler]
- tid: date range 1999-01-01 to 2024-01-01
notes:
- Note: the family type column is named `famtype` here (not `famtyp` as in bil62). Values are identical.
- maengde4 is a MEASUREMENT SELECTOR: always filter to 50 (within-family-type % distribution) OR 60 (share of all DK car purchases). Omitting this filter doubles every count silently.
- koebtype splits the series at 2006/2007 same as bil62 — but this table has Pct. values so "UNION" approach is for structure, not summing.
- famtype hierarchy same as bil62 (FAIA=total).
