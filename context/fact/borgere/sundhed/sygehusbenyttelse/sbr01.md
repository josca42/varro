table: fact.sbr01
description: Sygehusbenyttelse i befolkningen efter kommune, ophold på sygehus, alder, køn og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [3]
- ophold_pa_sygehus: values [200100=Personer i alt, 200110=Alle varigheder (antal personer med ophold på sygehus), 200220=Ophold på sygehus på under 12 timer (antal patienter), 200230=Ophold på sygehus på 12 timer eller derover (antal patienter), 200240=Personer uden ophold på sygehus (antal)]
- alder: values [TOT=Alder i alt, 0=0 år, 1-4=1-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-=85 år og derover]
- kon: values [00=Køn i alt, M=Mænd, K=Kvinder]
- tid: date range 2017-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- kommunedk joins dim.nuts at niveau=3 (98 kommuner). Code 0 = "Hele landet" (national total) is not in dim.nuts — exclude it when doing municipal analysis: WHERE f.kommunedk != 0, or simply JOIN dim.nuts which drops it naturally.
- ophold_pa_sygehus is a category selector with overlapping semantics. 200100 = full population (i alt); 200110 = persons with any hospital stay (unique persons); 200220/200230 = patient contacts (admissions, not unique persons — a person can appear in both); 200240 = persons WITHOUT a stay. Never sum across these codes. To count persons hospitalised: use 200110. To split by duration: 200220 (<12h) and 200230 (≥12h) are admission counts, not person counts.
- alder uses text codes (TOT, 0, 1-4, 5-9, ..., 85-) and kon uses 00/M/K. Filter alder='TOT' and kon='00' when you want national totals.
- To count hospitalised persons by municipality for a given year: WHERE ophold_pa_sygehus='200110' AND alder='TOT' AND kon='00' AND tid='2023-01-01', then JOIN dim.nuts d ON f.kommunedk=d.kode WHERE d.niveau=3.
- Map: /geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.