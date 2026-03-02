table: fact.fisk2
description: Danske fartøjers landing af fisk efter fangstområde, landingsplads, enhed, fiskeart og tid
measure: indhold (unit -)
columns:
- fangst: values [TOT=Fangst i alt, 3AN=Skagerak, 3AS=Kattegat, 4B=Nordsøen, 3BCD=Østersøen, OTH=Andre farvande]
- landing1: values [TOT=Landinger i alt, R84=Hovedstaden, R82=Midtjylland, R81=Nordjylland, R85=Sjælland, R83=Syddanmark, R86=EU uden Danmark, R87=Europa udenfor EU]
- tal: values [4=Landet vægt (kg.), 5=Levende vægt (kg.), 6=Landet værdi (kr.)]
- fisk: values [TOT=ALLE FISKEARTER, 00=1. TORSKEFISK, 01=1.1.  Torsk, 02=1.2. Torskefisk i øvrigt, 10=2. FLADFISK, 11=2.1. Rødspætte, 12=2.2. Tunge, 13=2.3. Fladfisk i øvrigt, 21=3. Sild, 22=4. Makrel, 31=5. Industrifisk, 40=6. KREBS OG BLØDDYR, 41=6.1. Dybvandsrejer, 42=6.2. Jomfruhummer, 43=6.3. Blåmusling, 44=6.4. Krebs- og bløddyr i øvrigt, 51=7. FISK I ØVRIGT]
- tid: date range 1996-01-01 to 2024-01-01

notes:
- fisk2 covers Danish vessels landing fish ANYWHERE (including abroad). landing1=R86 means Danish vessels landing in EU countries; R87 means landing outside EU. Contrast with fisk3 which covers all landings IN Denmark.
- tal is a measurement-type selector (4=Landet vægt kg, 5=Levende vægt kg, 6=Landet værdi kr). Filter to one tal — these are different units and cannot be summed.
- fisk has a two-level hierarchy: TOT is the grand total; category codes 00, 10, 21, 22, 31, 40, 51 are species groups; codes like 01, 02, 11-13, 41-44 are individual species within groups. Filter to one level (e.g. WHERE fisk IN ('00','10','21','22','31','40','51')) to avoid double-counting species within groups.
- fangst and landing1 both include TOT rows. Always filter to a specific area or explicitly include TOT to avoid summing areas + total.