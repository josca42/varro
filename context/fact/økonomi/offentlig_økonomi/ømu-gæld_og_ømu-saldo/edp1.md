table: fact.edp1
description: Offentligt underskud og gæld i EU-landene efter land, funktion, enhed og tid
measure: indhold (unit -)
columns:
- land: join dim.lande_uht_bb on land=kode [approx]; levels [2, 4]
- funktion: values [SALDO=Offentligt overskud(+)/underskud(-) (ØMU-saldo), GAELD=Offentlig bruttogæld (ØMU-gæld)]
- enhed: values [EUR=Mio. Euro (løbende priser), DKK=Mio. DKK (løbende priser, kun for Danmark), PCT=I % af BNP]
- tid: date range 2000-01-01 to 2024-01-01
dim docs: /dim/lande_uht_bb.md

notes:
- enhed is a measurement-selector column: EUR, DKK, PCT. Every (land, funktion, tid) combo is repeated for each applicable unit. Always filter to one enhed or you'll multiply counts. DKK is only available for land='DK' — all other countries have only EUR and PCT.
- funktion distinguishes two independent measures: SALDO (offentligt overskud/underskud) and GAELD (offentlig bruttogæld). Always filter to one value.
- land joins dim.lande_uht_bb but two codes are unmatched: 'DK' (Danmark, not in the dim) and 'I9' (EU total aggregate, also not in the dim). The matched codes split across niveau 2 (B6 = EU-27 uden UK) and niveau 4 (27 individual EU member states). Filter d.niveau=4 for country-level comparison; use B6 directly for EU-27 aggregate. I9 is a separate EU total (not decomposable via the dim hierarchy).
- For a cross-country comparison (e.g. GAELD as % of GDP for all EU members in 2024): filter funktion='GAELD', enhed='PCT', land NOT IN ('B6','I9'), join dim.lande_uht_bb on land=kode WHERE niveau=4. This gives exactly 27 rows.
- Use ColumnValues("lande_uht_bb", "titel", for_table="edp1") to browse the 27 matched country names. Note that DK and I9 will not appear in that result — reference them by code directly.