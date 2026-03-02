table: fact.laby36
description: 18-25 åriges ungdomsuddannelser efter uddannelsesstatus, uddannelse, alder, kommunegruppe og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- uddannelse: values [TOT=I alt, H00=Ingen ungdomsuddannelse, H20=H20 Gymnasiale uddannelser, H29=H29 Erhvervsfaglige grundforløb, H30=H30 Erhvervsfaglige uddannelser, H99=Andre højere uddannelser]
- alder: values [IALT=Alder i alt, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25=25 år]
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/kommunegrupper.md

notes:
- komgrp joins dim.kommunegrupper at niveau 1 only (5 groups: Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner). komgrp=0 is the national total and is NOT in the dim table — a plain JOIN excludes it automatically.
- dim.kommunegrupper also has niveau 2 (individual municipalities), but this fact table only uses niveau 1 codes. No need to filter by niveau.
- 4 dimension columns (uddstat, uddannelse, alder, komgrp) all include total rows. For counts by kommunegruppe: filter uddstat='AA_TOTAL', uddannelse='TOT', alder='IALT', then group by komgrp.
- Covers all ages 18–25. Companion table laby36a covers 20-year-olds only but returns percentages rather than counts.