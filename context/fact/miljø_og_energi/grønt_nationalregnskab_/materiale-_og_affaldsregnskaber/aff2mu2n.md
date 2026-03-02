table: fact.aff2mu2n
description: Direkte og indirekte affaldsproduktion efter endelig anvendelse og behandlingsform efter anvendelse, behandlingsform, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- anvend1: values [ACPT=Husholdningernes forbrugsudgifter (Anvendelse), ACPA=A Fødevarer mv. - (Anvendelse), ACPB=B Drikkevarer og tobak mv. - (Anvendelse), ACPC=C Beklædning og fodtøj - (Anvendelse), ACPD=D Boligbenyttelse - (Anvendelse) ... ABI5150=Investering i ændring i dyrkede aktiver - (Anvendelse), ABI517P=Intellektuelle rettigheder - (Anvendelse), AL5200=Lagre - (Anvendelse), AV5300=Værdigenstande - (Anvendelse), AE6000=Eksport - (Anvendelse)]
- behandling: values [TOT=I alt, GENANV=Genanvendelse, inkl. anden endelig materialenyttiggørelse, FORBRND=Forbrænding, DEPOT=Deponering, SPEC=Særlig behandling, MIDOP=Midlertidig oplagring]
- mult: values [AFF2DIREA=Direkte affaldsmængder efter endelig anvendelse og behandligsform, (tons), AFF2INTEA=Direkte og indirekte affaldsmængder efter endelig anvendelse og  behandligsform, (tons), AFF2MULEA=Direkte og indirekte affaldsmængder efter endelig anvendelse og  behandligsform (multiplikator), (tons pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2011-01-01 to 2023-01-01
notes:
- mult selector (3 values): AFF2DIREA=direkte tons, AFF2INTEA=direkte+indirekte tons, AFF2MULEA=multiplikator (tons/mio.kr.). Always filter to one.
- prisenhed selector (V/LAN) — filter to one.
- anvend1: final demand categories (no dim join). See aff1mu2n notes for structure.
- behandling=TOT is aggregate — filter to TOT or individual methods.
