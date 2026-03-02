table: fact.aff1mu2n
description: Direkte og indirekte affaldsproduktion efter endelig anvendelse og fraktion efter anvendelse, affaldsfraktion, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- anvend1: values [ACPT=Husholdningernes forbrugsudgifter (Anvendelse), ACPA=A Fødevarer mv. - (Anvendelse), ACPB=B Drikkevarer og tobak mv. - (Anvendelse), ACPC=C Beklædning og fodtøj - (Anvendelse), ACPD=D Boligbenyttelse - (Anvendelse) ... ABI5150=Investering i ændring i dyrkede aktiver - (Anvendelse), ABI517P=Intellektuelle rettigheder - (Anvendelse), AL5200=Lagre - (Anvendelse), AV5300=Værdigenstande - (Anvendelse), AE6000=Eksport - (Anvendelse)]
- afffrak: values [TOTAFFALD=Affald i alt (inkl. jord), TOTAFFALDX=Affald i alt (ekskl. jord), A=DAGRENOVATION OG LIGNENDE, 101=Dagrenovation og lignende, B=ORGANISK AFFALD, INKL. HAVEAFFALD ... 151=Restprodukter fra forbrænding, 152=Deponeringsegnet, 124=Tekstiler, 125=Blandet emballage, 199=Andet affald]
- mult: values [AFF1DIREA=Direkte affaldsmængder efter endelig anvendelse og affaldsfraktion, (tons), AFF1INTEA=Direkte og indirekte affaldsmængder efter endelig anvendelse og affaldsfraktion, (tons), AFF1MULEA=Direkte og indirekte affaldsmængder efter endelig anvendelse og affaldsfraktion (multiplikator), (tons pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2011-01-01 to 2023-01-01
notes:
- mult is a measurement-type selector (3 values): AFF1DIREA=direkte tons, AFF1INTEA=direkte+indirekte tons, AFF1MULEA=multiplikator (tons/mio.kr.). Always filter to one.
- prisenhed selector (V/LAN). Filter to one.
- anvend1: final demand categories (no dim join). ACPT=husholdningernes forbrugsudgifter i alt is the consumption total; AE6000=Eksport.
- afffrak is hierarchical — filter to consistent level.
