table: fact.raav
description: Industriens køb af råvarer, komponenter og hjælpestoffer efter varegruppe (6 cifre), enhed og tid
measure: indhold (unit -)
columns:
- vargr6: values [100.0=000100 Ikke fordelte varer, 200.0=000200 Handelsvarer, 10100.0=010100 Heste, æsler, muldyr og mulæsler, levende, 10201.0=010201 Hornkvæg, racerene avlsdyr, levende, 10290.0=010290 Hornkvæg, levende, undtagen avlsbrug ... 961600.0=961600 Rafraichisseurer og lignende til toiletbrug, bortset fra parfumerafraichisseurer, der har ka, 961700.0=961700 Termoflasker og andre termobeholdere med vakuumisolering, komplette med udvendigt hylster; d, 961800.0=961800 Mannequinfigurer og lignende mekaniske figurer og andet bevægeligt udstillingsmateriel til b, 969000.0=969000 Diverse, ikke specificeret, 990000.0=990000 I alt køb af råvarer]
- enhed: values [V=Værdi (1000 kr.), P=Andel i pct. af omsætning]
- tid: date range 2002-01-01 to 2023-01-01

notes:
- enhed is a selector: V=Værdi (1.000 kr.), P=Andel i pct. af omsætning. Always filter to one — mixing doubles/triples counts. For most value queries use enhed='V'.
- vargr6 is hierarchical: 990000=grand total (I alt), 100=Ikke fordelte varer, 200=Handelsvarer, 5-digit codes=chapter-level aggregates, 6-digit codes=detail. Filter to one level to avoid double-counting.
- vargr6 codes stored without leading zeros: the code "010100" is stored as 10100. ColumnValues returns these as floats (e.g. 10100.0=010100 Heste...) — cast to int or use LIKE comparisons if needed.
- No branche07 column — this table covers all of manufacturing industry's purchases aggregated. Use raav1 if you need industry sub-sector breakdown.