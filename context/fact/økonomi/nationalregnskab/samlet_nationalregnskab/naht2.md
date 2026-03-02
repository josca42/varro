table: fact.naht2
description: Husholdningers indkomst og forbrug efter transaktion, enhed, husholdningstype og tid
measure: indhold (unit -)
columns:
- transakt: values [B2GB3G=Bruttooverskud af produktionen og blandet indkomst, D1K=Modtaget aflønning af ansatte, D4K=Modtaget formueindkomst, D4D=Betalt formueindkomst, B5G=Primær bruttoindkomst ... CP10=Undervisning, CP11=Restauranter og hoteller, CP12=Forsikring og finansielle tjenester mv., P3=Samlet forbrug af residente husholdninger, B8GUP=Bruttoopsparing uden korrektion for ændringer i pensionsrettigheder]
- tal: values [8000=Beløb i alt (mio. kr.), 8010=Beløb pr. husholdning (1.000 kr.), 8020=Husholdninger i gruppen (antal)]
- hushtyp: values [A0=Alle husholdninger, A11=Enlig under 65 år, uden børn, A12=Enlig 65 år og over, uden børn, A13=Enlig med børn, A21=2 voksne, begge under 65 år, uden børn, A22=2 voksne, mindst en er 65 år eller over, uden børn, A23=2 voksne med under 3 børn, A24=2 voksne med 3 børn eller over, A31=Andre]
- tid: date range 2018-01-01 to 2022-01-01
notes:
- tal is a measurement unit selector: 8000=beløb i alt (mio. kr.), 8010=beløb pr. husholdning (1.000 kr.), 8020=husholdninger i gruppen (antal). Always filter to one tal value — never sum across them.
- hushtyp=A0 is 'Alle husholdninger' (total). The other 8 types (A11-A31) are subtypes — they do not all sum to A0 as some overlap in definition (e.g., A0 = national total, not necessarily the sum of listed types).
- transakt identical to naht1. Same 2018-2022 coverage. Use naht1 for income quintile analysis, naht2 for household type analysis.
