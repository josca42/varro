table: fact.ligehi5a
description: Ligestillingsindikator for døde efter indikator, dødsårsag, alder og tid
measure: indhold (unit -)
columns:
- indikator: values [M1=Mænd (pr. 100.000), K1=Kvinder (pr. 100.000), F1=Forskel mellem mænd og kvinder (point, pr. 100.000)]
- arsag: values [TOT=I ALT, A02=A-02 Kræft, A06=A-06 Psykiske lidelser og adfærdsmæssige forstyrrelser, A07=A-07 Sygdomme i nervesystemet og sanseorganerne, A0809=A-08-09 Sygdomme i kredsløbsorganer, A10=A-10 Sygdomme i åndedrætsorganer, A11=A-11 Sygdomme i fordøjelsesorganer, A19=A-19 Ulykker, A20=A-20 Selvmord og selvmordsforsøg, OVR=Øvrige dødsårsager og uoplyst]
- alder: values [TOT=Alder i alt, 0=0 år, 1-4=1-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-=85 år og derover]
- tid: date range 2007-01-01 to 2022-01-01

notes:
- indhold is a rate per 100,000 — NOT a count of deaths. Never SUM or aggregate indhold values.
- indikator is a measurement selector: M1=mænd rate, K1=kvinder rate, F1=forskel (M1 minus K1). Always filter to a single indikator value. F1 is already a derived difference — don't subtract M1-K1 yourself.
- arsag here is a reduced subset (10 causes) compared to doda1/dodb1's full taxonomy. Use ColumnValues("ligehi5a", "arsag") to see available causes.
- alder is grouped (same ranges as doda1). Filter alder='TOT' for all-ages rates.
- Use this table for gender equality comparisons in mortality rates, not for absolute death counts.