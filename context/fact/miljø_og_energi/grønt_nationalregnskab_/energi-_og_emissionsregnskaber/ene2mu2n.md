table: fact.ene2mu2n
description: Direkte og indirekte energiforbrug efter anvendelse, energitype, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- anvend1: values [ACPT=Husholdningernes forbrugsudgifter (Anvendelse), ACPA=A Fødevarer mv. - (Anvendelse), ACPB=B Drikkevarer og tobak mv. - (Anvendelse), ACPC=C Beklædning og fodtøj - (Anvendelse), ACPD=D Boligbenyttelse - (Anvendelse) ... ABI5150=Investering i ændring i dyrkede aktiver - (Anvendelse), ABI517P=Intellektuelle rettigheder - (Anvendelse), AL5200=Lagre - (Anvendelse), AV5300=Værdigenstande - (Anvendelse), AE6000=Eksport - (Anvendelse)]
- energi1: values [ETOT=I ALT, EROOL=RÅOLIE OG HALVFABRIKATA, ERO=Råolie, EHFBK=Halvfabrikata, EOIL=OLIEPRODUKTER ... EVMP=Omgivelsesvarme indvundet med varmepumper, EKONV=KONVERTEREDE ENERGIARTER, EEL=El, EFJV=Fjernvarme, EGVG=Bygas]
- mult: values [ENEDIREA=Direkte forbrug af energi efter endelig anvendelse, (GJ (gigajoule)), ENEINTEA=Direkte og indirekte forbrug af energi efter endelig anvendelse, (GJ (gigajoule)), ENEMULEA=Direkte og indirekte forbrug af energi efter endelig anvendelse (multiplikator), (GJ (gigajoule) pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- anvend1 is final demand (household consumption categories, investment, exports) — the use-side counterpart to ene2mu1n (which uses supply-side branche). ACPT=total household consumption; ACP* sub-codes are COICOP categories.
- mult is a measurement-type selector — every anvend1 × energi1 × prisenhed combination appears 3×. Always filter: ENEDIREA=direct GJ, ENEINTEA=direct+indirect GJ, ENEMULEA=multiplier (GJ/mio.kr.). Never SUM across mult.
- prisenhed: filter to one (V=current, LAN=2020 chain-linked).
- No dim join — anvend1 is inline-coded. ACPT is the grand total; ACP* sub-codes are components — don't mix levels.