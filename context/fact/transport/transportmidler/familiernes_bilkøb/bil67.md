table: fact.bil67
description: Familiernes bilkøb (andele og fordelinger) efter enhed, indkomst, købsmønster og tid
measure: indhold (unit Pct.)
columns:
- maengde4: values [50=Procentfordelingen, 60=Andel af det totale bilkøb]
- indkom: values [01=I husholdningerne, 02=Under 50.000 kr, 3=50.000 - 74.999 kr., 4=75.000 - 99.999 kr., 5=100.000 - 124.999 kr. ... 10DC=10. decil, 1KV=1. kvartil, 2KV=2. kvartil, 3KV=3. kvartil, 4KV=4. kvartil]
- koebmoens: values [10000=Familier i alt, 10010=Familier der Ikke har købt bil i alt, 10020=Familier der har købt bil i alt, 10030=Familier der har købt 1 bil i alt, 10040=Familier der har købt personbil ... 10142=Familier der har købt 1 personbil og leaset 2 personbiler, 10144=Familier der har købt 2 varebiler og leaset 1 personbiler, 10146=Familier der har købt 1 varebil og leaset 2 personbiler, 10148=Familier der har købt 1 varebil, 1 personbil og leaset 1 personbil, 10149=Familier der har købt eller leaset mere end 3 biler]
- tid: date range 1999-01-01 to 2023-01-01
notes:
- maengde4 is a MEASUREMENT SELECTOR: always filter to 50 (within-income-group %) OR 60 (share of all DK car purchases). Omitting doubles every row.
- indkom has THREE parallel grouping schemes (absolute bands, deciles 1DC–10DC, quartiles 1KV–4KV). Filter to exactly one scheme. indkom='01' is the overall total.
- koebtype splits series at 2006 same as bil64/bil66.
