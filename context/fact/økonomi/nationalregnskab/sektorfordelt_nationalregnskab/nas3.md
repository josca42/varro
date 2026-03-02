table: fact.nas3
description: 2.3 + 2.4.2 Korrigeret disponibel indkomst og faktisk forbrug (supplerende tabel) efter transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B6GK=B.6g Disponibel bruttoindkomst, D63K=D.63 Modt. Sociale overførsler i naturalier, D63D=D.63 Bet. Sociale overførsler i naturalier, D631D=D.631 Bet. Sociale overførsler i naturalier - ikke-markedsmæssig, D632D=D.632 Bet. Sociale overførsler i naturalier - købt markedsmæssig produktion, B7GD=B.7g Korrigeret disponibel bruttoindkomst, P51CD=P.51c Forbrug af fast realkapital, B7ND=B.7n Korrigeret disponibel nettoindkomst, D8K=D.8 Modt. Korrektion for ændringer i pensionsrettigheder, P4D=P.4 Faktisk forbrug, P41D=P.41 Faktisk individuelt forbrug, P42D=P.42 Offentlig kollektiv forbrugsudgift, B8GD=B.8g Bruttoopsparing]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- sektor codes drop the dot from ESA notation. Join dim.esa with: JOIN dim.esa d ON REPLACE(d.kode, '.', '') = f.sektor. 9 sectors: S11, S12, S13, S14, S15, S2, plus aggregates S1, S1M, S1W. Use ColumnValues("nas3", "sektor") for labels.
- Annual supplementary table for adjusted disposable income and actual consumption (chapter 2.3 + 2.4.2), 1995-2024. Quarterly equivalent: nks3 (1999+).
- Key transakt: B7GD=Korrigeret disponibel bruttoindkomst (adjusted for social transfers in kind), P4D=Faktisk forbrug. Use this table when you need actual consumption including government-provided services (e.g. healthcare, education) redistributed to households.