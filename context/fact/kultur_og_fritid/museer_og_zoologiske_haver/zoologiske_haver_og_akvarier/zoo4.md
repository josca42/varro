table: fact.zoo4
description: Besøg i zoologiske haver og akvarier efter zookategori, zootype, besøgstype og tid
measure: indhold (unit Antal)
columns:
- zookat: values [740=Zoologiske haver og akvarier i alt, 745=Zoologiske haver, 750=Akvarier]
- zoo: values [TOT5=Zootype i alt, 00550=Statsstøttede i henhold til zooloven, 00530=Andre statsstøttede, 00540=Ikke-statsstøttede]
- besogstype: values [640=Besøg i udstillingen i alt, 695=12 år og derover, fuld pris, 700=12 år og derover, reduceret pris (fx årskort, rabat), 705=12 år og derover, undervisningsbesøg, 710=Under 12 år, undervisningsbesøg, 715=3-11 år, fuld pris, 720=3-11 år, reduceret pris (fx årskort, rabat), 725=Under 3 år, gratis, 730=Uspecificeret]
- tid: date range 2021-01-01 to 2024-01-01

notes:
- besogstype=640 (Besøg i udstillingen i alt) is exactly the sum of all other besogstype values (verified). Filter to besogstype=640 for total visits. Exclude it when breaking down by ticket type to avoid double-counting.
- besogstype values are mutually exclusive age/price categories that sum to the total (640). Safe to filter to any subset and sum.
- zookat=740 is total (zoos + aquaria), 745=zoos only, 750=aquaria only. zoo=TOT5 is grand total. Filter both to your target to avoid double-counting.
- This table is specifically for visitor breakdown by ticket type / age group. For other activity metrics (opening hours, events, revenue), use zoo3 instead.