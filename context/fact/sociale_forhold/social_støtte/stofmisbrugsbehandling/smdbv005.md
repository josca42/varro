table: fact.smdbv005
description: Stofmisbrugsbehandling efter myndighedskommune, afslutningsstatus og tid
measure: indhold (unit -)
columns:
- myndighedskom: join dim.nuts on myndighedskom=kode; levels [1, 3]
- afslutstatus: values [FRI=Stoffri (antal), REDSTAB=Reduceret og stabiliseret forbrug (antal), ANDANT=Andet (antal), FRIPCT=Stoffri (pct.), REDSTABPCT=Reduceret og stabiliseret forbrug (pct.), ANDPCT=Andet (pct.)]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- myndighedskom joins dim.nuts. niveau 1 = 5 regioner, niveau 3 = 98 kommuner. myndighedskom = '0' is national total (not in dim). Filter to one niveau to avoid double-counting.
- afslutstatus MIXES counts and percentages — never sum all values. Counts: FRI (stoffri), REDSTAB (reduceret/stabiliseret), ANDANT (andet). Percentages: FRIPCT, REDSTABPCT, ANDPCT. National avg 2024: FRI≈37%, REDSTAB≈16%, ANDET≈47%.
- The three count categories are mutually exclusive and sum to total completed treatments. The three pct categories sum to 100%.
- indhold unit is '-' (mixed). Always filter afslutstatus to one semantic group (counts OR percentages) per query.
- "Myndighedskommune" is the municipality responsible for the client, which may differ from where the treatment took place. Use omrade (smdbv001/smdbv002) for treatment location; myndighedskom here for responsible authority.
- Sample query — completion outcomes by municipality (2024, percentages): SELECT d.titel, f.afslutstatus, f.indhold FROM fact.smdbv005 f JOIN dim.nuts d ON f.myndighedskom = d.kode WHERE d.niveau = 3 AND f.afslutstatus IN ('FRIPCT','REDSTABPCT','ANDPCT') AND f.tid = '2024-01-01'
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on myndighedskom=dim_kode. Exclude myndighedskom=0.