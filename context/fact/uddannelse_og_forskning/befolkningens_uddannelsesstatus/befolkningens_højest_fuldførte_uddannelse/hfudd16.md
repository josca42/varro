table: fact.hfudd16
description: Befolkningens højest fuldførte uddannelse (15-69 år) efter bopælsområde, højest fuldførte uddannelse, socioøkonomisk status, branche, alder, køn og tid
measure: indhold (unit Antal)
columns:
- bopomr: values [0=Hele landet, 84=Region Hovedstaden, 101=København, 147=Frederiksberg, 155=Dragør ... 773=Morsø, 840=Rebild, 787=Thisted, 820=Vesthimmerlands, 851=Aalborg]
- uddannelsef: values [TOT=I alt, H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H35=H35 Adgangsgivende uddannelsesforløb, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H60=H60 Bacheloruddannelser, BACH, H70=H70 Lange videregående uddannelser, LVU, H80=H80 Ph.d. og forskeruddannelser, H90=H90 Uoplyst mv.]
- socio: values [0=Under uddannelse, 1=Beskæftigede, 2=Arbejdsløs, 3=Udenfor arbejdsstyrken]
- erhverv: values [TOT=TOT Erhverv i alt, A=A Landbrug, skovbrug og fiskeri, B=B Råstofindvinding, CA=CA Føde-, drikke- og tobaksvareindustri, CB=CB Tekstil- og læderindustri ... QA=QA Sundhedsvæsen, QB=QB Sociale institutioner, R=R Kultur og fritid, S=S Andre serviceydelser mv., X=X Uoplyst aktivitet]
- alder: values [TOT=Alder i alt, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2008-01-01 to 2023-01-01

notes:
- bopomr joins dim.nuts directly (both smallint). 0=national total (not in dim), 81-85=5 regioner (niveau 1), 101-860+411=99 kommuner (niveau 3, including Christiansø=411). No landsdele (niveau 2). Filter d.niveau to choose granularity.
- socio has NO total row — the 4 categories (0=Under uddannelse, 1=Beskæftigede, 2=Arbejdsløs, 3=Udenfor arbejdsstyrken) are mutually exclusive and exhaustive. To get total population sum across all 4, or filter to one socio group.
- erhverv has a TOT code — always filter erhverv='TOT' unless you specifically want industry breakdown. Individual industry codes (A through S) plus X (Uoplyst) sum to TOT; summing only named industries understates the total.
- uddannelsef has inline codes (H10-H90 + TOT) — these are the same 10 education levels as other tables in this subject; no dim join needed, use them directly.
- To get simple population count by region and education: filter socio to all 4 values (or use GROUP BY + SUM), erhverv='TOT', alder='TOT', koen='TOT', then GROUP BY bopomr, uddannelsef.
- This is the only table in the subject with socio (employment status) and erhverv (industry) dimensions — use it when those breakdowns matter.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.