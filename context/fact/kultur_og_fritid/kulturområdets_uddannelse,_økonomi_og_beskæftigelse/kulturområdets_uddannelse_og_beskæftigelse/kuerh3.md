table: fact.kuerh3
description: Kulturarbejdssteder (ultimo november) efter kulturemne, aktivitet, størrelse og tid
measure: indhold (unit Antal)
columns:
- kulturemne: values [0=Alle kulturemner, 9=Fornøjelses- og temaparker, 10=Idræt, 11=Spil og lotteri, 13=Arkiver ... 26=Design, 27=Fotografering, 28=Kunsthåndværk, 30=Reklame, 33=Anden/tværgående kultur]
- aktivi: values [TOT=Alle aktiviteter, 0=Kerneaktivitet, 1=Støtteaktivitet]
- storrelse: values [20=0 beskæftigede, 21=1 beskæftiget, 22=2-4 beskæftigede, 23=5-9 beskæftigede, 24=10-19 beskæftigede, 25=20-49 beskæftigede, 26=50 beskæftigede og derover]
- tid: date range 2008-01-01 to 2023-01-01

notes:
- storrelse has 7 mutually exclusive size categories with no total row. Sum across all 7 for total workplace count.
- aktivi=TOT is the aggregate; do NOT add TOT to 0 or 1 — that triples the count.
- kulturemne=0 is total. Numeric kulturemne codes cannot be joined to dim.kulturemner directly. Use inline values from columns doc.
- Measures only workplace count (Antal), not employment or wages — use kuerh1 for those measures.