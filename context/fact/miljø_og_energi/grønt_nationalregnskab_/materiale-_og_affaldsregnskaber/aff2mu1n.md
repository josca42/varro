table: fact.aff2mu1n
description: Direkte og indirekte affaldsproduktion efter branche og behandlingsform efter branche, behandlingsform, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- branche: join dim.nr_branche on REPLACE(branche, 'V', '')=kode::text [approx: V prefix in fact values needs stripping; only ~55% codes match]
- behandling: values [TOT=I alt, GENANV=Genanvendelse, inkl. anden endelig materialenyttiggørelse, FORBRND=Forbrænding, DEPOT=Deponering, SPEC=Særlig behandling, MIDOP=Midlertidig oplagring]
- mult: values [AFF2DIR=Direkte genereret affald efter behandlingsform, (tons), AFF2INT=Direkte krav til genereret affald efter behandlingsform (affaldsintensitet), (tons pr. mio. kr.), AFF2MUL=Direkte og indirekte krav til genereret affald efter behandlingsform (multiplikator), (tons pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2011-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md
notes:
- mult is a measurement-type selector (3 values): AFF2DIR=direkte tons, AFF2INT=direkte intensitet (tons/mio.kr.), AFF2MUL=multiplikator (tons/mio.kr.). Always filter to one.
- prisenhed selector (V/LAN) — filter to one.
- branche joins dim.nr_branche via REPLACE(branche,'V','')=kode. Same partial-match issue (~56%); 6-digit sub-industry codes won't join. branche='V' = aggregate total.
- behandling=TOT is aggregate — filter to individual treatment methods or TOT for totals.
