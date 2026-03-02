table: fact.turist3
description: Hoteller og feriecentre efter certificering, kapacitet og tid
measure: indhold (unit Antal)
columns:
- cert: values [TOT=Hoteller og feriecentre i alt, 1=Hoteller og feriecentre med Green key-certificering, 2=Hoteller og feriecentre uden Green key-certificering]
- kapacitet: values [1080=Hoteller og feriecentre (antal), 1082=Udlejede værelser (antal), 1084=Overnatninger (antal), 1090=Værelser (antal), 1100=Senge (antal), 1110=Værelser (kapacitetsudnyttelse, pct.), 1120=Senge (kapacitetsudnyttelse, pct.)]
- tid: date range 2019-01-01 to 2024-12-01

notes:
- tid appears monthly (ends 2024-12-01) but data is only available from 2019. National level only — no omrade column.
- cert has 3 values: TOT (total), 1 (Green Key certified), 2 (not certified). For the sustainability share: compare cert=1 to cert='TOT'. The two non-TOT values are mutually exclusive and sum to TOT.
- kapacitet is a measurement selector — always filter to one value. Same 7 metrics as hotel31: 1080=antal hoteller/feriecentre, 1082=udlejede værelser, 1084=overnatninger, 1090=antal værelser, 1100=antal senge, 1110=værelsesbel. pct., 1120=sengebel. pct. Never SUM across kapacitet.
- This is the only table in the subject with Green Key certification data. Use it for sustainability/environmental certification questions.