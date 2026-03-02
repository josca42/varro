<fact tables>
<table>
id: dagblad3
description: Dagblade efter nøgletal, geografisk dækning, læsertalsinterval og tid
columns: aktp, geodaek, laesinterval, tid (time), indhold (unit -)
tid range: 2018-01-01 to 2024-01-01
</table>
<table>
id: magasin2
description: Magasiner efter nøgletal, udgivelsesfrekvens, emne, læsertalsinterval og tid
columns: aktp, udgivfrek, boger, laesinterval, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2024-01-01
</table>
<table>
id: fagblad2
description: Fagblade efter nøgletal, udgivelsesfrekvens, branche, læsertalsinterval og tid
columns: aktp, udgivfrek, branche, laesinterval, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2024-01-01
</table>
<table>
id: avislas1
description: Avislæsere efter nøgletal, geografisk område og tid
columns: aktp, geoomr, tid (time), indhold (unit 1.000 personer)
tid range: 2018-01-01 to 2024-01-01
</table>
<table>
id: kv2nyh1
description: Forbrug af nyheder efter adgang, køn, alder og tid
columns: adgang, koen, alder1, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2nyh2
description: Forbrug af skriftlige medier og nyhedspodcasts efter adgang, køn, alder og tid
columns: adgang, koen, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2nyh3
description: Forbrug af nyheder efter nyhedsmedie, køn, alder og tid
columns: nymedie, koen, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2nyh4
description: Oplevelse af mis- eller desinformerende nyhedsindhold efter hyppighed, køn, alder og tid
columns: hyp, koen, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2nyh5
description: Barrierer for forbrug af nyheder efter årsag og tid
columns: aarsag, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Two table groups here: (1) press industry statistics (dagblad3, magasin2, fagblad2, avislas1) from 2018–2024 with annual data; (2) survey data on news consumption habits (kv2nyh1–5) from 2024 only, single time point.
- For how many dagblade/magasiner/fagblade exist and their readership over time: use dagblad3 (dagblade by geodaek+laesinterval), magasin2 (magasiner by emne+udgivfrek), or fagblad2 (fagblade by branche+udgivfrek). All share the same aktp measurement-selector pattern.
- For simple total avis-reader counts by geographic coverage: use avislas1 — simpler than dagblad3 (no laesinterval breakdown). avislas1 has geoomr=DB1440 as a geographic total; dagblad3 does not have a geographic total row.
- All press tables (dagblad3, magasin2, fagblad2, avislas1): aktp is a measurement selector (count vs. readership). Always filter to one aktp value. Never aggregate across both.
- For news consumption behaviour by gender/age: kv2nyh1 (general channels), kv2nyh2 (written media/podcasts access types), kv2nyh3 (by media type: local/national/public/commercial). All are 2024 survey percentages, NOT mutually exclusive across their main dimension — compare rows side by side, never sum.
- For misinformation experience: kv2nyh4. The 5 hyp values ARE mutually exclusive (~100% total) — they are response options to a single frequency question.
- For barriers to news consumption: kv2nyh5. aarsag values are NOT mutually exclusive (sum ~190%). No gender/age breakdown available.