table: fact.skib32
description: Udenrigs færgetransport efter færgerute, enhed og tid
measure: indhold (unit -)
columns:
- faerge: values [10002=FÆRGERUTER I ALT, 10210=DANMARK-SVERIGE, 10215=København-Malmö, 10220=København-Landskrona, 10225=København-Helsingborg ... 10361=Esbjerg-Newcastle, 10362=DANMARK-FÆRØERNE, 10364=Hirtshals-Torshavn, 10365=Hanstholm-Torshavn, 10366=Esbjerg-Torshavn]
- enhed: values [8000=Dobbeltture, 8005=Passagerer, 1000, 8010=Personkm, 1000, 8015=Biler i alt, 8020=Personbiler, 8025=Busser, 8030=Lastvogne uden anhænger, 8035=Lastvogne med anhænger, 8040=Sættevogne med forvogn, 8045=Sættevogne uden forvogn, 8046=Modulvogntog med forvogn (2009 - ), 8048=Modulvogntog uden forvogn (2009 - ), 8050=Campingvogne, 8055=Motorcykler, knallerter, 8060=Cykler, 8065=Færgegods i alt, 1000 ton, 8075=Lastbilgods, 1000 ton, 8070=Banegods, 1000 ton, 8080=Andet gods, 1000 ton, 8085=Transportarbejde, 1000 tonkm]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- enhed is a measurement selector with 20 values spanning passengers, vehicles (by type), and freight tonnage — all in different units. Always filter to exactly one enhed value. Do not sum across enhed.
- faerge=10002 (FÆRGERUTER I ALT) is the pre-computed total. faerge also includes destination-group aggregate codes (e.g. 10210=DANMARK-SVERIGE) alongside individual routes (10215, 10220, etc.) — exclude these when summing individual routes.
- International ferry routes only. For domestic ferries use skib31 (annual) or skib33 (monthly).
- Annual data. For monthly resolution use skib34 (2000–2025).
