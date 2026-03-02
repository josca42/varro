table: fact.bil70
description: Familiernes bilkøb (faktiske tal) efter købstype, socioøkonomisk status, købsmønster og tid
measure: indhold (unit Antal)
columns:
- koebtype: values [34=Nye biler (2006 - ), 33=Nye biler (1999 - 2005)]
- socio: values [100=I husholdningerne, 110=Selvstændige, 111=Selvstændige med ansatte, 112=Selvstændige uden ansatte, 130=Lønmodtagere i alt, 131=Topledere, 132=Lønmodtagere højeste niveau, 133=Lønmodtagere mellemniveau, 134=Lønmodtagere grundniveau, 135=Lønmodtagere i øvrigt, 136=Lønmodtagere uden nærmere angivelse, 500=Arbejdsløse , 505=Uden for arbejdsstyrken, 510=Uddannelsessøgende, 515=Pensionister i alt, 520=Folkepensionister, 522=Førtidspensionist, 525=Efterlønsmodtagere mv., 530=Øvrige uden for arbejdsstyrken, 535=Uoplyst socioøkonomisk gruppe]
- koebmoens: values [10000=Familier i alt, 10010=Familier der Ikke har købt bil i alt, 10020=Familier der har købt bil i alt, 10030=Familier der har købt 1 bil i alt, 10040=Familier der har købt personbil ... 10142=Familier der har købt 1 personbil og leaset 2 personbiler, 10144=Familier der har købt 2 varebiler og leaset 1 personbiler, 10146=Familier der har købt 1 varebil og leaset 2 personbiler, 10148=Familier der har købt 1 varebil, 1 personbil og leaset 1 personbil, 10149=Familier der har købt eller leaset mere end 3 biler]
- tid: date range 1999-01-01 to 2023-01-01
notes:
- koebtype splits series at 2006 (same as bil64): 33=1999–2005, 34=2006–2023.
- socio=100 is the grand total ("I husholdningerne"). The remaining codes are hierarchical: 110=Selvstændige (parent of 111+112), 130=Lønmodtagere i alt (parent of 131–136), 505=Uden for arbejdsstyrken (parent of 510+515+530+535). 515=Pensionister i alt (parent of 520+522+525). Never sum a parent code with its children — that double-counts. For a flat breakdown use: 110+130+500+505+535 (top-level groups only, check completeness by verifying sum≈socio=100).
- koebmoens same hierarchy as bil600.
