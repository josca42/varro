table: fact.vnas3
description: Versionstabel NAS3 - 2.3 + 2.4.2 Korrigeret disponibel indkomst og faktisk forbrug (supplerende tabel) efter version, transaktion, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- version: values [V2024_JUN=Juniversion 2021-2024, V2024_MAR=Martsversion 2024, V2023_JUN=Juniversion 1966-2023 (Hovedrevision 2024), V2023_MAR=Martsversion 2023, V2022_SEP=Septemberversion 2021-2022 ... V2014_NOV=Novemberversion 2012-2014, V2014_JUN=Juniversion 2014, V2014_MAR=Martsversion 2014, V2013_NOV=Novemberversion 2011-2013, V2013_SEP=Septemberversion 1966-2013 (Hovedrevision 2014)]
- transakt: values [B6GK=B.6g Disponibel bruttoindkomst, D63K=D.63 Modt. Sociale overførsler i naturalier, D63D=D.63 Bet. Sociale overførsler i naturalier, D631D=D.631 Bet. Sociale overførsler i naturalier - ikke-markedsmæssig, D632D=D.632 Bet. Sociale overførsler i naturalier - købt markedsmæssig produktion, B7GD=B.7g Korrigeret disponibel bruttoindkomst, P51CD=P.51c Forbrug af fast realkapital, B7ND=B.7n Korrigeret disponibel nettoindkomst, D8K=D.8 Modt. Korrektion for ændringer i pensionsrettigheder, P4D=P.4 Faktisk forbrug, P41D=P.41 Faktisk individuelt forbrug, P42D=P.42 Offentlig kollektiv forbrugsudgift, B8GD=B.8g Bruttoopsparing]
- sektor: join dim.esa on sektor=kode [approx]
- tid: date range 1995-01-01 to 2024-01-01
dim docs: /dim/esa.md

notes:
- Version table of nas3. Same structure but adds a version dimension. Always filter WHERE version = 'V2024_JUN' (or the latest) unless comparing revisions. For current data use nas3.
- sektor: same dot-dropped ESA codes as nas3. Join dim.esa with REPLACE(d.kode, '.', ''). 9 sectors including S14, S15. Use ColumnValues("vnas3", "sektor") for labels.
- Covers adjusted disposable income and actual consumption (chapter 2.3 + 2.4.2) across multiple publication versions.