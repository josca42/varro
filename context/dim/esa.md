# Sektorer i nationalregnskabet (ESA) (esa)

Dimensionstabel for sektorer i nationalregnskabet (esa).

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedsektor | 6
2 | Delsektor | 18
3 | Undersektor | 24

## Niveau 1 — Hovedsektor

kode | titel
--- | ---
S.11 | Ikke-finansiel selskabssektor
S.12 | Finansiel selskabssektor
S.13 | Offentlig forvaltning og service
S.14 | Husholdningssektoren
S.15 | Nonprofit-institutioner rettet mod husholdninger (NPIsH)
S.2 | Udlandet

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
S.12 | 1 | Finansiel selskabssektor | NULL
S.122 | 2 | Pengeinstitutter, undtagen centralbanken | S.12
S.12201 | 3 | Offentige pengeinstitutter, undtagen centralbanken | S.122

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.esa d ON f.esa = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.esa detail ON f.esa = detail.kode AND detail.niveau = 3
  JOIN dim.esa mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
  JOIN dim.esa top ON top.kode = mid.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
