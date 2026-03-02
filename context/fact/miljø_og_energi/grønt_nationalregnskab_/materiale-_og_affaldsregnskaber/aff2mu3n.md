table: fact.aff2mu3n
description: Affaldsproduktion efter branche, behandlingsform og forårsagende endelig anvendelse efter branche, behandlingsform, årsag, prisenhed og tid
measure: indhold (unit Ton)
columns:
- branche: join dim.nr_branche on REPLACE(branche, 'V', '')=kode::text [approx: V prefix in fact values needs stripping; only ~55% codes match]
- behandling: values [TOT=I alt, GENANV=Genanvendelse, inkl. anden endelig materialenyttiggørelse, FORBRND=Forbrænding, DEPOT=Deponering, SPEC=Særlig behandling, MIDOP=Midlertidig oplagring]
- affaldsopr: values [ACPT=Husholdningernes forbrugsudgifter (Anvendelse), ACPA=A Fødevarer mv. - (Anvendelse), ACPB=B Drikkevarer og tobak mv. - (Anvendelse), ACPC=C Beklædning og fodtøj - (Anvendelse), ACPD=D Boligbenyttelse - (Anvendelse) ... ABI5150=Investering i ændring i dyrkede aktiver - (Anvendelse), ABI517P=Intellektuelle rettigheder - (Anvendelse), AL5200=Lagre - (Anvendelse), AV5300=Værdigenstande - (Anvendelse), AE6000=Eksport - (Anvendelse)]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2011-01-01 to 2023-01-01
dim docs: /dim/nr_branche.md
notes:
- Shows which final demand (affaldsopr) caused waste by industry (branche) broken down by treatment method.
- prisenhed selector (V/LAN) — filter to one. No mult column: indhold always in tons.
- branche joins dim.nr_branche via REPLACE(branche,'V','')=kode. Same partial-match issue as aff1mu1n.
- behandling=TOT is aggregate — use TOT for total or filter to individual method.
