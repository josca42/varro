table: fact.byg62
description: Omkostningsindeks for anlæg efter indekstype, enhed og tid
measure: indhold (unit Indeks)
columns:
- indekstype: values [VEJARBEJD=Anlæg af veje, JORDARB=Jordarbejde, ASFALT=Asfaltarbejde, BETONVEJ=Betonkonstruktioner, JERNKONSTR=Jernkonstruktioner, DELINDEKS=Delindeks: Materiel og maskiner, DEL=Delindeks: Lastvognskørsel, DRIFT=Driftsindeks (2006 -)]
- tal: values [100=Indeks, 210=Ændring i forhold til kvartalet før (pct.), 310=Ændring i forhold til samme kvartal året før (pct.)]
- tid: date range 1986-07-01 to 2025-04-01

notes:
- `tal` is a measurement selector — every indekstype×tid combination appears three times (100=Indeks, 210=kvartal-over-kvartal pct, 310=år-over-år pct). Always filter to the `tal` value you need before reading indhold. Mixing `tal` values silently combines incompatible units.
- Quarterly frequency (months 1, 4, 7, 10). Longest time series in this subject group: back to 1986.
- `DRIFT=Driftsindeks (2006 -)` only has data from 2006. Other indekstype values go back to the full 1986 start.
- To get the simple index level for a single anlægstype: `WHERE tal = 100 AND indekstype = 'VEJARBEJD'` (or whichever type). No totals/aggregation needed — each indekstype is a standalone index.