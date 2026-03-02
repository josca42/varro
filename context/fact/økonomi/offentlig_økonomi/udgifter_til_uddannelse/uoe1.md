table: fact.uoe1
description: Udgifter til uddannelse efter uddannelsesniveau, udgiftstype, ejerforhold og tid
measure: indhold (unit Mio. kr.)
columns:
- uddniv: values [TOT1=Uddannelsesniveauer i alt, H10=Grundskoler, H30=Ungdomsuddannelser, H40=Korte videregående uddannelser, H50=Mellemlange og lange videregående uddannelser]
- udtype: values [TOT=Udgifter i alt, 10=Lønudgifter, 20=Andre løbende udgifter, 30=Investeringer, 50=Forskning og udvikling (FoU) , 40=SU og andre stipendier, 60=Ukendt]
- ejer: values [TOT4=Institutionernes udgifter i alt, 200=Offentlige uddannelsesinstitutioner, 210=Private uddannelsesinstitutioner, 2=Husholdninger]
- tid: date range 2016-01-01 to 2023-01-01

notes:
- All three dimension columns contain aggregate total rows: uddniv='TOT1', udtype='TOT', ejer='TOT4'. To avoid double-counting, either filter to a single specific value per column, or use the TOT codes to get pre-aggregated sums (e.g. uddniv='TOT1', udtype='TOT', ejer='TOT4' gives total uddannelsesudgifter).
- The uddniv × udtype × ejer matrix is sparse — not all combinations exist. Key structural facts:
  - ejer='2' (Husholdninger) only appears with udtype='40' (SU og andre stipendier) and udtype='TOT'. Households only show up in the SU expenditure type.
  - udtype='50' (Forskning og udvikling) only appears with ejer='200' (Offentlige) and ejer='TOT4'. FoU is only attributed to public institutions.
  - ejer='210' (Private institutioner) has no FoU row.
- This table covers expenditure by type (how money is spent: lønudgifter, investeringer, SU, FoU) and by institutional owner (public vs private vs households). Use uoe2 instead to see who finances the expenditure (state, municipalities, households, firms).
- Sample query — total udgifter by uddannelsesniveau in 2023: WHERE tid='2023-01-01' AND udtype='TOT' AND ejer='TOT4' (gives one row per uddniv including TOT1).