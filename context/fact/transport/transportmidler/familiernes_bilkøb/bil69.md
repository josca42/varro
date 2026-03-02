table: fact.bil69
description: Familiernes bilkøb (andele og fordelinger) efter enhed, boligforhold, købsmønster og tid
measure: indhold (unit Pct.)
columns:
- maengde4: values [50=Procentfordelingen, 60=Andel af det totale bilkøb]
- bol: values [100=I husholdningerne, 110=Stuehuse til landbrugsejendomme, 120=Parcelhuse, 130=Række-, kæde- og dobbelthuse, 140=Etageboliger, 150=Kollegier, 610=Andre typer af boliger, 620=Ejerbolig, 630=Lejerbolig, 640=Uoplyst boligform]
- koebmoens: values [10000=Familier i alt, 10010=Familier der Ikke har købt bil i alt, 10020=Familier der har købt bil i alt, 10030=Familier der har købt 1 bil i alt, 10040=Familier der har købt personbil ... 10142=Familier der har købt 1 personbil og leaset 2 personbiler, 10144=Familier der har købt 2 varebiler og leaset 1 personbiler, 10146=Familier der har købt 1 varebil og leaset 2 personbiler, 10148=Familier der har købt 1 varebil, 1 personbil og leaset 1 personbil, 10149=Familier der har købt eller leaset mere end 3 biler]
- tid: date range 1999-01-01 to 2023-01-01
notes:
- maengde4 is a MEASUREMENT SELECTOR: always filter to 50 (within-housing-group %) OR 60 (share of all DK car purchases). Omitting doubles every row.
- bol has TWO parallel grouping schemes (boligtype: 110–610, ejerform: 620–640), plus bol=100 as total. Pick one scheme — see bil68 notes for details.
- koebtype splits series at 2006 same as bil68.
