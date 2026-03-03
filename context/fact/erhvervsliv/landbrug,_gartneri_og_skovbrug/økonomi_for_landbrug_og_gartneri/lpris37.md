table: fact.lpris37
description: Priser for landbrugsjord og forpagtning efter region, produkt, enhed og tid
measure: indhold (unit -)
columns:
- region: join dim.nuts on region=kode; levels [1]
- produkt: values [1695=Forpagtningsafgift (kr. pr. ha), 1705=Landbrugsjord, købspris (kr. pr. ha)]
- enhed: values [320=Løbende priser, 315=Ændring i forhold til året før (pct.)]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- region joins dim.nuts directly (both smallint). All fact codes are at niveau=1 (5 standard regions: 81–85). Code 0 = hele landet, not in dim — use WHERE region = 0 for national figure without joining.
- enhed is a measurement selector: 320=Løbende priser, 315=Ændring ift. året før (pct.). Always filter to ONE enhed.
- produkt only has 2 values: 1695=Forpagtningsafgift (kr. pr. ha), 1705=Landbrugsjord købspris (kr. pr. ha). These are different metrics — don't sum them.
- Annual frequency (2015–2024). The only table in this subject with regional land price breakdown.
- Map: /geo/regioner.parquet — merge on region=dim_kode (niveau 1, codes 81–85). Exclude region=0.
