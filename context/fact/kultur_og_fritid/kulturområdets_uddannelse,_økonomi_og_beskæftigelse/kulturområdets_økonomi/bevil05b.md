table: fact.bevil05b
description: Offentlige kulturbevillinger på forskningsområdet efter kulturemne, formål, finansieringskilde, finansieringsart og tid
measure: indhold (unit Mio. kr.)
columns:
- kulturemne: join dim.kulturemner on kulturemne::text=kode [approx: Dimension uses K prefix for niveau-2 codes (K09 vs 9)]; levels [1]
- formal: values [1000=Alle formål, 1530=Digitale fag- og forskningsbibliotek - Udvikling af digitale biblioteker (FL 21310420), 1675=Forskning på statslige og statsanerk museer - museers forskningskompetencer (FL 21334520), 2070=Formidling og kvalitet i forskning - Open Science og data management (FL 19460217), 2145=Fond til idrætsorganisationer mv. - Idrættens Analyseinstitut (FL 07181473), 2170=Fond til idrætsorganisationer mv. - Videnscenter om Handicap (FL 07181478), 3290=Statens Museum for Kunst - Tilskudsfinansieret forskningsvirksomhed (FL 21332195), 2200=Forskning på kulturinstitutioner (kulturel aktstykke), 2225=Kulturstatistik (kulturel aktstykke)]
- finans: values [405=OFFENTLIG I ALT, 401=Kommuner, 404=STATEN I ALT, 400=Finanslov - Kulturministeriet, 406=Finanslov - Øvrige ministerier, 402=Udlodningsmidler (Tips), 403=Licensmidler]
- finansart: values [0=I alt, 40=Anlæg, 41=Distribution, 43=Drift, 39=Personlig, 42=Projekt]
- tid: date range 2020-01-01 to 2025-01-01
dim docs: /dim/kulturemner.md

notes:
- Same kulturemne coding as bevil01b: smallint codes 0=I alt, 1–6=niveau-1 (match dim), 7–34=niveau-2 (use `'K'||LPAD(f.kulturemne::text, 2, '0') = d.kode`), 99=Uoplyst.
- Subset of bevil01b covering only forskningsrelaterede bevillinger. For overall cultural funding use bevil01b or bevil02.
- `finans` (405=all public, 404=all state) and `finansart` (0=I alt) have aggregate totals — filter to avoid double-counting.