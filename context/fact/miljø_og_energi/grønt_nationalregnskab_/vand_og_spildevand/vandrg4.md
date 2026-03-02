table: fact.vandrg4
description: Udledning af spildevand (Fysiske vandregnskab) efter branche, udledning og tid
measure: indhold (unit 1.000 m3)
columns:
- erhverv: join dim.nr_branche on REPLACE(erhverv, 'V', '')=kode::text [approx: Industry codes prefixed with V (e.g., V01000 -> 01000). Aggregate codes like ETOT, EHUSHOLD, EV, VA not in dimension.]
- udl: values [UDLTOT=Udledning af spildevand i alt, UDLREC=Egen udledning til recipient, UDLSPI=Udledning til spildevandssystem]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md

notes:
- erhverv joins dim.nr_branche using: REPLACE(REPLACE(f.erhverv, 'V', ''), '_', '-') = TRIM(d.kode). EHUSHOLD and ETOT are aggregate codes not in the dim.
- udl is hierarchical: UDLTOT = UDLREC + UDLSPI. Filter to one value to avoid double-counting.
- 5 hierarchy levels in dim (1–5); filter by d.niveau to pick granularity and avoid cross-level double-counting.
- Industry breakdown for wastewater discharge volumes. Companion to vandud (which has regional breakdown instead).
