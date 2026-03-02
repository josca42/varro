table: fact.strfsoc2
description: Skyldige personer efter overtrædelsens art, socioøkonomisk status og tid
measure: indhold (unit Antal)
columns:
- overtraed: join dim.overtraedtype on overtraed=kode [approx]; levels [1, 3]
- socio: join dim.socio on socio=kode::text [approx]; levels [3]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/overtraedtype.md, /dim/socio.md
notes:
- overtraed covers ONLY Straffelov — both niveau 1 and 3 appear as separate rows. Filter by niveau to avoid double-counting (same as strfudd2).
- socio uses simplified custom codes, not standard SOCIO13. Treat as inline categorical: TOT=I alt, 111=Selvstændige, 200=Lønmodtagere, 210=Arbejdsløse, 310=Studerende, 315=Pensionister mv., 900=Øvrige personer. Do not rely on dim.socio join for a full breakdown.
