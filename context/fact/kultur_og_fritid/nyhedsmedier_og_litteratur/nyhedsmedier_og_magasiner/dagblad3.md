table: fact.dagblad3
description: Dagblade efter nøgletal, geografisk dækning, læsertalsinterval og tid
measure: indhold (unit -)
columns:
- aktp: values [DB138=Dagblade (antal), DB140=Læsertal (Bruttodækning 1.000)]
- geodaek: values [DB143=Landsdækkende, DB144=Regionalt/lokalt]
- laesinterval: values [DB145=Alle læsere, DB146=under 20.000 læsere, DB147=20.000-49.999 læsere, DB148=50.000-99.999 læsere, DB149=100.000-199.999 læsere, DB150=200.000-399.999 læsere, DB151=400.000 læsere og derover]
- tid: date range 2018-01-01 to 2024-01-01

notes:
- aktp is a measurement selector: DB138=Dagblade (antal), DB140=Læsertal (Bruttodækning 1.000). Always filter to exactly one — never aggregate across both.
- laesinterval=DB145 (Alle læsere) is the total and equals the exact sum of all size buckets. For simple queries filter WHERE laesinterval='DB145'. Only use the size buckets (DB146-DB151) if you need the size distribution.
- geodaek has no total row — DB143=Landsdækkende and DB144=Regionalt/lokalt only. To get combined total, SUM across both.
- Sample: in 2024, DB138+DB143+DB145 = 9 landsdækkende dagblade; DB138+DB144+DB145 = 9 regionale/lokale dagblade.