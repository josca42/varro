table: fact.bil66
description: Familiernes bilkøb (faktiske tal) efter købstype, indkomst, købsmønster og tid
measure: indhold (unit Antal)
columns:
- koebtype: values [34=Nye biler (2006 - ), 33=Nye biler (1999 - 2005)]
- indkom: values [01=I husholdningerne, 02=Under 50.000 kr, 3=50.000 - 74.999 kr., 4=75.000 - 99.999 kr., 5=100.000 - 124.999 kr. ... 10DC=10. decil, 1KV=1. kvartil, 2KV=2. kvartil, 3KV=3. kvartil, 4KV=4. kvartil]
- koebmoens: values [10000=Familier i alt, 10010=Familier der Ikke har købt bil i alt, 10020=Familier der har købt bil i alt, 10030=Familier der har købt 1 bil i alt, 10040=Familier der har købt personbil ... 10142=Familier der har købt 1 personbil og leaset 2 personbiler, 10144=Familier der har købt 2 varebiler og leaset 1 personbiler, 10146=Familier der har købt 1 varebil og leaset 2 personbiler, 10148=Familier der har købt 1 varebil, 1 personbil og leaset 1 personbil, 10149=Familier der har købt eller leaset mere end 3 biler]
- tid: date range 1999-01-01 to 2023-01-01
notes:
- koebtype splits series at 2006 (same as bil64): 33=1999–2005, 34=2006–2023.
- indkom has THREE parallel grouping schemes stored simultaneously in the same column (37 codes total). Pick exactly one scheme — summing all triples the total:
  - Absolute bands: 01=total, 02=<50k, 3=50k–75k, 4=75k–100k, 5=100k–125k, ..., 99=uoplyst
  - Deciles: 1DC–10DC (each ≈1/10 of total)
  - Quartiles: 1KV–4KV (each ≈1/4 of total)
  For a simple total without income breakdown use indkom='01'.
- koebmoens same hierarchy as bil600.
