table: fact.ene2mu3n
description: Direkte og indirekte energiforbrug efter branche, energitype, årsag, prisenhed og tid
measure: indhold (unit GJ (gigajoule))
columns:
- branche: values [V=I alt, VA=A Landbrug, skovbrug og fiskeri, V01000=01000 Landbrug og gartneri, V010000=010000 Landbrug og gartneri, V02000=02000 Skovbrug ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- energi1: values [ETOT=I ALT, EROOL=RÅOLIE OG HALVFABRIKATA, ERO=Råolie, EHFBK=Halvfabrikata, EOIL=OLIEPRODUKTER ... EVMP=Omgivelsesvarme indvundet med varmepumper, EKONV=KONVERTEREDE ENERGIARTER, EEL=El, EFJV=Fjernvarme, EGVG=Bygas]
- affaldsopr: values [ACPT=Husholdningernes forbrugsudgifter (Anvendelse), ACPA=A Fødevarer mv. - (Anvendelse), ACPB=B Drikkevarer og tobak mv. - (Anvendelse), ACPC=C Beklædning og fodtøj - (Anvendelse), ACPD=D Boligbenyttelse - (Anvendelse) ... ABI5150=Investering i ændring i dyrkede aktiver - (Anvendelse), ABI517P=Intellektuelle rettigheder - (Anvendelse), AL5200=Lagre - (Anvendelse), AV5300=Værdigenstande - (Anvendelse), AE6000=Eksport - (Anvendelse)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 1990-01-01 to 2022-01-01

notes:
- affaldsopr (despite the column name meaning "waste/origin") contains final demand categories — same ACP* structure as ene2mu2n.anvend1. It shows which final demand category drives energy use by each sector (input-output attribution).
- branche: V-prefix convention (no dim join noted in this doc). V=total; VA, VC, V{NACE}... are sectors. Filter to one hierarchy level.
- prisenhed: selector (V=current prices, LAN=2020). Filter to one.
- indhold is in GJ (unlike ene2mu1n/ene2mu2n which have mixed units depending on mult). Ends at 2022 (ene2mu1n goes to 2024).
- This table is a branche × final-demand attribution table — useful for tracing energy footprints back to consumption.