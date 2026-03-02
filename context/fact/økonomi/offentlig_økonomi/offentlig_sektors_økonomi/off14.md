table: fact.off14
description: Den offentlige sektors finanser efter sektor, konto og tid
measure: indhold (unit Mio. kr.)
columns:
- sektor: values [1=1 Den offentlige sektor i alt., 11=1.1 Offentlig forvaltning og service, 12=1.2 Offentlige selskabslign. virksomheder, 13=1.3 Offentlige selskaber, 2=2 Offentlig virksomhed i alt efter branche, 21=2.1 Landbrug, fiskeri, råstofindvinding og industri, 22=2.2 Energiforsyning, 23=2.3 Vandforsyning og spildevand, 24=2.4 Affaldsbehandling, 25=2.5 Bygge- og anlægsvirks. samt handel, hotel- og restaurationsvirks. mv., 26=2.6 Transportvirksomhed, post og telekommunikation, 27=2.7 Finansiering og forretningsservice mv.]
- konto: values [A1=A.1. Produktion, A2=A.2. Forbrug i produktion, A3=A.3. Bruttoværditilvækst (A.1-A.2), A4=A.4. Forbrug af fast realkapital, A5=A.5. Nettoværditilvækst (A.3-A.4) ... E6=E.6. Investeringer i forskning og udvikling, E7=E.7. Lagerændringer, E8=E.8. Køb af jord og rettigheder, netto, E9=E.9. Investeringstilskud og andre kapitaloverførsler, E10=E.10. Fordringserhvervelse, netto (E.4-(E.5+E.6+E.7+E.8+E.9))]
- tid: date range 1993-01-01 to 2023-01-01

notes:
- sektor is hierarchical: 1=all public sector, 11=offentlig forvaltning og service, 12=selskabslign. virksomheder, 13=selskaber (11+12+13 ≈ 1's public admin portion); 2=all public enterprises (=sum of 21–27), 21–27=enterprise branches by industry. Never sum sektor 1+2 or 1+11+12+13+2+21...27 etc.
- konto has lettered sections (A=production account, B=income distribution, C=secondary income, D=use of income, E=capital account) with numbered items within each section. konto A3=BVT is a derived row (=A1-A2). E10=Fordringserhvervelse netto is the bottom-line capital account balance. Summing all konto codes is meaningless — pick the account you need.
- Annual (1993–2023). For public enterprises only, see off14a.