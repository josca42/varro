table: fact.van2mu2n
description: Direkte og indirekte vandforbrug efter anvendelse, vandtype, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- anvend1: values [ACPT=Husholdningernes forbrugsudgifter (Anvendelse), ACPA=A Fødevarer mv. - (Anvendelse), ACPB=B Drikkevarer og tobak mv. - (Anvendelse), ACPC=C Beklædning og fodtøj - (Anvendelse), ACPD=D Boligbenyttelse - (Anvendelse) ... ABI5150=Investering i ændring i dyrkede aktiver - (Anvendelse), ABI517P=Intellektuelle rettigheder - (Anvendelse), AL5200=Lagre - (Anvendelse), AV5300=Værdigenstande - (Anvendelse), AE6000=Eksport - (Anvendelse)]
- vandtyp: values [VAFO=Forbrug af vand i alt, INDVA=Eget indvundet vand, INDGVA=Eget indvundet grundvand, INDOVA=Eget indvundet overfladevand, KOVA=Købt vand]
- mult: values [VANDIREA=Direkte forbrug af vand efter endelig anvendelse, (1000 m3), VANINTEA=Direkte og indirekte forbrug af vand efter endelig anvendelse, (1000 m3), VANMULEA=Direkte og indirekte forbrug af vand efter endelig anvendelse (multiplikator), (1000 m3 pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2010-01-01 to 2023-01-01

notes:
- No dimension joins — all columns are inline coded values.
- mult is a measurement-type selector (three different measures/units). Must filter to exactly one.
- prisenhed is a price-base selector (V=current, LAN=2020 fixed). Must filter to one.
- vandtyp is hierarchical: VAFO = INDVA + KOVA; INDVA = INDGVA + INDOVA. Filter to one.
- anvend1 = final demand categories (household consumption sub-categories, investment types, export). These are breakdowns of total final demand — ACPT is the household total and the sub-categories (ACPA, ACPB, …) sum to ACPT. Use ColumnValues("van2mu2n", "anvend1") to see all categories.
- Companion to van2mu1n: van2mu1n breaks down by production branch (who produces), van2mu2n by final use category (who consumes).
