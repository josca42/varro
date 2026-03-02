table: fact.uddakt35
description: Uddannelsesaktivitet på erhvervsfaglige uddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status, uddannelsesform og tid
measure: indhold (unit Antal)
columns:
- uddannelse: values [TOT=I alt, H29=H29 Erhvervsfaglige grundforløb, H2910=H2910 Omsorg, sundhed og pædagogik (OSP), grundforløb, H291010=H291010 Sundhed, omsorg og pædagogik, grundforløb, H2915=H2915 Kontor, handel og forretningsservice (KHF), grundforløb ... H3090=H3090 Andre erhvervsfaglige uddannelser, H309010=H309010 Erhvervsfiskeri mv., H309015=H309015 Maritime uddannelser, H309020=H309020 Forsvaret, H309025=H309025 Øvrige erhvervsfaglige uddannelser]
- alder: values [TOT=Alder i alt, -13=Under 14 år, 14=14 år, 15=15 år, 16=16 år ... 28=28 år, 29=29 år, 30-34=30-34 år, 35-39=35-39 år, 40-=40 år-]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- herkomst1: values [TOT=I alt, 1=Danmark, 2=Vestlige lande, 9=Ikke-vestlige lande, 000=Uoplyst national oprindelse]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- uddform: values [70=I alt, 40=Mesterlære, 41=EUD praktikvej          , 42=EUD skolevej          , 43=Skolepraktik, 44=Voksenerhvervsuddannelse, 45=Gymnasial adgangsvej, 46=Opskoling og merit, 47=EUX praktivej, 48=EUX skolevej, 49=EUX skolepraktik, 50=Gymnasial adgangsvej praktikvej, 51=Gymnasiel adgangsvej  skolevej, 60=Maritim uddannelse, uden merit                         , 61=Maritim Uddannelse med 6 mdrs. merit            , 65=Maritim Uddannelse med 30 mdrs. merit          , 0=Uden nærmere angivelse (andet)]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- uddform is the distinguishing column vs uddakt34: it breaks down erhvervsfaglige uddannelser by training form/pathway (Mesterlære, EUD praktikvej, EUD skolevej, Skolepraktik, EUX-variants, Maritime etc.). 70=I alt. Filter to 70 for total counts; use specific codes to compare e.g. praktik vs. skole pathways.
- fstatus, uddannelse, alder, herkomst, herkomst1 behave the same as uddakt34. Always filter fstatus to one value; keep uddannelse at one hierarchy level; use alder='TOT' unless doing age breakdown.
- uddakt35 replaces udddl (uddannelsesdel in uddakt34) with uddform (uddannelsesform). Use uddakt34 for grundforløb/hovedforløb split; use uddakt35 for practical vs. school pathway split.
- Note: uddform values have trailing whitespace in some codes (e.g. '41=EUD praktikvej          '). Trim when filtering.