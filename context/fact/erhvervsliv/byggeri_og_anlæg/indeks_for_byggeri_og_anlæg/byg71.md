table: fact.byg71
description: Omkostningsindeks for anlæg efter indekstype, enhed og tid
measure: indhold (unit -)
columns:
- indekstype: values [VEJARBEJD=Anlæg af veje, JORDARB=Jordarbejde, ASFALT=Asfaltarbejde, BETONKONSTR=Betonkonstruktioner, JERNKONSTR=Jernkonstruktioner, DELINDEKS=Delindeks: Materiel og maskiner, DEL=Delindeks: Lastvognskørsel, DRIFT=Driftsindeks (2006 -)]
- tal: values [100=Indeks, 315=Ændring i forhold til året før (pct.)]
- tid: date range 1987-01-01 to 2024-01-01

notes:
- `tal` is a measurement selector — every indekstype×tid combination appears twice (100=Indeks, 315=år-over-år pct). Always filter to `tal = 100` or `tal = 315`.
- Annual frequency (month 1 only). This is the annual companion to byg62 (quarterly). Use byg62 if quarterly granularity is needed; byg71 for cleaner annual series.
- Note one naming difference from byg62: byg71 uses `BETONKONSTR` while byg62 uses `BETONVEJ` for the concrete code. Both refer to Betonkonstruktioner.
- Data ends 2024; use byg62 for more recent observations.