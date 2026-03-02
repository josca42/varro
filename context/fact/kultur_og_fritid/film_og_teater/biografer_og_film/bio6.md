table: fact.bio6
description: Biograffilm efter nøgletal, spilleuge, nationalitet, type/målgruppe og tid
measure: indhold (unit Pct.)
columns:
- aktp: values [60=Viste film, 61=Solgte billetter]
- spilleuge: values [00=Alle uger, 1U=1. Uge, 2U=2. uge, 3U=3. uge, 4U=4. uge ... 16U=16. uge, 17U=17. uge, 18U=18. uge, 19U=19. uge, 20U=20. uge]
- nation2: values [0=Alle lande, 5000=Danmark, 4998=Norden ekskl. Danmark, 4997=EU-27 udenfor Danmark, 4994=EU-28 udenfor Danmark, 4995=Europa udenfor Danmark, 7100=Verden udenfor Europa og USA, 5390=USA]
- typmal: values [27=Spillefilm og dokumentarfilm, alle målgrupper, 47=Spillefilm, alle målgrupper, 28=Spillefilm. voksne, 29=Spillefilm, børn/unge/familie, 48=Dokumentarfilm, alle målgrupper, 30=Dokumentarfilm voksne , 31=Dokumentarfilm, børn/unge/familie, 32=Uoplyst]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- Values are percentages and represent a cinema retention curve: what share of a film's total lifetime screenings (or tickets) occurred by a given week in its run. spilleuge=00 and spilleuge=1U both equal 100 (all films screened in week 1 = 100%); week 2 ≈ 97%, week 3 ≈ 94%, etc. Do NOT sum across spilleuge — each week is a cumulative share, not an independent slice.
- aktp is a measurement selector: 60=Viste film (pct. of films still being screened), 61=Solgte billetter (pct. of tickets sold by that week). Filter to one.
- typmal same two-level hierarchy as bio4ta/bio5. Filter to one level.
- nation2 has 0=Alle lande as total.
- Use this table for questions like "how quickly do Danish vs. American films leave cinemas" or "what share of tickets are sold in the first two weeks".