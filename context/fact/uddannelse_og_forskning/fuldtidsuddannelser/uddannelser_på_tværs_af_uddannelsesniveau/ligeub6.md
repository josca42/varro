table: fact.ligeub6
description: Uddannelsesaktivitet på STEM-uddannelser efter uddannelse, køn og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [TOT=I alt, TOTS=STEM-uddannelser, i alt, TOTO=Øvrige uddannelser, i alt, H40=H40 Korte videregående uddannelser, i alt, H40A=H40 STEM-uddannelser, Korte videregående uddannelser, H40B=H40 Øvrige uddannelser, Korte videregående uddannelser, H50=H50 Mellemlange videregående uddannelser, i alt, H50A=H50 STEM-uddannelser, Mellemlange videregående uddannelser, H50B=H50 Øvrige uddannelser, Mellemlange videregående uddannelser, H60=H60 Bacheloruddannelser, i alt, H60A=H60 STEM-uddannelser, Bacheloruddannelser, H60B=H60 Øvrige uddannelser, Bacheloruddannelser, H70=H70 Lange videregående uddannelser, i alt, H70A=H70 STEM-uddannelser, Lange videregående uddannelser, H70B=H70 Øvrige uddannelser, Lange videregående uddannelser, H80=H80 Ph.d. og forskeruddannelser, i alt, H80A=H80 STEM-uddannelser, Ph.d. og forskeruddannelser, H80B=H80 Øvrige uddannelser, Ph.d. og forskeruddannelser]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- Covers only higher education (KVU, MVU, bachelor, LVU, Ph.d.) — not grundskole, gymnasiale, or erhvervsfaglige uddannelser. For full education coverage use uddakt10/uddakt11.
- uddannelse has a two-layer STEM structure: TOT=all higher ed, TOTS=STEM total, TOTO=non-STEM total, then per-level splits (H40A=STEM KVU, H40B=non-STEM KVU, H50A/B, H60A/B, H70A/B, H80A/B). TOTS+TOTO=TOT and H40A+H40B=H40. Do not sum TOT with TOTS or TOTO — that double counts.
- No fstatus column — indhold is enrolled count (B-equivalent only).
- No alder or geographic breakdown.