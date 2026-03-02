# Herkomst (herkomst)

Herkomst er baseret på oplysninger i Det Centrale Personregister (CPR). Personens egne oplysninger om fødested og statsborgerskab samt forældrenes oplysninger om fødested og statsborgerskab ligger til grund for definitionen.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Herkomsttype | 4

## Niveau 1 — Herkomsttype

kode | titel
--- | ---
1 | Personer med dansk oprindelse
2 | Indvandrere
3 | Efterkommere
9 | Uoplyst

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.amr2 f
JOIN dim.herkomst d ON f.herkomst = d.kode
WHERE d.niveau = 1
```
