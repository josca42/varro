table: fact.indkf201
description: Hovedtabel familieindkomster efter indkomsttype, familietype, population, prisenhed, enhed og tid
measure: indhold (unit -)
columns:
- indkomsttype: values [100=1 Disponibel indkomst (2+30-31-32-35), 105=2 Indkomst i alt, før skatter mv. (3+7+22+26+29), 110=3 Erhvervsindkomst (4+5+6), 115=4 Løn, 120=5 Virksomhedsoverskud ... 270=35 Betalt underholdsbidrag, 275=Ækvivaleret disponibel indkomst, 280=Ejendomsskat (grundskyld), boligejere, 285=Ejendomsskat (grundskyld), lejere, 290=Skattepligtig indkomst]
- famtyp: values [PAIAA=A. Par i alt, PAUB=Par uden børn, PAMB=Par med børn, ENIAA=B. Enlige i alt, ENUB=Enlige uden børn, ENMB=Enlige med børn, FAIAA=(A+B) Familier i alt, FAUBB=Familier uden børn, FAMBB=Familier med børn]
- popu: values [5000=Alle uanset om de har indkomstypen, 5010=Kun familier med indkomstypen]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 0=Løbende priser]
- enhed: values [50=Gennemsnit (kr.), 55=Median (kr.), 60=Nederste kvartilgræsnse (kr.), 65=Øverste kvartilgrænse (kr.), 100=Familier (Antal)]
- tid: date range 2004-01-01 to 2024-01-01
notes:
- Family-level headquarters table, parallel to indkp201 for persons. No geography — use indkf101/indkf104/indkf111/indkf112 for regional breakdowns.
- Three mandatory selectors: enhed (5 types), popu (alle vs. kun familier med indkomsttypen), prisenhed (faste vs. løbende). CAUTION: prisenhed coding differs from indkp201 — here 0=løbende priser (not nominelle) and 5=faste priser.
- indkomsttype is hierarchical (35+ types) using the same 100-290 series as person tables. Never sum across types.
- famtyp totals: FAIAA=familier i alt. PAIAA=par i alt, ENIAA=enlige i alt.
- enhed=100 gives family count (Antal); enhed=50/55/60/65 give kr-statistics.
- Only goes back to 2004. For earlier family counts by area use indkf11a.
