table: fact.naht1
description: Husholdningers indkomst og forbrug efter transaktion, enhed, kvintil og tid
measure: indhold (unit -)
columns:
- transakt: values [B2GB3G=Bruttooverskud af produktionen og blandet indkomst, D1K=Modtaget aflønning af ansatte, D4K=Modtaget formueindkomst, D4D=Betalt formueindkomst, B5G=Primær bruttoindkomst ... CP10=Undervisning, CP11=Restauranter og hoteller, CP12=Forsikring og finansielle tjenester mv., P3=Samlet forbrug af residente husholdninger, B8GUP=Bruttoopsparing uden korrektion for ændringer i pensionsrettigheder]
- tal: values [8000=Beløb i alt (mio. kr.), 8010=Beløb pr. husholdning (1.000 kr.), 8020=Husholdninger i gruppen (antal)]
- kvintil: values [KVTOT=I alt, 1K=1. kvintil, 2K=2. kvintil, 3K=3. kvintil, 4K=4. kvintil, 5K=5. kvintil]
- tid: date range 2018-01-01 to 2022-01-01
notes:
- tal is a measurement unit selector: 8000=beløb i alt (mio. kr.), 8010=beløb pr. husholdning (1.000 kr.), 8020=husholdninger i gruppen (antal). These are completely different units — never mix them or sum across tal values.
- kvintil=KVTOT is 'I alt' (all quintiles). The 5 quintile rows (1K-5K) sum to KVTOT.
- transakt codes span both income and expenditure items — the codes are not additive across the full list. This table is meant for distributional analysis: compare specific transakt codes across kvintil groups.
- Only covers 2018-2022. No quarterly version.
