table: fact.mus5
description: Aktivitet uden for museets adresse efter museumskategori, museumstype, aktivitet og tid
measure: indhold (unit Antal)
columns:
- museer: values [TOT5=Alle museer, 00335=Kulturhistoriske museer, 00350=Kunstmuseer, 00360=Naturhistoriske museer, 00375=Museumslignende institutioner (2012-)]
- afdling: values [TOT=Alle museer, 00510=Statslige i henhold til museumsloven, 00520=Statsanerkendte i henhold til museumsloven, 00530=Andre statsstøttede, 00540=Ikke-statsstøttede]
- aktivitet: values [660=Arrangementer uden for museets adresse, 665=Deltagere til arrangementer uden for museets adresse i alt, 670=Børn og unge under 18 år, undervisningsbesøg, 675=Børn og unge under 18 år, ikke undervisningsbesøg, 680=Voksne 18 år og derover eller uspecificeret, 685=Onlinearrangementer, 690=Deltagere til onlinearrangementer]
- tid: date range 2022-01-01 to 2024-01-01

notes:
- aktivitet mixes counts and participant subtotals: 660=antal arrangementer i alt, 665=deltagere i alt (sum of 670+675+680), 670/675/680=deltager subtypes by age, 685=antal onlinearrangementer, 690=deltagere til onlinearrangementer. Never sum across aktivitet.
- 665 covers physical participants (670+675+680); 690 covers online participants. To get all participants, use 665+690 — do not use 660 or 685 (those count events, not people).
- museer=TOT5 and afdling=TOT are totals. Filter both for national figures.