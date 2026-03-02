table: fact.rme1
description: Materialestrømme opgjort i råstofækvivalenter efter råstoftype, indikator og tid
measure: indhold (unit 1.000 ton)
columns:
- rastoftype: values [MF0=I ALT, MF1=BIOMASSE, MF111=Korn, MF112=Rodfrugter og rodknolde, MF113=Sukkerafgrøder ... MF411=Brunkul, MF412=Kul, MF421=Råolie, kondensat og NGL, MF422=Naturgas mv., MF43=Anden fossil energi (tørv, olieskifer, tjæresand mv.)]
- indikator: values [10=1 Dansk ressourceindvinding (1), 20=2 Import (2), 30=3 Direkte materialeinputs råstofækvivalent (3)=(1+2), 40=4 Eksport (4), 50=5 Indenlandsk anvendelses råstofækvivalent (Ressourcefodaftryk) (5)=(3-4)]
- tid: date range 2008-01-01 to 2023-01-01
notes:
- indikator is a flow-type selector (5 values): 10=Dansk ressourceindvinding, 20=Import, 30=Direkte materialeinputs råstofækvivalent, 40=Eksport, 50=Indenlandsk anvendelses råstofækvivalent (Ressourcefodaftryk). Always filter to one.
- rastoftype has 31 hierarchical codes: MF0=total, MF1=Biomasse, MF2=Metalmalme, MF3=Ikke-metalliske mineraler, MF4=Fossil energi, then sub-levels (e.g. MF111=Korn, MF112=Rodfrugter). Filter to a consistent level. MF1–MF4 gives the 4 top categories.
- Values are in 1.000 ton (thousands of tonnes), not tonnes — note the unit when reporting.
- Measures resource footprint (råstofækvivalenter), not direct material flows. Shorter series than mrm2: 2008–2023.
