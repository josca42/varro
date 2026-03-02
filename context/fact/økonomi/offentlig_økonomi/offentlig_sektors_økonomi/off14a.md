table: fact.off14a
description: Offentlige virksomheder efter sektor, konto og tid
measure: indhold (unit Mio. kr.)
columns:
- sektor: values [2=2 Offentlig virksomhed i alt efter branche, 21=2.1 Landbrug, fiskeri, råstofindvinding og industri, 22=2.2 Energiforsyning, 23=2.3 Vandforsyning og spildevand, 24=2.4 Affaldsbehandling, 25=2.5 Bygge- og anlægsvirks. samt handel, hotel- og restaurationsvirks. mv., 26=2.6 Transportvirksomhed, post og telekommunikation, 27=2.7 Finansiering og forretningsservice mv.]
- konto: values [A1=A.1. Produktion, A2=A.2. Forbrug i produktion, A3=A.3. Bruttoværditilvækst (A.1-A.2), A4=A.4. Forbrug af fast realkapital, A5=A.5. Nettoværditilvækst (A.3-A.4) ... E6=E.6. Investeringer i forskning og udvikling, E7=E.7. Lagerændringer, E8=E.8. Køb af jord og rettigheder, netto, E9=E.9. Investeringstilskud og andre kapitaloverførsler, E10=E.10. Fordringserhvervelse, netto (E.4-(E.5+E.6+E.7+E.8+E.9))]
- tid: date range 1993-01-01 to 2023-01-01

notes:
- Subset of off14 — only sektor 2 (offentlig virksomhed i alt, =sum of 21–27) and sub-sectors 21–27 (enterprise branches). Do not sum sektor 2 with 21–27; sektor 2 is their aggregate.
- konto same structure as off14: lettered sections A–E with numbered items. Derived and aggregate rows are included; pick one.
- Annual (1993–2023).