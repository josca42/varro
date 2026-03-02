table: fact.foder1
description: Foderforbruget efter fodermiddel, oprindelse, enhed og tid
measure: indhold (unit -)
columns:
- foder2: values [5=Foderforbrug i alt, 10=Kraftfoderforbrug i alt, 15=Korn til foder i alt, 20=Hvede, 25=Rug ... 195=Korn, helsædsensilage, 200=Græs og kløver i omdriften, 205=Græs og kløver udenfor omdriften, 210=Andet grøntfoder, 215=Halm]
- oprind: values [4=I alt dansk og importeret, 5=Dansk produceret, 10=Importeret]
- enhed: values [1F=Vægt (mio. kg), 2F=Foderværdi (mio. foderenheder), 4F=Ren råprotein (mio. kg.)]
- tid: date range 1990 to 2025

notes:
- tid is int4range — each row spans a two-year harvest window like [2023,2025). Filter with `WHERE tid @> 2024` to get the 2023/24 harvest year, or `WHERE lower(tid) = 2023`.
- enhed is a measurement selector: 1F=Vægt (mio. kg), 2F=Foderværdi (mio. foderenheder), 4F=Ren råprotein (mio. kg). Every foder2×oprind combination appears 3 times — one per enhed. Always filter to exactly one, e.g. `enhed='1F'`.
- oprind: 4=I alt (Danish + imported total), 5=Dansk produceret, 10=Importeret. Code 4 covers all foder2 items; codes 5 and 10 only cover items where the origin split exists. foder2=115 only appears with oprind=4 (no origin breakdown). Summing all three oprind values would triple-count totals.
- foder2 has a hierarchy: code 5 (Foderforbrug i alt) is the grand total, code 10 (Kraftfoderforbrug i alt) and 15 (Korn til foder i alt) are subtotals, and codes 20–215 are individual commodities. Do not sum aggregate codes with their components.
- To get total feed consumption by weight: `WHERE enhed='1F' AND oprind=4 AND foder2=5`.