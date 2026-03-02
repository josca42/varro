table: fact.fagblad2
description: Fagblade efter nøgletal, udgivelsesfrekvens, branche, læsertalsinterval og tid
measure: indhold (unit Antal)
columns:
- aktp: values [DB140=Læsertal (Bruttodækning 1.000), DB172=Fagblade (antal)]
- udgivfrek: values [DB154=Ugentligt, DB155=Sjældnere end ugentligt]
- branche: values [K1=Landbrug, gartneri, skovbrug og fiskeri, K2=Fremstilling og industriel virksomhed, K3=Bygge og anlægsvirksomhed, K4=Engros-, detailhandel og indkøb, K5=Transport og kommunikation, K6=Tjenesteydelse, rådgivning og økonomi, K7=Offentlig virksomhed og undervisning, K8=Sundhed, behandling og pædagogik, K9=Fritid, foreninger og ideel virksomhed]
- laesinterval: values [DB145=Alle læsere, DB146=under 20.000 læsere, DB147=20.000-49.999 læsere, DB148=50.000-99.999 læsere, DB149=100.000-199.999 læsere, DB152=200.000-499.999 læsere, DB153=500.000 læsere og derover]
- tid: date range 2018-01-01 to 2024-01-01

notes:
- aktp is a measurement selector: DB140=Læsertal (Bruttodækning 1.000), DB172=Fagblade (antal). Always filter to exactly one.
- laesinterval=DB145 (Alle læsere) is the total. Use it for simple queries; DB146-DB153 are reader-count size buckets.
- branche has 9 industry categories (K1-K9), no total row. Not all branches appear in both udgivfrek — K1-K4 only appear in DB154 (Ugentligt), K5-K9 only in DB155 (Sjældnere). To get total across all branche, SUM WHERE laesinterval='DB145'.
- udgivfrek has no total row: DB154=Ugentligt, DB155=Sjældnere end ugentligt.
- To get total fagblade across everything: SUM(indhold) WHERE aktp='DB172' AND laesinterval='DB145'.