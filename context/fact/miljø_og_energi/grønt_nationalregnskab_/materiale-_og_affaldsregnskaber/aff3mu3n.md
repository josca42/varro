table: fact.aff3mu3n
description: Affaldsproduktion efter branche, farlighed og forårsagende endelig anvendelse efter branche, farlighed, årsag, prisenhed og tid
measure: indhold (unit Ton)
columns:
- branche: values [V=I alt, VA=A Landbrug, skovbrug og fiskeri, V01000=01000 Landbrug og gartneri, V010000=010000 Landbrug og gartneri, V02000=02000 Skovbrug ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- farlig: values [FARLIG=Farligt affald, IKFARLIG=Ikke-farligt affald, TOTAFFALDX=Affald i alt (ekskl. jord)]
- affaldsopr: values [ACPT=Husholdningernes forbrugsudgifter (Anvendelse), ACPA=A Fødevarer mv. - (Anvendelse), ACPB=B Drikkevarer og tobak mv. - (Anvendelse), ACPC=C Beklædning og fodtøj - (Anvendelse), ACPD=D Boligbenyttelse - (Anvendelse) ... ABI5150=Investering i ændring i dyrkede aktiver - (Anvendelse), ABI517P=Intellektuelle rettigheder - (Anvendelse), AL5200=Lagre - (Anvendelse), AV5300=Værdigenstande - (Anvendelse), AE6000=Eksport - (Anvendelse)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2011-01-01 to 2023-01-01
notes:
- Shows which final demand (affaldsopr) caused waste by industry (branche) broken down by hazard classification.
- prisenhed selector (V/LAN) — filter to one. No mult column: indhold always in tons. No dim join on branche (inline coded).
- branche='V' = aggregate total. branche values follow the V-prefix pattern (VA=Landbrug etc.) but no dim join is configured for this table.
- farlig: 3 values (FARLIG/IKFARLIG/TOTAFFALDX) — filter to one.
- affaldsopr is hierarchical (ACPT=husholdningsforbrug total, then sub-categories, plus investment/export/etc.) — filter to consistent level.
