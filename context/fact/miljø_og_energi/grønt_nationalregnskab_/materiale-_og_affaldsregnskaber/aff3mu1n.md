table: fact.aff3mu1n
description: Direkte og indirekte affaldsproduktion efter branche og farlighed efter branche, farlighed, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- branche: join dim.nr_branche on REPLACE(branche, 'V', '')=kode::text [approx: V prefix in fact values needs stripping; only ~55% codes match]
- farlig: values [FARLIG=Farligt affald, IKFARLIG=Ikke-farligt affald, TOTAFFALDX=Affald i alt (ekskl. jord)]
- mult: values [AFF3DIR=Direkte genereret affald efter farlighed, (tons), AFF3INT=Direkte krav til genereret affald efter farlighed (affaldsintensitet), (tons pr. mio. kr.), AFF3MUL=Direkte og indirekte krav til genereret affald efter farlighed (multiplikator), (tons pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2011-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md
notes:
- mult is a measurement-type selector (3 values): AFF3DIR=direkte tons, AFF3INT=direkte intensitet (tons/mio.kr.), AFF3MUL=multiplikator (tons/mio.kr.). Always filter to one.
- prisenhed selector (V/LAN) — filter to one.
- branche joins dim.nr_branche via REPLACE(branche,'V','')=kode. Same partial-match issue (~56%). branche='V' = aggregate total.
- farlig has 3 values: FARLIG, IKFARLIG, TOTAFFALDX. Filter to one to avoid summing hazardous + non-hazardous + total.
