table: fact.van2mu1n
description: Direkte og indirekte vandforbrug efter branche, vandtype, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- branche: join dim.nr_branche on REPLACE(branche, 'V', '')=kode::text [approx: Strip V prefix from fact values to match dimension KODE]
- vandtyp: values [VAFO=Forbrug af vand i alt, INDVA=Eget indvundet vand, INDGVA=Eget indvundet grundvand, INDOVA=Eget indvundet overfladevand, KOVA=Købt vand]
- mult: values [VANDIR=Direkte forbrug af vand, (1000 m3), VANINT=Direkte krav til forbrug af vand (vandintensitet), (1000 m3 pr. mio. kr.), VANMUL=Direkte og indirekte krav til forbrug af vand (multiplikator), (1000 m3 pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md

notes:
- branche joins dim.nr_branche using: REPLACE(REPLACE(f.branche, 'V', ''), '_', '-') = TRIM(d.kode). branche='V' alone (total all industries) is not in dim — query without join for national totals.
- mult is a measurement-type selector — three completely different measures with different units (absolute volume, intensity, multiplier). Must always filter to exactly one mult value.
- prisenhed is a price-base selector — V (current prices) and LAN (2020 fixed prices). Must filter to one; never sum across both.
- vandtyp is hierarchical: VAFO = INDVA + KOVA; INDVA = INDGVA + INDOVA. Filter to one value.
- 5 hierarchy levels in dim (1–5); filter by d.niveau to pick granularity and avoid cross-level double-counting.
- For absolute water consumption by industry use VANDIR; for comparing water efficiency use VANINT; for full supply-chain footprint use VANMUL.
