table: fact.skib461
description: National godsomsætning på danske havne efter havn, retning, landsdel og tid
measure: indhold (unit 1.000 ton)
columns:
- havn: values [0=HAVNE I ALT, 1000=LANDSDEL BYEN KØBENHAVN, 25=Københavns Havn, 2000=LANDSDEL KØBENHAVNS OMEGN, 10=Avedøreværkets Havn ... 790=Skagen Havn, 720=Thisted Havn, 795=Vesterø Havn, 730=Aalborg Havn, 735=Aalborg Portland Havn]
- ret: values [1184=INDGÅENDE OG UDGÅENDE GODS I ALT, 1186=Indgående gods, 1188=Udgående gods]
- landdel: join dim.nuts on landdel=kode [approx]; levels [2]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- landdel joins dim.nuts niveau 2 (landsdele, codes 1–11) at 85% match. Two codes do NOT match dim.nuts: 0=Hele landet (national total), 888=Danske søområder (sea areas). Handle these separately or exclude from the join. For a clean join: JOIN dim.nuts d ON f.landdel=d.kode WHERE d.niveau=2 — this returns the 11 landsdele only.
- havn has the same aggregate/LANDSDEL structure as skib421/431/451. Filter to individual ports or havn='0'.
- ret: filter to one of 3 values (1184 total, 1186 indgående, 1188 udgående).
- Use ColumnValues("nuts", "titel", for_table="skib461") to see which landsdele codes appear in this table.
- Map: context/geo/landsdele.parquet — merge on landdel=dim_kode. Exclude landdel IN (0, 888).
