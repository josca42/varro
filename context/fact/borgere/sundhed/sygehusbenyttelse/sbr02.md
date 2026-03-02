table: fact.sbr02
description: Sygehusbenyttelse i befolkningen efter varighed af ophold på sygehus, hoveddiagnosegruppe, akut/ikke-akut, alder, køn og tid
measure: indhold (unit Antal)
columns:
- varighed_af_ophold: values [200300=Ophold af alle varigheder, 200310=Ophold på under 12 timer, 200320=Ophold på 12 timer eller derover]
- diagnosehoved: values [20000=Diagnoser i alt, 20100=Visse infektiøse og parasitære sygdomme, 20200=Neoplasmer, 20300=Sygdomme i blod og bloddannende organer og visse sygdomme, som inddrager immunsystemet, 20400=Endokrine, ernæringsbetingede og metaboliske sygdomme ... 21800=Symptomer og abnorme fund IKA, 21900=Læsioner, forgiftninger og visse andre følger af ydre påvirkninger, 22000=Ydre årsager til skade, 22100=Faktorer af betydning for sundhedstilstand og kontakter med sundhedsvæsen, 22200=Ukendt/andet]
- akutejakut: values [IALT=Akut og ikke-akut, i alt, AKUT=Akut, IKKE-AKUT=Ikke-akut]
- alder: values [0000=Alder i alt, 0AAR=0 år, 0109=1-9 år, 1019=10-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8089=80-89 år, 90-=90 år og derover]
- kon: values [00=Køn i alt, M=Mænd, K=Kvinder]
- tid: date range 2017-01-01 to 2024-01-01

notes:
- Three independent selector columns all include "i alt" totals — always filter each to avoid overcounting: varighed_af_ophold=200300 (all durations), diagnosehoved=20000 (all diagnoses), akutejakut='IALT'.
- diagnosehoved contains 22 ICD-10 chapter groups plus a total (20000). These are mutually exclusive chapter codes — you can sum them to reconstruct the total, or filter to one chapter for disease-specific analysis.
- alder uses numeric codes (0000=total, 0AAR=0 år, 0109=1-9 år, ..., 90-=90+). Different scheme from sbr01 — no single-year ages here, only decade groups.
- To count admissions by diagnosis chapter for a given year (all ages, both sexes): WHERE varighed_af_ophold='200300' AND akutejakut='IALT' AND alder='0000' AND kon='00', GROUP BY diagnosehoved.