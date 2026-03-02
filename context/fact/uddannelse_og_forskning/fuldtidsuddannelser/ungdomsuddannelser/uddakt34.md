table: fact.uddakt34
description: Uddannelsesaktivitet på erhvervsfaglige uddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status, uddannelsesdel og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [TOT=I alt, H29=H29 Erhvervsfaglige grundforløb, H2910=H2910 Omsorg, sundhed og pædagogik (OSP), grundforløb, H291010=H291010 Sundhed, omsorg og pædagogik, grundforløb, H2915=H2915 Kontor, handel og forretningsservice (KHF), grundforløb ... H3090=H3090 Andre erhvervsfaglige uddannelser, H309010=H309010 Erhvervsfiskeri mv., H309015=H309015 Maritime uddannelser, H309020=H309020 Forsvaret, H309025=H309025 Øvrige erhvervsfaglige uddannelser]
- alder: values [TOT=Alder i alt, -13=Under 14 år, 14=14 år, 15=15 år, 16=16 år ... 28=28 år, 29=29 år, 30-34=30-34 år, 35-39=35-39 år, 40-=40 år-]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- herkomst1: values [TOT=I alt, 1=Danmark, 2=Vestlige lande, 9=Ikke-vestlige lande, 000=Uoplyst national oprindelse]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- udddl: values [TT=I alt, 00=Udelt uddannelse, 51=Grundforløb før EUD-reformene 2015, 53=Grundforløb 1, 54=Grundforløb 2, 52=Hovedforløb, 55=EUX Studiekompetenceforløb, 56=Grundforløb plus]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus splits three independent measurement types (B=enrolled 1. oktober, F=fuldført, T=tilgang). Always filter to one.
- uddannelse is hierarchical with 4 levels via H-prefix code length: 3 chars (H29, H30) = gruppe, 5 chars = undergruppe, 7 chars = detaljeret, 9 chars = specifik program. TOT=I alt. Pick one level; don't mix lengths.
- alder: individual ages 14–29, then age bands 30-34, 35-39, 40-. Summing all numeric ages plus TOT or the age bands causes double-counting. For a simple count, use alder='TOT'. For age distribution, pick either single years (14–29) or bands (30-34 etc.), not both.
- udddl breaks the education into parts (grundforløb/hovedforløb/EUX etc.). TT=I alt. Filter to TT for total counts. Use specific codes to compare e.g. grundforløb vs. hovedforløb enrollment.
- herkomst and herkomst1: same as uddakt30 — filter both to TOT unless studying origin breakdown.
- No regional dimension; for regional breakdown of erhvervsfaglige uddannelser this table cannot help — use other tables or combine sources.