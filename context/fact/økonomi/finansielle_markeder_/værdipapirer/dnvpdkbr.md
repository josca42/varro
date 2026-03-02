table: fact.dnvpdkbr
description: VP-registrerede papirer efter papirtype, valuta, udstederbranche, investorbranche, værdiansættelse, datatype og tid
measure: indhold (unit Mio. kr.)
columns:
- papir: values [11A=1. Aktier, i alt, 11N=1.1. Heraf noterede aktier, 20A=2. Obligationer, i alt, 20I=2.0.0.0.1. Heraf indeksobligationer, 21B=2.0.1. Statsobligationer og statsgældsbeviser, 21K=2.0.2. Skatkammerbeviser, 24A=2.0.3. Realkreditudstedelser, i alt, 25A=2.0.4. Andre obligationer end stats- og realkreditudstedelser, 30A=3. Investeringsforeningsbeviser, i alt, 30N=3.1. Heraf noterede investeringsforeningsbeviser]
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- udstedbranc: values [0000=Alle brancher, i alt, 1000=1. Alle indenlandske brancher, LAND=1.1 Landbrug, skovbrug og fiskeri, INDU=1.2 Industri, råstofindvinding og forsyningsvirksomhed, BYGG=1.3 Bygge og anlæg, HAND=1.4 Handel og transport mv., INKO=1.5 Information og kommunikation, FIFO=1.6 Finansiering og forsikring, 1212=1.6.1 Monetære finansielle institutioner (MFIer), 1256=1.6.2 Forsikring og pension samt andre finansielle formidlere m.m., IKFI=1.7 Ikke-finansielle holdingselskaber, EJEN=1.8 Ejendomshandel og udlejning, ERHV=1.9 Erhvervsservice, OFFE=1.10 Offentlig administration, undervisning og sundhed, KULT=1.11 Kultur, fritid og anden service, 2000=2 Udstedt af udlændinge]
- holbranc: values [0000=Alle brancher i alt, 100E=1.1 Erhvervsmæssige i alt, LAND=1.1.1 Landbrug, skovbrug og fiskeri, INDU=1.1.2 Industri, råstofindvinding og forsyningsvirksomhed, RAAS=1.1.2.1 Råstofindvinding ... KULT=1.1.11.1 Kultur og fritid, ANSE=1.1.11.2 Andre serviceydelser, hushold. med hjælp, 1ZX0=1.1.12 Ufordelt indland, 1430=1.2 Lønmodtagere, pensionister mv., 2000=2 Udland]
- vaerdian: values [B=Markedsværdi, N=Nominel værdi]
- data: values [1=Beholdning]
- tid: date range 2008-11-01 to 2025-09-01
dim docs: /dim/valuta_iso.md

notes:
- vaerdian is a measurement selector — doubles every row. Always filter to one: typically vaerdian='B' (markedsværdi). data only has one value (1=Beholdning) so no filtering needed there.
- valuta: Z01 (alle valutaer) is an aggregate code not in dim.valuta_iso. The ISO join works for specific currencies (DKK, EUR, USD, etc.) but not for Z01. Use valuta='Z01' directly for all-currency totals.
- udstedbranc and holbranc are inline coded (hierarchical branch codes). Both have aggregate totals: 0000=alle brancher. To avoid double-counting, filter to one hierarchy level: either the top-level codes (LAND, INDU, BYGG, etc.) or subtotals (1000=alle indenlandske), not both.
- papir has nested totals: 11A=aktier i alt includes 11N (noterede). 20A=obligationer i alt includes 20I, 21B, 21K, 24A, 25A. Pick one level.
- This is the current holdings-by-branch table (from 2008). Use this when you need to know which industries hold or issue which security types.