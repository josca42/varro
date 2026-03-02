table: fact.fisk3
description: Landinger af fisk i Danmark efter fangstområde, landingsplads, enhed, fiskeart og tid
measure: indhold (unit -)
columns:
- fangst: values [TOT=Fangst i alt, 3AN=Skagerak, 3AS=Kattegat, 4B=Nordsøen, 3BCD=Østersøen, OTH=Andre farvande]
- landing1: values [TOT=Landinger i alt, R84=Hovedstaden, R82=Midtjylland, R81=Nordjylland, R85=Sjælland, R83=Syddanmark, R86=EU uden Danmark, R87=Europa udenfor EU]
- tal: values [4=Landet vægt (kg.), 5=Levende vægt (kg.), 6=Landet værdi (kr.)]
- fisk: values [TOT=ALLE FISKEARTER, 00=1. TORSKEFISK, 01=1.1.  Torsk, 02=1.2. Torskefisk i øvrigt, 10=2. FLADFISK, 11=2.1. Rødspætte, 12=2.2. Tunge, 13=2.3. Fladfisk i øvrigt, 21=3. Sild, 22=4. Makrel, 31=5. Industrifisk, 40=6. KREBS OG BLØDDYR, 41=6.1. Dybvandsrejer, 42=6.2. Jomfruhummer, 43=6.3. Blåmusling, 44=6.4. Krebs- og bløddyr i øvrigt, 51=7. FISK I ØVRIGT]
- tid: date range 1996-01-01 to 2024-01-01

notes:
- fisk3 covers all fish LANDED IN DENMARK, including by foreign vessels. Contrast with fisk2 which covers Danish vessels landing anywhere. For "how much fish came into Danish ports" use fisk3; for "how much did Danish fishers catch" use fisk2.
- landing1=R86 in fisk3 means EU vessels (other than Danish) landing in Denmark; R87 means non-EU vessels landing in Denmark.
- Same structure as fisk2: tal is a unit selector (4=Landed weight, 5=Live weight, 6=Landed value) — filter to one.
- fisk species codes have two hierarchy levels (groups 00/10/21/22/31/40/51 vs individual species). Filter to one level to avoid double-counting.
- fangst and landing1 both have TOT rows — filter or group carefully.