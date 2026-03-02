table: fact.bil71
description: Familiernes bilkøb (andele og fordelinger) efter enhed, socioøkonomisk status, købsmønster og tid
measure: indhold (unit Pct.)
columns:
- maengde4: values [50=Procentfordelingen, 60=Andel af det totale bilkøb]
- socio: values [100=I husholdningerne, 110=Selvstændige, 111=Selvstændige med ansatte, 112=Selvstændige uden ansatte, 130=Lønmodtagere i alt, 131=Topledere, 132=Lønmodtagere højeste niveau, 133=Lønmodtagere mellemniveau, 134=Lønmodtagere grundniveau, 135=Lønmodtagere i øvrigt, 136=Lønmodtagere uden nærmere angivelse, 500=Arbejdsløse , 505=Uden for arbejdsstyrken, 510=Uddannelsessøgende, 515=Pensionister i alt, 520=Folkepensionister, 522=Førtidspensionist, 525=Efterlønsmodtagere mv., 530=Øvrige uden for arbejdsstyrken, 535=Uoplyst socioøkonomisk gruppe]
- koebmoens: values [10000=Familier i alt, 10010=Familier der Ikke har købt bil i alt, 10020=Familier der har købt bil i alt, 10030=Familier der har købt 1 bil i alt, 10040=Familier der har købt personbil ... 10142=Familier der har købt 1 personbil og leaset 2 personbiler, 10144=Familier der har købt 2 varebiler og leaset 1 personbiler, 10146=Familier der har købt 1 varebil og leaset 2 personbiler, 10148=Familier der har købt 1 varebil, 1 personbil og leaset 1 personbil, 10149=Familier der har købt eller leaset mere end 3 biler]
- tid: date range 1999-01-01 to 2023-01-01
notes:
- maengde4 is a MEASUREMENT SELECTOR: always filter to 50 (within-socio-group %) OR 60 (share of all DK car purchases). Omitting doubles every row.
- socio is hierarchical (same as bil70): 100=total, 110=Selvstændige (parent of 111+112), 130=Lønmodtagere (parent of 131–136), 515=Pensionister (parent of 520+522+525). Never mix parent and child codes.
- koebtype splits series at 2006 same as bil70.
