table: fact.zoo3
description: Aktivitet i zoologiske haver og akvarier efter zookategori, zootype, aktivitet og tid
measure: indhold (unit Antal)
columns:
- zookat: values [740=Zoologiske haver og akvarier i alt, 745=Zoologiske haver, 750=Akvarier]
- zoo: values [TOT5=Zootype i alt, 00550=Statsstøttede i henhold til zooloven, 00530=Andre statsstøttede, 00540=Ikke-statsstøttede]
- aktivitet: values [400.0=Zoologiske anlæg (antal), 420.0=Besøg i udstillingen, 430.0=Årlige åbningstimer, 600.0=Formidlingsaktiviteter og undervisningsforløb, 605.0=Deltagere ved formidlingsaktiviteter og undervisningsforløb, 610.0=Lukkede arrangementer (ikke undervisning), 615.0=Deltagere ved lukkede arrangementer (ikke undervisning), 625.0=Frivillige, 630.0=Frivilligtimer, 635.0=Samlede entréindtægter inkl. årskort (kr.)]
- tid: date range 2021-01-01 to 2024-01-01

notes:
- aktivitet is a measurement-type selector — each value is a different metric in a different unit. Never sum across aktivitet values. To count visitors, filter aktivitet=420. For revenue (kr), filter aktivitet=635. For facility count, filter aktivitet=400.
- aktivitet=635 (entréindtægter, kr) has only 45 rows vs 48 for the other aktivitet values — a few zoo/zookat combinations are missing for 2024.
- There are 12 NULL aktivitet rows, only in 2021. They represent a different visitor count (not identical to aktivitet=420). These rows have no label and should be excluded from time-series analysis to keep consistency: WHERE aktivitet IS NOT NULL.
- zookat=740 is the total (zoos + aquaria combined), 745=zoologiske haver only, 750=akvarier only. zoo=TOT5 is the grand total across funding types. Filter both to avoid double-counting: e.g. WHERE zookat=745 AND zoo='00550' for state-subsidised zoos only.
- Typical query pattern: SELECT tid, indhold FROM fact.zoo3 WHERE zookat=740 AND zoo='TOT5' AND aktivitet=420 ORDER BY tid — total visits across all categories over time.