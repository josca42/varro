table: fact.bil6
description: Nyregistreringer, brugtvognshandel og bestand mv. efter køretøjstype, enhed og tid
measure: indhold (unit Antal)
columns:
- biltype: values [4000101002=Personbiler i alt, 1105=Personbiler i alt, benzin, 1110=Personbiler i alt, diesel, 4000101004=Personbiler i husholdningerne, 1115=Personbiler i husholdninger, benzin ... 2025=Traktorer over 5.000 kg, 4000103001=Campingvogne i alt, 2105=Campingvogne 0-1.000 kg, 2110=Campingvogne over 1.000 kg, 3000=Øvrige køretøjer]
- enhed: values [600=Nyregistreringer, 610=Genregistreringer, 620=Ejerskift, 630=Brugtvognshandel, 640=Afmeldinger, 650=Bestand]
- tid: date range 2000-01-01 to 2025-09-01
notes:
- enhed is the primary measurement selector: 600=Nyregistreringer, 610=Genregistreringer, 620=Ejerskift, 630=Brugtvognshandel, 640=Afmeldinger, 650=Bestand. Always filter to a single enhed — the same biltype×tid combination repeats once per enhed. Forgetting this multiplies counts by 6.
- biltype contains aggregate codes alongside subcategories (e.g., 4000101002=Personbiler i alt, plus 1105=personbiler benzin, 1110=personbiler diesel, etc.). Check for hierarchy: summing a parent + children for the same enhed+tid double-counts.
- This is the most comprehensive table for comparing registrations, used-car trade, and fleet stock side by side across vehicle types and fuel types. For a simpler view of just new registrations by vehicle type, bil5 is cleaner.
