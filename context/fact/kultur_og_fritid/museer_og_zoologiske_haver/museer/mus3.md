table: fact.mus3
description: Aktivitet på danske museers besøgssteder efter område, museumskategori, museumstype, aktivitet og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- museer: values [TOT5=Alle museer, 00335=Kulturhistoriske museer, 00350=Kunstmuseer, 00360=Naturhistoriske museer, 00365=Blandet kategori, 00375=Museumslignende institutioner (2012-)]
- afdling: values [TOT=Alle museer, 00510=Statslige i henhold til museumsloven, 00520=Statsanerkendte i henhold til museumsloven, 00530=Andre statsstøttede, 00540=Ikke-statsstøttede]
- aktivi: values [411=Besøgssteder, 420=Besøg i udstillingen, 430=Årlige åbningstimer, 435=Besøg på besøgsstedet]
- tid: date range 2016-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 2 (11 landsdele). Code '0' is a national total not in dim.nuts — exclude it or handle separately. Always filter to one niveau level to avoid double-counting: WHERE d.niveau = 1 for regioner, WHERE d.niveau = 2 for landsdele.
- aktivi is a measurement selector: 411=antal besøgssteder, 420=besøg i udstillingen, 430=åbningstimer, 435=besøg på besøgssted. Never sum across aktivi.
- museer=TOT5 and afdling=TOT are totals. Filter both for clean aggregation.
- Regional breakdown only covers besøgssted-level aktiviteter (no frivillige, entréindtægter etc.). For those, use mus1.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.