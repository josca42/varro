table: fact.straf61
description: Afgjorte biforhold efter overtrædelsens art, afgørelsestype, alder, køn og tid
measure: indhold (unit Antal)
columns:
- overtraed: join dim.overtraedtype on overtraed=kode::text [approx]; levels [1, 2, 3]
- afgorelse: values [TOT=Afgjorte forhold i alt, FA=Fældende afgørelser (skyldig), IFA=Ikke fældende afgørelser (ikke skyldig)]
- alder: values [TOT=Alder i alt, UA=Uoplyst alder, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70-79=70-79 år, 80-=80 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder, VIRKSOMHEDER=Virksomheder]
- tid: date range 1980-01-01 to 2024-01-01
dim docs: /dim/overtraedtype.md

notes:
- "Biforhold" = secondary charges settled in the same case (distinct from the principal sentence in straf40). This counts adjudicated secondary matters, not persons or sentences.
- afgorelse has only 3 values: TOT (all), FA (fældende afgørelser = guilty), IFA (ikke fældende = not guilty). Much simpler than straf40's 47-code hierarchy.
- overtraed joins dim.overtraedtype at niveaux 1, 2, 3 (95 of 97 distinct codes match). Two unmatched codes: TOT (aggregate, not in dim) and 1000 (= "Uoplyst straffelov" — an inline code present in the fact table but absent from the dim). Filter or handle these explicitly.
- kon includes VIRKSOMHEDER. Goes back to 1980 (same as straf40).