table: fact.nks3
description: 2.3 + 2.4.2 Korrigeret disponibel indkomst og faktisk forbrug (supplerende tabel) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B6GK=B.6g Disponibel bruttoindkomst, D63K=D.63 Modt. Sociale overførsler i naturalier, D63D=D.63 Bet. Sociale overførsler i naturalier, D631D=D.631 Bet. Sociale overførsler i naturalier - ikke-markedsmæssig, D632D=D.632 Bet. Sociale overførsler i naturalier - købt markedsmæssig produktion, B7GD=B.7g Korrigeret disponibel bruttoindkomst, P51CD=P.51c Forbrug af fast realkapital, B7ND=B.7n Korrigeret disponibel nettoindkomst, D8K=D.8 Modt. Korrektion for ændringer i pensionsrettigheder, P4D=P.4 Faktisk forbrug, P41D=P.41 Faktisk individuelt forbrug, P42D=P.42 Offentlig kollektiv forbrugsudgift, B8GD=B.8g Bruttoopsparing]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1999-01-01 to 2025-04-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. Sectors: S1, S11, S12, S13, S1M, S1W, S2 (no individual S14/S15). Aggregates have no dim.esa entry — use ColumnValues("nks3", "sektor") for labels.
- Quarterly supplementary table for adjusted disposable income and actual consumption (chapter 2.3 + 2.4.2). Quarterly data 1999Q1–2025Q1. Annual equivalent: nas3 (1995-2024).
- Key transakt: B7GD=Korrigeret disponibel bruttoindkomst, P4D=Faktisk forbrug (which includes social transfers in kind from government to households).