table: fact.frugt4
description: Nettoareal  og trætæthed for æbler og pærer efter enhed, sort, træernes alder og tid
measure: indhold (unit -)
columns:
- maengde4: values [2025=Nettoareal (ha), 2030=Trætæthed (træer pr. hektar (ha))]
- sort: values [100=Nettoareal og antal æbletræer pr. ha i alt, 105=Aroma inkl. røde typer, 110=Belle de Boskoop, 115=Bellida, 120=Cox Orange ... 215=Clara Frijs, 220=Concorde, 225=Conference, 230=Doyenne du Comice, 235=Andre pærer]
- tre: values [0=I alt, 4=0-4 år, 9=5-9 år, 10=10-14 år, 15=15-24 år, 24=Mere end 24 år]
- tid: date range 2002-01-01 to 2023-01-01
notes:
- sort has two subtotals that should never be summed with their constituents: 100="Nettoareal og antal æbletræer pr. ha i alt" (apple total) covers varieties 105–185; 200="Nettoareal og antal pæretræer pr. ha i alt" (pear total) covers varieties 205–235. Pick individual variety OR the total, never sum both.
- maengde4 is a measurement selector: 2025=Nettoareal (ha), 2030=Trætæthed (træer pr. hektar). Always filter to one — they have incompatible units.
- tre is tree age class: 0=I alt (all ages), 4=0–4 år, 9=5–9 år, 10=10–14 år, 15=15–24 år, 24=Mere end 24 år. Filter to tre=0 for age totals; summing individual age groups adds up to the tre=0 total.
- Table covers only apples and pears (not other fruit). For total apple nettoareal: WHERE sort=100 AND maengde4=2025 AND tre=0. For pear total: sort=200.
