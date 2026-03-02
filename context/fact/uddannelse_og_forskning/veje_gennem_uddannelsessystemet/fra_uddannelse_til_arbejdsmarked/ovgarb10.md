table: fact.ovgarb10
description: Fra uddannelsesgrupper til fortsat uddannelse eller arbejdsmarked efter slutuddannelse i gruppen, herkomst, køn, uddannelsesstatus, status efter afgang, statustidspunkt efter afgang, alder ved afgang fra gruppe og tid
measure: indhold (unit Antal)
columns:
- uddangroup: values [TOT=I alt, H10=H10 Grundskole, H1010=H1010 Grundskole til og med 6. klasse, H101010=H101010 Grundskole til og med 6. klasse, H101020=H101020 Grundskole 7.-9. klasse ... H808035=H808035 Naturvidenskab, Ph.d., H808039=H808039 Samfundsvidenskab, Ph.d., H808059=H808059 Teknisk videnskab, Ph.d., H808080=H808080 Jordbrug, natur og miljø, Ph.d., H808090=H808090 Sundhedsvidenskab, Ph.d.]
- ietype: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- uddstat: values [T=I alt, 0=Har fuldført uddannelsen, 1=Har afbrudt uddannelsen, 2=Har fuldført delkompetance]
- statusafg: values [TOT=I alt, 000=Under uddannelse, 001=Beskæftigede, 002=Arbejdsløs, 003=Udenfor arbejdsstyrken, 950=Ikke i befolkningen]
- statustid: values [3M=3 måneder, 9M=9 måneder, 15M=15 måneder, 21M=21 måneder]
- alderlev: values [TOT=Alder i alt, -14=Under 15 år, 15=15 år, 16=16 år, 17=17 år ... 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-=50- år]
- tid: date range 2012-01-01 to 2021-01-01

notes:
- statustid is a measurement selector (3M, 9M, 15M, 21M = months after departure from education). All ~2M rows are repeated for each time point — ALWAYS filter to exactly one value (e.g. statustid = '9M'). Forgetting this silently multiplies counts by 4.
- uddangroup has 3 nested hierarchy levels present simultaneously: length=3 (10 top groups, e.g. H10=Grundskole), length=5 (12 mid groups), length=7 (76 fine-grained programs). Filter by length(uddangroup) = 7 for program-level detail, = 3 for top-level groupings. Summing across all levels massively overcounts. Note: some level-2 codes are redundant (H10 = H1010, both = 69662) because they have only one child.
- statusafg is the main outcome variable: 001=Beskæftigede, 002=Arbejdsløs, 003=Udenfor arbejdsstyrken, 000=Under uddannelse, 950=Ikke i befolkningen, TOT=total. Use TOT when summing all statuses, filter to specific codes when analyzing outcomes.
- uddstat distinguishes how students left: 0=fuldført uddannelsen, 1=afbrudt uddannelsen, 2=fuldført delkompetence, T=I alt. Most employment analyses want T (all) or 0 (completers only).
- All remaining columns have totals: uddangroup=TOT, statusafg=TOT, alderlev=TOT, ietype=TOT (I alt), kon=TOT, uddstat=T. When focusing on one dimension, filter all others to their total code to avoid overcounting.
- alderlev mixes individual ages (15–29 as single years) and age brackets (30–34, 35–39, 40–44, 45–49, 50–). There is no consistent single-year granularity above 29. TOT covers all ages.
- Sample query (employed 9M after completing any education, by top-level education group, latest year): SELECT uddangroup, indhold FROM fact.ovgarb10 WHERE statustid='9M' AND uddstat='T' AND statusafg='001' AND ietype='TOT' AND kon='TOT' AND alderlev='TOT' AND length(uddangroup)=3 AND tid='2021-01-01' ORDER BY uddangroup;