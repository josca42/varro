table: fact.bil91
description: Familiernes bilrådighed (andele og fordelinger) efter enhed, socioøkonomisk status, rådighedsmønster og tid
measure: indhold (unit Pct.)
columns:
- maengde4: values [50=Procentfordelingen, 70=Andel af den totale bilrådighed]
- socio: values [100=I husholdningerne, 110=Selvstændige, 111=Selvstændige med ansatte, 112=Selvstændige uden ansatte, 130=Lønmodtagere i alt, 131=Topledere, 132=Lønmodtagere højeste niveau, 133=Lønmodtagere mellemniveau, 134=Lønmodtagere grundniveau, 135=Lønmodtagere i øvrigt, 136=Lønmodtagere uden nærmere angivelse, 500=Arbejdsløse , 505=Uden for arbejdsstyrken, 510=Uddannelsessøgende, 515=Pensionister i alt, 520=Folkepensionister, 522=Førtidspensionist, 525=Efterlønsmodtagere mv., 530=Øvrige uden for arbejdsstyrken, 535=Uoplyst socioøkonomisk gruppe]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10220=Familier med 1 bil i alt, 10230=Familier med personbil, 10240=Familier med firmabil, 10250=Familier med varebil, 10260=Familier med 2 biler i alt, 10270=Familier med 2 personbiler, 10280=Familier med 2 firmabiler, 10290=Familier med 2 varebiler, 10300=Familier med 1 personbil og 1 firmabil, 10310=Familier med 1 personbil og en varebil, 10320=Familier med 1 firmabil og 1 varebil, 10330=Familier med 3 biler i alt, 10340=Familier med flere end 3 biler]
- tid: date range 2000-01-01 to 2024-01-01
notes:
- maengde4 doubles all rows — always filter to one value: 50=Procentfordelingen, 70=Andel af den totale bilrådighed. Values are Pct.; do not SUM.
- socio has hierarchical sub-groups (100=total, 110/130/515/505 are sub-totals). See bil90 notes.
- raadmoens is hierarchical — pick one level.
