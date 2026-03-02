table: fact.ene2mu1n
description: Direkte og indirekte energiforbrug efter branche, energitype, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- branche: join dim.nr_branche on REPLACE(branche, 'V', '')=kode::text [approx: Fact values are prefixed with V (e.g., VA, V01000). Remove V prefix to match nr_branche.KODE.]
- energi1: values [ETOT=I ALT, EROOL=RÅOLIE OG HALVFABRIKATA, ERO=Råolie, EHFBK=Halvfabrikata, EOIL=OLIEPRODUKTER ... EVMP=Omgivelsesvarme indvundet med varmepumper, EKONV=KONVERTEREDE ENERGIARTER, EEL=El, EFJV=Fjernvarme, EGVG=Bygas]
- mult: values [ENEDIR=Direkte forbrug af energi, (GJ (gigajoule)), ENEINT=Direkte krav til energi (energiintensitet), (GJ (gigajoule) pr. mio. kr.), ENEMUL=Direkte og indirekte krav til energi (multiplikator), (GJ (gigajoule) pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1990-01-01 to 2024-01-01
dim docs: /dim/nr_branche.md

notes:
- branche joins dim.nr_branche using: REPLACE(REPLACE(f.branche, 'V', ''), '_', '-') = TRIM(d.kode). Strip V prefix, replace underscore with hyphen (VD_E → D-E), and TRIM the dim kode (some have trailing spaces). Code 'V' alone (total of all sectors) has no dim match.
- mult is a measurement-type selector — each branche × energi1 × prisenhed combination appears 3× (once per mult). Always filter to one mult: ENEDIR=direct energy use (GJ), ENEINT=energy intensity (GJ/mio.kr.), ENEMUL=multiplier incl. indirect use (GJ/mio.kr.). Never SUM across mult values.
- prisenhed is a second selector (V=current prices, LAN=2020 prices). Filter to one. For ENEDIR, the physical GJ values are the same regardless of prisenhed; prisenhed only affects intensity/multiplier denominators.
- Use ColumnValues("nr_branche", "titel", for_table="ene2mu1n") to see available branches.