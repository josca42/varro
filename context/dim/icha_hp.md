# Sundhedsregnskaber efter udbyder (ICHA-HP) (icha_hp)

Dimensionstabel for sundhedsregnskaber efter udbyder (icha-hp).

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedudbyder | 9
2 | Udbyder | 24
3 | Underudbyder | 8

## Niveau 1 — Hovedudbyder

kode | titel
--- | ---
HP.1 | Hospitaler
HP.2 | Boligfaciliteter med langtidspleje
HP.3 | Ambulante aktører
HP.4 | Udbydere af fritstående hjælpetjenester
HP.5 | Apoteker og detailhandlere
HP.6 | Aktører indenfor sundhedsfremme og forebyggelse
HP.7 | Sundhedsmyndigheder og sygeforsikringsselskaber
HP.8 | Resten af økonomien
HP.9 | Resten af verden

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
HP.3 | 1 | Ambulante aktører | NULL
HP.3.1 | 2 | Praksissektoren | HP.3
HP.3.1.1 | 3 | Almen praksis | HP.3.1

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.icha_hp d ON f.icha_hp = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.icha_hp detail ON f.icha_hp = detail.kode AND detail.niveau = 3
  JOIN dim.icha_hp mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
  JOIN dim.icha_hp top ON top.kode = mid.parent_kode AND top.niveau = 1
GROUP BY top.titel
```

## Relaterede tabeller

- **icha**: Sundhedsregnskaber efter funktion (ICHA-HC)
