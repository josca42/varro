table: fact.eud34
description: Uddannelsesaktivitet på erhvervsfaglige uddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status, uddannelsesdel og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [TOT=I alt, 3=3 Erhvervsfaglige uddannelser, 31=31 Erhvervsuddannelserne, grundforløb, 311=311 Erhvervsuddannelserne, grundforløb 1 for helt unge, 3111=3111 Omsorg, sundhed og pædagogik (grundforløb 1) ... 3983=3983 Maritime uddannelser, erhvervsfaglige, 3985=3985 Politivirksomhed, erhvervsfaglig, 3987=3987 Erhvervsfaglige uddannelser, øvrige, 399=399 Erhvervsfaglig åben uddannelse (ÅU), 3995=3995 Erhvervsfaglig åben uddannelse (ÅU)]
- alder: values [TOT=Alder i alt, -13=Under 14 år, 14=14 år, 15=15 år, 16=16 år ... 28=28 år, 29=29 år, 30-34=30-34 år, 35-39=35-39 år, 40-=40 år-]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- herkomst1: values [TOT=I alt, 1=Danmark, 2=Vestlige lande, 9=Ikke-vestlige lande, 000=Uoplyst national oprindelse]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- udddl: values [TT=I alt, 00=Udelt uddannelse, 51=Grundforløb før EUD-reformene 2015, 53=Grundforløb 1, 54=Grundforløb 2, 52=Hovedforløb, 55=EUX Studiekompetenceforløb, 56=Grundforløb plus]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- eud34 covers the same topic as uddakt34 (erhvervsfaglige uddannelser, by alder/herkomst/kon/fstatus/udddl) but uses a completely different uddannelse classification: numeric codes (1–4 digits) instead of H-prefix codes. The two tables are NOT directly comparable by uddannelse code.
- eud34 has ~1.7M rows vs uddakt34's ~5M — reflecting the narrower/fewer categories in the numeric scheme.
- uddannelse hierarchy follows 4 numeric levels by code length: 1 digit = top, 2 digit = gruppe, 3 digit = undergruppe, 4 digit = specifik. TOT=I alt. Filter to one level.
- fstatus, alder, udddl, herkomst, herkomst1 behave identically to uddakt34 — see those notes for caveats.
- Prefer uddakt34 when the H-prefix classification is needed (matches other gymnasiale/erhvervsfaglige tables). Use eud34 when the numeric DST classification system is required or when comparing with other tables that use numeric education codes.