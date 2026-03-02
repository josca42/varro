table: fact.handbu02
description: Handicapindsatser til børn og unge mellem 0-17 år efter kommune, indsats, alder og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [3]
- indsatser: values [100=Handicapindsatser i alt, 110=Børn og unge der modtager handicapindsatser i alt]
- alder: values [IALT=Alder i alt, 0005=0-5 år, 0611=6-11 år, 1217=12-17 år, 999=Uoplyst alder]
- tid: date range 2022-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- kommunedk joins dim.nuts at niveau=3 (95 kommuner). kommunedk=0 is a national total not in dim.nuts.
- indsatser has 2 values: 100=total interventions, 110=unique children. Never sum 100+110. Use 110 for headcounts.
- alder has IALT as a total row — do not sum across all alder values (IALT + 0005 + 0611 + 1217 + 999 would double-count). Filter to alder='IALT' for totals, or SUM only the individual bands (0005, 0611, 1217) and handle 999=uoplyst separately.
- Map: context/geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.
