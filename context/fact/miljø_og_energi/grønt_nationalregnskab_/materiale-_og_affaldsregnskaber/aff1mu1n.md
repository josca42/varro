table: fact.aff1mu1n
description: Direkte og indirekte affaldsproduktion efter branche og fraktion efter branche, affaldsfraktion, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- branche: join dim.nr_branche on REPLACE(branche, 'V', '')=kode::text [approx: V prefix in fact values needs stripping; only ~55% codes match]
- afffrak: values [TOTAFFALD=Affald i alt (inkl. jord), TOTAFFALDX=Affald i alt (ekskl. jord), A=DAGRENOVATION OG LIGNENDE, 101=Dagrenovation og lignende, B=ORGANISK AFFALD, INKL. HAVEAFFALD ... 151=Restprodukter fra forbrænding, 152=Deponeringsegnet, 124=Tekstiler, 125=Blandet emballage, 199=Andet affald]
- mult: values [AFF1DIR=Direkte genereret affald efter affaldsfraktion, (tons), AFF1INT=Direkte krav til genereret affald efter affaldsfraktion (affaldsintensitet), (tons pr. mio. kr.), AFF1MUL=Direkte og indirekte krav til genereret affald efter affaldsfraktion (multiplikator), (tons pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2011-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md
notes:
- mult is a measurement-type selector (3 values): AFF1DIR=direkte tons, AFF1INT=direkte intensitet (tons/mio.kr.), AFF1MUL=multiplikator direkte+indirekte (tons/mio.kr.). Always filter to one — units differ.
- prisenhed selector (2 values): V=løbende priser, LAN=2020-priser. Filter to one when using intensity/multiplier values.
- branche joins dim.nr_branche via REPLACE(branche,'V','')=kode. branche='V' (stripped to '') is the aggregate total — does not join.
- ~103 of 234 branche codes are 6-digit sub-industry codes not present in dim.nr_branche (e.g. V190000, V200010). These represent the most granular NACE sub-level; use branche value directly for labels at that level.
- afffrak is hierarchical (letter categories + numeric sub-fractions) — filter to consistent level.
