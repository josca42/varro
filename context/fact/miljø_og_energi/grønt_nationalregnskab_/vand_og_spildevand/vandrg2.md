table: fact.vandrg2
description: Forbrug af vand (Fysiske vandregnskab) efter branche, vandtype og tid
measure: indhold (unit 1.000 m3)
columns:
- erhverv: join dim.nr_branche on erhverv=kode [approx: Strip V or E prefix from fact values; some aggregate codes like EHUSHOLD, ETOT not in dimension]
- vandtyp: values [VAFO=Forbrug af vand i alt, INDVA=Eget indvundet vand, INDGVA=Eget indvundet grundvand, INDOVA=Eget indvundet overfladevand, KOVA=Købt vand]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md

notes:
- The join documented as erhverv=kode is wrong. Correct join: REPLACE(REPLACE(f.erhverv, 'V', ''), '_', '-') = TRIM(d.kode). Same three transforms as other nr_branche tables: strip V prefix, replace _ with - for group codes, TRIM trailing space from dim.kode.
- EHUSHOLD (husholdninger) and ETOT (total) are aggregate codes not in dim.nr_branche — query them directly without joining.
- 5 hierarchy levels in dim (1–5); filter by d.niveau to avoid cross-level double-counting.
- vandtyp is hierarchical: VAFO = INDVA + KOVA (total = own abstraction + purchased). INDVA = INDGVA + INDOVA. Filter to one value.
- Covers water consumption (forbrug) not abstraction (indvinding). Use vandrg1 for abstraction, vandrg2 for consumption.
