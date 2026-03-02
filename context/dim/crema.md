# Miljøøkonomiske aktiviteter (CReMA) (crema)

Ressourceforvaltningsaktiviteter (CReMA) fordeler udgifter og indtægter på aktiviteter, hvis primære formål er ressourceforvaltning.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Aktivitet | 7

## Niveau 1 — Aktivitet

kode | titel
--- | ---
1 | Forvaltning af vandressourcer
2 | Forvaltning af skovressourcer
3 | Forvaltning af dyreliv og planter
4 | Forvaltning af energiressourcer
5 | Forvaltning af mineralressourcer
6 | Forskning og udvikling inden for naturressourcer
7 | Anden ressourceforvaltning, herunder administration 

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.crema d ON f.crema = d.kode
WHERE d.niveau = 1
```
