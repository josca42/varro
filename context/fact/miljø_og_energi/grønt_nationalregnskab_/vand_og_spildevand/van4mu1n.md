table: fact.van4mu1n
description: Direkte og indirekte udledning af spildevand efter branche, udledning, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- branche: join dim.nr_branche on REPLACE(branche, 'V', '')=kode::text [approx: Strip V prefix from fact values to match dimension KODE]
- udl: values [UDLTOT=Udledning af spildevand i alt, UDLREC=Egen udledning til recipient, UDLSPI=Udledning til spildevandssystem]
- mult: values [SPVANDIR=Direkte udledning af spildevand, 1000 m3, SPVANINT=Direkte krav til udledning af spildevand (spildevandsintensitet), 1000 m3 / mio. kr, SPVANMUL=Direkte og indirekte krav til udledning af spildevand (multiplikator), 1000 m3 / mio. kr.]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2010-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md

notes:
- branche joins dim.nr_branche using: REPLACE(REPLACE(f.branche, 'V', ''), '_', '-') = TRIM(d.kode). branche='V' alone (total all industries) is not in dim.
- mult is a measurement-type selector — three different measures with different units (absolute volume, intensity, multiplier). Must filter to exactly one.
- prisenhed is a price-base selector (V=current, LAN=2020 fixed). Must filter to one.
- udl is hierarchical: UDLTOT = UDLREC + UDLSPI. Filter to one value.
- 5 hierarchy levels in dim (1–5); filter by d.niveau to pick granularity and avoid cross-level double-counting.
- Wastewater counterpart to van2mu1n (water consumption). Use SPVANDIR for absolute volume, SPVANINT for discharge intensity, SPVANMUL for full supply-chain footprint.
