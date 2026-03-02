table: fact.bevil04b
description: Offentlige kulturbevillinger på uddannelsesområdet efter kulturemne, formål, finansieringskilde, finansieringsart og tid
measure: indhold (unit Mio. kr.)
columns:
- kulturemne: join dim.kulturemner on kulturemne::text=kode [approx: Dimension uses K prefix for niveau-2 codes (K09 vs 9)]; levels [1]
- formal: values [1000=Alle formål, 1055=Forskellige tilskud - Den Jyske Sangskole (FL 21112352), 1500=Tilskud til filmformål mv. - Station Next (FL 21240370), 1705=Kunstakademiets Billedkunstskoler - Almindelig virksomhed (FL 21410910), 1710=Det Kgl. Danske Musikkonservatorium - Almindelig virksomhed (FL 21412110) ... 2356=Folkeoplysning mv. - Nye fællesskaber (FL 21210162), 3160=Budgetregulering - Udflytning af kunstneriske studiepladser (FL 21417965), 3270=Tilskud til filmformål mv. - Pulje til styrket uddannelse og kompetenceudvikling (FL 21240315), 3350=Forskellige tilskud til medieformål - Manuskriptskolen for Børnefiktion (FL 21814232), 2270=Folkeoplysning (kulturel aktstykke)]
- finans: values [405=OFFENTLIG I ALT, 401=Kommuner, 404=STATEN I ALT, 400=Finanslov - Kulturministeriet, 406=Finanslov - Øvrige ministerier, 402=Udlodningsmidler (Tips), 403=Licensmidler]
- finansart: values [0=I alt, 40=Anlæg, 41=Distribution, 43=Drift, 39=Personlig, 42=Projekt]
- tid: date range 2020-01-01 to 2025-01-01
dim docs: /dim/kulturemner.md

notes:
- Same kulturemne coding as bevil01b: smallint codes 0=I alt, 1–6=niveau-1 (match dim), 7–34=niveau-2 (use `'K'||LPAD(f.kulturemne::text, 2, '0') = d.kode`), 99=Uoplyst.
- Subset of bevil01b covering only uddannelsesrelaterede bevillinger. For overall cultural funding use bevil01b or bevil02.
- `finans` (405=all public, 404=all state) and `finansart` (0=I alt) have aggregate totals — filter to avoid double-counting.