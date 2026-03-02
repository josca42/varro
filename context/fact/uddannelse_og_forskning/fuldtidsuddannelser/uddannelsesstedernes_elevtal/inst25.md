table: fact.inst25
description: Kunstneriske og kulturelle uddannelsesinstitutioner efter status, institution, uddannelse, herkomst, køn, alder og tid
measure: indhold (unit Antal)
columns:
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- insti: values [TOT=I alt, 101428=101428 Danmarks Designskole, 101447=101447 Det Kgl. Danske Musikkonservatorium, 101456=101456 Det Kongelige Danske Kunstakademi - Billedkunstskolerne, 101458=101458 Den Danske Filmskole ... 621408=621408 Designskolen Kolding, 751426=751426 Arkitektskolen Aarhus, 751449=751449 Det Jyske Kunstakademi, 751454=751454 Kaospiloterne, 785401=785401 Vestervig Kirkemusikskole]
- uddannelse: values [TOT=I alt, H30=H30 Erhvervsfaglige uddannelser, H3055=H3055 Teknologiområdet, maskinteknik og produktion (TBT), H305570=H305570 Tekstil- og beklædningshåndværk, H3090=H3090 Andre erhvervsfaglige uddannelser ... H803065=H803065 Musik, Ph.d., H8039=H8039 Samfundsvidenskab, Ph.d., H803935=H803935 Politologi, Ph.d., H8090=H8090 Sundhedsvidenskab, Ph.d., H809050=H809050 Medicin, Ph.d.]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 9920=Under 20 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50OV=50 år og derover]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector — always filter to one value. B=elever pr. 1. oktober, F=fuldført, T=tilgang. Omitting this triples all sums.
- uddannelse spans erhvervsfaglige (H30xx), KVU (H40xx), MVU (H50xx), LVU (H70xx), and Ph.d. (H80xx) — kunstneriske institutioner offer programs across many levels. 2 hierarchy levels (5-char, 7-char) plus TOT.
- Small, specialized table: kunstakademier, musikkonservatorier, arkitektskoler, filmskolen, designskoler. Use ColumnValues("inst25", "insti") to see the full list.
- alder: TOT plus 8 age groups.
- kon total code is '10', not 'TOT'.