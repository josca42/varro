table: fact.ligehi10
description: Ligestillingsindikator for tilskadekomne og dræbte i færdselsuheld efter indikator, personskade, indblandede transportmidler, alder og tid
measure: indhold (unit -)
columns:
- indikator: values [M1=Mænd (pr. 100.000), K1=Kvinder (pr. 100.000), F1=Forskel mellem mænd og kvinder (point, pr. 100.000)]
- uheld: values [0=Personskade i alt, 1=Dræbte, 2=Alvorligt tilskadekomne, 3=Lettere tilskadekomne]
- indbland: values [0=I alt, 11=Almindelig personbil, 12=Taxi, 13=Køretøj 0-3.500 kg under udrykning, 21=Varebil 0-3.500 kg., 31=Lastbil over 3.500 kg., 33=Bus, 41=Motorcykel, 45=Knallert 45, 50=Knallert, 61=Cykel, 71=Fodgænger, 99=Andre]
- alder: values [IALT=Alder i alt, 9917=0-17 år, 1824=18-24 år, 2544=25-44 år, 4564=45-64 år, 6599=65 år og derover, 9999=Uoplyst alder]
- tid: date range 1998-01-01 to 2024-01-01
notes:
- indhold is a RATE (per 100,000 inhabitants), not a count. Unit is "-". Never sum across rows — each value is an independent rate.
- indikator has 3 values: M1=rate for men, K1=rate for women, F1=point difference (M1–K1). These are independent indicators; summing them is meaningless.
- uheld=0 (Personskade i alt), indbland=0 (I alt), and alder='IALT' are aggregates — filter to one value per dimension.
- To compare men vs women in traffic fatalities: WHERE uheld='1' AND indbland='0' AND alder='IALT', then compare M1 vs K1 rows.
- F1>0 means men have a higher rate; F1<0 means women have a higher rate. A negative F1 at certain transport modes (e.g., cycling) would indicate women are overrepresented.
- alder='IALT' is the all-ages aggregate (unlike other tables that use numeric codes for totals).
