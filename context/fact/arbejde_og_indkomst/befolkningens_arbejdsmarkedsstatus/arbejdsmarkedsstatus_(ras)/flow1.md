table: fact.flow1
description: Befolkningens skift af socioøkonomisk status efter tidligere socioøkonomisk status, ny socioøkonomisk status, bevægelse, køn, alder og tid
measure: indhold (unit Antal)
columns:
- tidsocio: values [6=Selvstændige og medarbejdende ægtefæller, 15=Lønmodtager med ledelsesarbejde, 20=Lønmodtagere på højeste niveau, 25=Lønmodtagere på mellemniveau, 30=Lønmodtagere på grundniveau, 35=Andre lønmodtagere, 40=Lønmodtagere u.n.a., 50=Arbejdsløse, 55=Uden for arbejdsstyrken]
- nysocio: values [6=Selvstændige og medarbejdende ægtefæller, 15=Lønmodtager med ledelsesarbejde, 20=Lønmodtagere på højeste niveau, 25=Lønmodtagere på mellemniveau, 30=Lønmodtagere på grundniveau, 35=Andre lønmodtagere, 40=Lønmodtagere u.n.a., 50=Arbejdsløse, 55=Uden for arbejdsstyrken, 60=Ikke i befolkningen]
- bevaegelsev: values [1-2KVT=1. kvartal til 2. kvartal, 2-3KVT=2. kvartal til 3. kvartal, 3-4KVT=3. kvartal til 4. kvartal]
- kon: values [M=Mænd, K=Kvinder]
- alder: values [-16=Under 16 år, 16-19=16-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, OV69=Over 69]
- tid: date range 2020-01-01 to 2023-01-01

notes:
- bevaegelsev represents the transition period within a year: 1-2KVT=Q1→Q2, 2-3KVT=Q2→Q3, 3-4KVT=Q3→Q4. Each value is a different quarter-transition, not a duplicate measurement. Do not sum across bevaegelsev unless tracking annual mobility volume.
- tidsocio and nysocio together form a transition matrix. nysocio includes 60=Ikke i befolkningen (people who left Denmark). A row where tidsocio=nysocio means no change in status.
- Short time series: only 2020–2023.
- kon has NO total row (only M and K). tidsocio has 9 values (no total), nysocio has 10 (adds 60=emigrated/deceased).
- National level only. Use flow2 for municipality-level flow data (with simplified socio).
- tid is always January 1 of the year; the actual quarterly transitions happen during that calendar year.