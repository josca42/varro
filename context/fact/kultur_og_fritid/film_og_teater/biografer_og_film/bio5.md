table: fact.bio5
description: Biograffilm efter biograffilm/billetter, filmkategori, type/målgruppe, censur, nationalitet og tid
measure: indhold (unit Antal)
columns:
- bio: values [5=Solgte billetter (1.000), 24=Film (antal)]
- filmkat: values [10=Foreviste film, 11=Årets premierefilm]
- typmal: values [27=Spillefilm og dokumentarfilm, alle målgrupper, 47=Spillefilm, alle målgrupper, 28=Spillefilm. voksne, 29=Spillefilm, børn/unge/familie, 48=Dokumentarfilm, alle målgrupper, 30=Dokumentarfilm voksne , 31=Dokumentarfilm, børn/unge/familie, 32=Uoplyst]
- censur: values [39=Alle censurforhold, 34=Tilladt for alle, 35=Frarådet  for børn under 7 år, 36=Tilladt for børn over 11 år, 37=Tilladt for børn over 15 år, 38=Over 15 år, ikke censureret]
- nation2: values [0=Alle lande, 5000=Danmark, 4998=Norden ekskl. Danmark, 4997=EU-27 udenfor Danmark, 4994=EU-28 udenfor Danmark, 4995=Europa udenfor Danmark, 4999=Udlandet i alt, 7100=Verden udenfor Europa og USA, 5390=USA]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- bio is a measurement selector. Filter to one: 5=Solgte billetter (1.000), 24=Film (antal). Never sum across bio values.
- filmkat: 10=Foreviste film (all screened films) vs 11=Årets premierefilm (new releases only). These are not additive — premierefilm is a subset of foreviste film. Filter to one.
- typmal has same two-level hierarchy as bio4ta: 27=all, 47=all spillefilm (28+29), 48=all dok (30+31), 32=uoplyst. Filter to one level.
- censur: 39=Alle is total. Sub-categories (34–38) add up to 39.
- nation2: 0=Alle lande is total. Note this table has fewer country options than bio4ta — only broad groupings (Norden, EU-27, Europa, USA, Verden udenfor Europa+USA).
- Has 5 dimension columns total; to get a simple total query: filmkat='10', typmal='27', censur='39', nation2='0', then pick bio.