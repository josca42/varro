<fact tables>
<table>
id: scene01a
description: Produktioner og opførelser på danske teatre (egen scene) efter teaterkategori, aktivitet, genre og tid
columns: teattyp, aktivitet, genre, tid (time), indhold (unit Antal)
tid range: 2020/2021 to 2023/2024
</table>
<table>
id: scene01b
description: Tilskuere på danske teatre (egen scene) efter teaterkategori, aktivitet, genre og tid
columns: teattyp, aktivitet, genre, tid (time), indhold (unit Antal)
tid range: 2020/2021 to 2023/2024
</table>
<table>
id: scene02a
description: Produktioner på danske teatre efter teaterkategori, publikumsgruppe, scene, genre og tid
columns: teattyp, pubgrup, scene, genre, tid (time), indhold (unit Antal)
tid range: 2020/2021 to 2023/2024
</table>
<table>
id: scene03a
description: Opførelser på danske teatre efter teaterkategori, publikumsgruppe, scene, genre og tid
columns: teattyp, pubgrup, scene, genre, tid (time), indhold (unit Antal)
tid range: 2020/2021 to 2023/2024
</table>
<table>
id: scene04a
description: Tilskuere på danske teatre efter teaterkategori, publikumsgruppe, scene, genre og tid
columns: teattyp, pubgrup, scene, genre, tid (time), indhold (unit Antal)
tid range: 2020/2021 to 2023/2024
</table>
<table>
id: scene05a
description: Danske teatre efter teaterkategori, teatrets primære publikum og tid
columns: teattyp, teater, tid (time), indhold (unit Antal)
tid range: 2020/2021 to 2023/2024
</table>
<table>
id: scene06a
description: Udenlandske gæstespil på danske scener efter teaterkategori, aktivitet, genre, nationalitet og tid
columns: teattyp, aktivitet, genre, nation2, tid (time), indhold (unit Antal)
tid range: 2020/2021 to 2023/2024
</table>
<table>
id: scene07a
description: Danske teatres turne i udlandet efter teaterkategori, aktivitet, genre, land og tid
columns: teattyp, aktivitet, genre, land, tid (time), indhold (unit Antal)
tid range: 2020/2021 to 2023/2024
</table>
<table>
id: scene08a
description: Statsstøttede teatres økonomi efter teaterkategori, enhed og tid
columns: teattyp, enhed, tid (time), indhold (unit -)
tid range: 2015/2016 to 2023/2024
</table>
<table>
id: scene09a
description: Danske teatres turne i Danmark efter område, teaterkategori, aktivitet, genre og tid
columns: omrade, teattyp, aktivitet, genre, tid (time), indhold (unit Antal)
tid range: 2020/2021 to 2023/2024
</table>
<table>
id: scene10a
description: Aktivitet på danske teatre efter teaterkategori, publikumsgruppe, type, genre og tid
columns: teattyp, pubgrup, type, genre, tid (time), indhold (unit Antal)
tid range: 2015/2016 to 2023/2024
</table>
<table>
id: kv2sc1
description: Forbrug af scenekunst efter genre, køn, alder og tid
columns: genre, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2sc2
description: Forbrug af scenekunst efter adgang, køn, alder og tid
columns: adgang, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2sc3
description: Forbrug af scenekunst efter forestillingens placering, køn, alder og tid
columns: forstilplac, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2sc4
description: Scenekunstnere efter kunstnertype, køn, alder og tid
columns: ktyp, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2sc5
description: Barrierer for forbrug af scenekunst efter årsag, køn og tid
columns: aarsag, kon, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Two distinct groups: scene01a–10a are supply-side statistics from theatre operators (productions, performances, audience counts, finances); kv2sc1–5 are demand-side survey percentages from Kulturvaneundersøgelsen 2024 (consumption habits, access methods, barriers). Never mix the two groups.
- All scene tables cover 2020/2021–2023/2024, except scene08a and scene10a which go back to 2015/2016. For historical trends, use scene08a (finances) or scene10a (activity).
- teattyp hierarchy appears in every scene table: 100=alle teatre (total), 105=alle statsstøttede (aggregate of 115–144). Always filter to a single teattyp to avoid double-counting.
- Two different genre taxonomies: scene01a–09a use 11 specific genres (codes 165, 320–365); scene10a uses 6 broader groups (165,170,175,180,190,192). Cannot be directly compared.
- For productions + opørelser + tilskuere all in one table with longest series: scene10a (broader genre, from 2015/2016). For granular genre with separate measures: scene01a (produktioner/opørelser), scene01b (tilskuere by ticket type), scene04a (tilskuere by pubgrup + stationær/turné).
- For publikumsgruppe breakdown (voksne/unge/børn): scene02a (produktioner), scene03a (opørelser), scene04a (tilskuere).
- For regional breakdown of Danish tours: scene09a (only produktioner, niveau=2 landsdele). Supports choropleth via /geo/landsdele.parquet — merge on omrade=dim_kode, exclude omrade=0.
- For international: scene06a (foreign guests in Denmark, includes audience), scene07a (Danish tours abroad, no audience).
- For theatre economics (only statsstøttede): scene08a — enhed mixes 1000 kr. and antal teatre, always filter to one enhed.
- For number of theatres: scene05a.
- kv2sc survey tables (2024 only, all Pct.): kv2sc1=consumption by genre, kv2sc2=by access method, kv2sc3=location of performance, kv2sc4=practicing as performer, kv2sc5=barriers (non-consumers only). All percentage categories are non-exclusive — never sum across the primary dimension.