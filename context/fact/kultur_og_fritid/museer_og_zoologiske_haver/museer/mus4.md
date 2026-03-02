table: fact.mus4
description: Besøg på museets udstilling efter museumskategori, museumstype, besøgstype og tid
measure: indhold (unit Antal)
columns:
- museer: values [TOT5=Alle museer, 00335=Kulturhistoriske museer, 00350=Kunstmuseer, 00360=Naturhistoriske museer, 00375=Museumslignende institutioner (2012-)]
- afdling: values [TOT=Alle museer, 00510=Statslige i henhold til museumsloven, 00520=Statsanerkendte i henhold til museumsloven, 00530=Andre statsstøttede, 00540=Ikke-statsstøttede]
- besogstype: values [640=Besøg i udstillingen i alt, 645=Voksne 18 år og derover, fuld pris, 650=Voksne 18 år og derover, reduceret pris, 655=Voksne 18 år og derover, gratis, 670=Børn og unge under 18 år, undervisningsbesøg, 675=Børn og unge under 18 år, ikke undervisningsbesøg, 730=Uspecificeret]
- tid: date range 2022-01-01 to 2024-01-01

notes:
- besogstype=640 is the total (Besøg i udstillingen i alt). 645+650+655+670+675+730 sum exactly to 640. Filter to 640 for a total, or use the detailed codes for breakdown by payment type and age group. Never sum all besogstype values — that doubles the total.
- museer=TOT5 and afdling=TOT are totals. Filter both for national figures.
- Only 3 years of data (2022-2024). For longer series on exhibition visits use mus1 (aktivitet=420, from 2009).