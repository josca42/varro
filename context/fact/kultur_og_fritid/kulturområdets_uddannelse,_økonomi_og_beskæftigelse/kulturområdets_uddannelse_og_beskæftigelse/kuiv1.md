table: fact.kuiv1
description: Kulturiværksætteri efter kulturemne, enhed og tid
measure: indhold (unit -)
columns:
- kulturemne: values [0=Alle kulturemner, 8=IDRÆT OG FRITID, 1=MEDIER, BIBLIOTEKER OG LITTERATUR, 20=SCENE OG MUSIK, 23=VISUEL KUNST OG DESIGN, 29=ANDEN KULTUREL AKTIVITET]
- enhed: values [30=Job ultimo november, 50=Nye virksomheder]
- tid: date range 2008-01-01 to 2023-01-01

notes:
- enhed is a measurement selector: 30=Job ultimo november, 50=Nye virksomheder. These are different measures — always filter to one. Do NOT sum across enhed.
- kulturemne=0 is the total across all cultural areas; filter when drilling into specific areas.
- Numeric kulturemne codes do not join to dim.kulturemner (K-prefix mismatch). Use inline values: 1=MEDIER mm., 8=IDRÆT OG FRITID, 20=SCENE OG MUSIK, 23=VISUEL KUNST OG DESIGN, 29=ANDEN KULTUREL AKTIVITET.