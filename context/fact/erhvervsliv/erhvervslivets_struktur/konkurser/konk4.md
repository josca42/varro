table: fact.konk4
description: Erklærede konkurser efter branche, virksomhedstype og tid
measure: indhold (unit Antal)
columns:
- branche: values [000=Konkurser i alt, 1=Landbrug, skovbrug og fiskeri, 2=Industri, råstofindvinding og forsyningsvirksomhed, 3=Bygge og anlæg, 4=Handel og transport mv., G=Handel, G01=Handel med biler og motorcykler, G02=Engroshandel, G03=Detailhandel, H=Transport, I=Hoteller og restauranter, 101=Hoteller mv., 102=Restauranter, 5=Information og kommunikation, 6=Finansiering og forsikring, 7=Ejendomshandel og udlejning, 8=Erhvervsservice, 9=Offentlig administration, undervisning og sundhed, 10=Kultur, fritid og anden service, 11=Uoplyst aktivitet]
- virktyp1: values [K01=Konkurser i alt, K02=Konkurser i aktive virksomheder, K03=Konkurser i nulvirksomheder]
- tid: date range 2009-01-01 to 2025-09-01

notes:
- virktyp1 is a measurement selector: K01=total, K02=aktive virksomheder, K03=nulvirksomheder. K01 = K02 + K03. Always filter to one value — summing all three inflates counts 3x.
- branche uses a custom inline hierarchy, not dim.db. 000=national total, then 10 broad sectors (1–11). Sector 4 (Handel og transport) is further split: G/G01/G02/G03 for Handel subgroups and H for Transport. Sector I (Hoteller og restauranter) splits into 101/102. These subgroups overlap with their parent — pick one level of granularity and don't mix.
- For a clean sector breakdown use branche IN ('1','2','3','4','5','6','7','8','9','10','11') and virktyp1='K01'. To drill into Handel/Transport detail, replace '4' with G01/G02/G03/H.
- Prefer konk15 when you need fine-grained DB07 industry detail — konk4 only has ~20 coarse categories. konk4 has a broad-sector custom breakdown; konk15 has full niveau-5 DB07 detail.