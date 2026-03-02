table: fact.udvstd02
description: Udvekslingsstuderende efter køn, udveksling, opholds varighed, uddannelse, område og tid
measure: indhold (unit Antal)
columns:
- kon: values [0=I alt, 1=Mænd, 2=Kvinder, 9=Uoplyst køn]
- udveksling: values [TOT=I alt, 1=Udlænding i Danmark, 2=Dansker i udlandet]
- opvar: values [TOT=I alt, 10=0 - 3 måneder, 20=4 - 6 måneder, 30=7 - 12 måneder, 40=Mere end 12 måneder, 999=Uoplyst]
- uddannelse: values [TOT=I alt, H30=H30 Erhvervsfaglige uddannelser, H3055=H3055 Teknologiområdet, maskinteknik og produktion (TBT), H40=H40 Korte videregående uddannelser, KVU, H4024=H4024 Medier og kommunikation, KVU ... H8039=H8039 Samfundsvidenskab, Ph.d., H8059=H8059 Teknisk videnskab, Ph.d., H8080=H8080 Jordbrug, natur og miljø, Ph.d., H8090=H8090 Sundhedsvidenskab, Ph.d., H8097=H8097 Videregående uddannelser uden nærmere angivelse, Ph.d.]
- omr20: values [TOT=I alt, 100=Norden, 361=Øvrige Europa, 371=Afrika, 372=USA/Canada, 373=Latinamerika/Caribien, 374=Asien, 375=Australien/New Zealand/Stillehavsøer, 999=Uoplyst]
- tid: date range 2010-01-01 to 2024-01-01

notes:
- All 5 non-tid columns have aggregate/total rows (kon=0, udveksling=TOT, opvar=TOT, omr20=TOT, uddannelse=TOT). Filter every non-target column to its total to avoid overcounting — forgetting even one will inflate results.
- uddannelse has a 2-level hierarchy within the inline codes: 6 parent aggregates (H30, H40, H50, H60, H70, H80) and their children (H3055, H4024, etc.), plus TOT. H30+H40+H50+H60+H70+H80 = TOT. Never mix levels; pick either the level-1 aggregates or the detail codes, not both.
- opvar=999 (Uoplyst) listed in metadata does not exist in the actual data. Only 10, 20, 30, 40, TOT appear.
- udveksling distinguishes direction: 1=Udlænding i Danmark (inbound), 2=Dansker i udlandet (outbound). For total exchange students regardless of direction use udveksling=TOT.
- omr20 is the world region of the partner country (origin for inbound, destination for outbound). Use ColumnValues("udvstd02", "omr20") to see the 8 regions plus TOT.
- Sample query — inbound exchange students by education level in 2023:
  SELECT uddannelse, indhold FROM fact.udvstd02
  WHERE tid='2023-01-01' AND kon='0' AND udveksling='1' AND opvar='TOT' AND omr20='TOT'
    AND uddannelse IN ('H30','H40','H50','H60','H70','H80')
  ORDER BY uddannelse;