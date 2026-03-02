table: fact.lbesk62
description: Lønmodtagere efter enhed, branche (DB07 19-grp), sektor, køn, herkomst og tid
measure: indhold (unit Antal)
columns:
- tal: values [1020=Lønmodtagere, 1010=Fuldtidsbeskæftigede lønmodtagere]
- branchedb0738: join dim.db on branchedb0738=kode::text
- sektor: join dim.esr_sekt on sektor::text=kode
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder, UDK=Uoplyst køn, uden bopæl i Danmark]
- herkomst: join dim.herkomst on herkomst=kode::text [approx]; levels [1]
- tid: date range 2008-01-01 to 2025-01-01
dim docs: /dim/db.md, /dim/esr_sekt.md, /dim/herkomst.md
notes:
- ALWAYS filter tal to one value: 1020=Lønmodtagere OR 1010=Fuldtidsbeskæftigede lønmodtagere. Forgetting this doubles all counts.
- WARNING: dim.db join for branchedb0738 is broken (0% match). Treat branchedb0738 as inline — see lbesk61 notes for letter-code labels.
- WARNING: dim.esr_sekt join for sektor is broken (0% match). sektor values same as lbesk61: 1000=total, 1032=Offentlig, 1035=Offentlige virksomheder, 1040=Private, 1045=Private nonprofit, 1050=Uoplyst. Treat as inline.
- WARNING: dim.herkomst join is mostly broken. herkomst uses: 1=Dansk, 24=Indvandrere vestlige, 25=Indvandrere ikke-vestlige, 34=Efterkommere vestlige, 35=Efterkommere ikke-vestlige, TOT=I alt, UDK=Uoplyst. Treat as inline.
- Data ends 2025-01. For more recent data use tables without the herkomst dimension.
