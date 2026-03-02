table: fact.kv2bib1
description: Seneste besøg på biblioteket efter formål, køn, alder og tid
measure: indhold (unit Pct.)
columns:
- formaaal: values [40100=Lån eller aflevering af fysiske bøger, aviser eller magasiner, 40110=Lån eller aflevering af DVD'er, konsolspil eller CD'er, 40120=Børneaktiviteter, 40130=Foredrag, undervisning, kursus eller koncert, 40140=Læse, studere eller mødes med andre, 40150=Finde information eller inspiration til læsning, 40160=Hjælp til informationssøgning, IT-vejledning o.lign., 40170=Print og scanning, 40180=Andre formål]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 1624=16-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 75OV=75 år og derover]
- tid: date range 2024-01-01 to 2024-01-01
notes:
- Survey data (percentage of library visitors indicating each purpose for their most recent visit). Only 2024, no geographic breakdown.
- formaaal values are NOT mutually exclusive — respondents could indicate multiple purposes. Never sum percentages across formaaal; each value is an independent rate.
- kon: 10=Køn i alt, 1=Mænd, 2=Kvinder (numeric codes — different from ibib/fstrib tables which use M/K/TOT).
- alder covers 16+ only (16-24 through 75+). No children's data.
- To get a national rate for a given purpose: WHERE formaaal='40100' AND kon=10 AND alder='TOT'.
