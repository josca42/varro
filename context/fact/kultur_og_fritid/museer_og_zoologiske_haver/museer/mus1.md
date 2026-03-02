table: fact.mus1
description: Aktivitet på danske museer efter museumskategori, museumstype, aktivitet og tid
measure: indhold (unit Antal)
columns:
- museer: values [TOT5=Alle museer, 00335=Kulturhistoriske museer, 00350=Kunstmuseer, 00360=Naturhistoriske museer, 00365=Blandet kategori, 00370=Andre museer (-2011), 00375=Museumslignende institutioner (2012-)]
- afdling: values [TOT=Alle museer, 00510=Statslige i henhold til museumsloven, 00520=Statsanerkendte i henhold til museumsloven, 00530=Andre statsstøttede, 00540=Ikke-statsstøttede]
- aktivitet: values [410=Museer, 420=Besøg i udstillingen, 430=Årlige åbningstimer, 435=Besøg på besøgsstedet, 625=Frivillige, 630=Frivilligtimer, 635=Samlede entréindtægter inkl. årskort (kr.)]
- tid: date range 2009-01-01 to 2024-01-01

notes:
- aktivitet is a measurement selector — each code measures a different thing: 410=antal museer, 420=besøg i udstillingen, 430=åbningstimer, 435=besøg på besøgssted, 625=frivillige, 630=frivilligtimer, 635=entréindtægter (kr.). Never sum across aktivitet.
- museer=TOT5 (alle museer) and afdling=TOT (alle) are totals. Filter both when computing national figures. Category codes in museer and afdling are mutually exclusive subsets.
- Typical visit query: WHERE museer='TOT5' AND afdling='TOT' AND aktivitet='420' gives national exhibition visits by year.
- Revenue (aktivitet=635) is in kr. despite the "Antal" unit label — treat separately from visit/hour counts.