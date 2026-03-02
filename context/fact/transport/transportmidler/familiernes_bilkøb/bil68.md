table: fact.bil68
description: Familiernes bilkøb (faktiske tal) efter købstype, boligforhold, købsmønster og tid
measure: indhold (unit Antal)
columns:
- koebtype: values [34=Nye biler (2006 - ), 33=Nye biler (1999 - 2005)]
- bol: values [100=I husholdningerne, 110=Stuehuse til landbrugsejendomme, 120=Parcelhuse, 130=Række-, kæde- og dobbelthuse, 140=Etageboliger, 150=Kollegier, 610=Andre typer af boliger, 620=Ejerbolig, 630=Lejerbolig, 640=Uoplyst boligform]
- koebmoens: values [10000=Familier i alt, 10010=Familier der Ikke har købt bil i alt, 10020=Familier der har købt bil i alt, 10030=Familier der har købt 1 bil i alt, 10040=Familier der har købt personbil ... 10142=Familier der har købt 1 personbil og leaset 2 personbiler, 10144=Familier der har købt 2 varebiler og leaset 1 personbiler, 10146=Familier der har købt 1 varebil og leaset 2 personbiler, 10148=Familier der har købt 1 varebil, 1 personbil og leaset 1 personbil, 10149=Familier der har købt eller leaset mere end 3 biler]
- tid: date range 1999-01-01 to 2023-01-01
notes:
- koebtype splits series at 2006 (same as bil64): 33=1999–2005, 34=2006–2023.
- bol has TWO parallel grouping schemes stored simultaneously. Summing all 10 codes (including total) multiplies counts by ~3. Pick one scheme:
  - Boligtype: 110=stuehuse, 120=parcelhuse, 130=rækkehuse, 140=etageboliger, 150=kollegier, 610=andre (sum=100 total)
  - Ejerform: 620=ejerbolig, 630=lejerbolig, 640=uoplyst (sum=100 total)
  bol=100 is the overall total ("I husholdningerne") common to both schemes.
- koebmoens same hierarchy as bil600.
