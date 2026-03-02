table: fact.ifatsf10
description: Udenlandsk ejede firmaer efter branche, land, enhed og tid
measure: indhold (unit -)
columns:
- erhverv: values [0=I alt, 2=2 Industri, råstofindvinding og forsyningsvirksomhed, 3=3 Bygge og anlæg, 4=4 Handel og transport mv., 5=5 Information og kommunikation, 6=6 Finansiering og forsikring, 7=7 Ejendomshandel og udlejning, 8=8 Erhvervsservice, X1=X1 Andre erhverv]
- land: values [TOT=I alt, DAN1=Dansk ejede, UDD=Udenlandsk ejede]
- enhed: values [ANTFIR=Firmaer (antal), XOM=Omsætning (mio. kr.), VAERK=Antal ansatte (årsværk)]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- enhed is a measurement-type selector — always filter to one value: ANTFIR (firm count), XOM (revenue mio. DKK), VAERK (FTE/årsværk). Failing to filter silently mixes incompatible units.
- erhverv='0' is "I alt" (all industries total). Exclude it when summing across industries: WHERE erhverv != '0'.
- land has 3 values: TOT (all firms), DAN1 (Danish-owned), UDD (foreign-owned). DAN1 + UDD = TOT — filter TOT when summing to avoid double-counting.
- No dim joins. All columns have inline coded values.