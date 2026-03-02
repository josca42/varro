table: fact.skib31
description: Indenrigs færgetransport efter færgerute, enhed og tid
measure: indhold (unit -)
columns:
- faerge: values [10002=FÆRGERUTER I ALT, 10006=Korsør-Nyborg, DSB, 10007=Korsør-Nyborg, Vognmandsruten, 10008=Halsskov-Knudshoved, 10009=Kalundborg-Juelsminde ... 10185=Hvalpsund-Sundsøre, 10190=Branden-Fur, 10195=Kleppen-Venø, 10200=Thyborøn-Agger, 10205=Esbjerg-Fanø]
- enhed: values [8000=Dobbeltture, 8005=Passagerer, 1000, 8010=Personkm, 1000, 8015=Biler i alt, 8020=Personbiler, 8025=Busser, 8030=Lastvogne uden anhænger, 8035=Lastvogne med anhænger, 8040=Sættevogne med forvogn, 8045=Sættevogne uden forvogn, 8046=Modulvogntog med forvogn (2009 - ), 8048=Modulvogntog uden forvogn (2009 - ), 8050=Campingvogne, 8055=Motorcykler, knallerter, 8060=Cykler, 8065=Færgegods i alt, 1000 ton, 8075=Lastbilgods, 1000 ton, 8070=Banegods, 1000 ton, 8080=Andet gods, 1000 ton, 8085=Transportarbejde, 1000 tonkm]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- enhed is a measurement selector with 20 values spanning passengers, vehicles (by type), and freight tonnage — all in different units. Always filter to exactly one enhed value. Do not sum across enhed.
- faerge=10002 (FÆRGERUTER I ALT) is the pre-computed total across all routes. Exclude when summing individual routes to avoid double-counting.
- Domestic ferry routes only. For international ferries use skib32 (annual 1990–2024) or skib34 (monthly 2000–2025).
- Annual data. For monthly resolution of the same domestic routes use skib33 (2000–2025).
