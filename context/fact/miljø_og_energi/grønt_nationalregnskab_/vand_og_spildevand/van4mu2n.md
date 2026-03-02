table: fact.van4mu2n
description: Direkte og indirekte udledning af spildevand efter anvendelse, udledning, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- anvend1: values [ACPT=Husholdningernes forbrugsudgifter (Anvendelse), ACPA=A Fødevarer mv. - (Anvendelse), ACPB=B Drikkevarer og tobak mv. - (Anvendelse), ACPC=C Beklædning og fodtøj - (Anvendelse), ACPD=D Boligbenyttelse - (Anvendelse) ... ABI5150=Investering i ændring i dyrkede aktiver - (Anvendelse), ABI517P=Intellektuelle rettigheder - (Anvendelse), AL5200=Lagre - (Anvendelse), AV5300=Værdigenstande - (Anvendelse), AE6000=Eksport - (Anvendelse)]
- udl: values [UDLTOT=Udledning af spildevand i alt, UDLREC=Egen udledning til recipient, UDLSPI=Udledning til spildevandssystem]
- mult: values [SPVANDIREA=Direkte udledning af spildevand efter endelig anvendelse, (1000 m3), SPVANINTEA=Direkte og indirekte udledning af spildevand efter endelig anvendelse, (1000 m3), SPVANMULEA=Direkte og indirekte udledning af spildevand efter endelig anvendelse (multiplikator), (1000 m3 pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2010-01-01 to 2023-01-01

notes:
- No dimension joins — all columns are inline coded values.
- mult is a measurement-type selector (three different measures/units). Must filter to exactly one.
- prisenhed is a price-base selector (V=current, LAN=2020 fixed). Must filter to one.
- udl is hierarchical: UDLTOT = UDLREC + UDLSPI. Filter to one value.
- anvend1 = final demand categories. ACPT is household total; ACPA–ACPZ are sub-categories that sum to ACPT. Use ColumnValues("van4mu2n", "anvend1") to browse all categories.
- Companion to van4mu1n: van4mu1n breaks down by production branch, van4mu2n by final use category.
