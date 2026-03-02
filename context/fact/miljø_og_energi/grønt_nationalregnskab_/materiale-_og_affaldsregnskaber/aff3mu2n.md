table: fact.aff3mu2n
description: Direkte og indirekte affaldsproduktion efter endelig anvendelse og farlighed efter anvendelse, farlighed, multiplikator, prisenhed og tid
measure: indhold (unit -)
columns:
- anvend1: values [ACPT=Husholdningernes forbrugsudgifter (Anvendelse), ACPA=A Fødevarer mv. - (Anvendelse), ACPB=B Drikkevarer og tobak mv. - (Anvendelse), ACPC=C Beklædning og fodtøj - (Anvendelse), ACPD=D Boligbenyttelse - (Anvendelse) ... ABI5150=Investering i ændring i dyrkede aktiver - (Anvendelse), ABI517P=Intellektuelle rettigheder - (Anvendelse), AL5200=Lagre - (Anvendelse), AV5300=Værdigenstande - (Anvendelse), AE6000=Eksport - (Anvendelse)]
- farlig: values [FARLIG=Farligt affald, IKFARLIG=Ikke-farligt affald, TOTAFFALDX=Affald i alt (ekskl. jord)]
- mult: values [AFF3DIREA=Direkte affaldsmængder efter endelig anvendelse og farlighed, (tons), AFF3INTEA=Direkte og indirekte affaldsmængder efter endelig anvendelse og farlighed, (tons), AFF3MULEA=Direkte og indirekte affaldsmængder efter endelig anvendelse og farlighed (multiplikator), (tons pr. mio. kr.)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2011-01-01 to 2023-01-01
notes:
- mult selector (3 values): AFF3DIREA=direkte tons, AFF3INTEA=direkte+indirekte tons, AFF3MULEA=multiplikator (tons/mio.kr.). Always filter to one.
- prisenhed selector (V/LAN) — filter to one.
- anvend1: final demand categories (no dim join). See aff1mu2n notes.
- farlig: 3 values (FARLIG/IKFARLIG/TOTAFFALDX) — filter to one.
