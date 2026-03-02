# Sundhedsregnskaber efter funktion (ICHA-HC) (icha)

Dimensionstabel for sundhedsregnskaber efter funktion (icha-hc).

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedfunktion | 8
2 | Funktion | 25
3 | Underfunktion | 15

## Niveau 1 — Hovedfunktion

kode | titel
--- | ---
HC.1 | Behandling
HC.2 | Rehabilitering
HC.3 | Sygepleje og personlig pleje
HC.4 | Fritstående hjælpetjenester
HC.5 | Medicinske varer og hjælpemidler (uspecificerede)
HC.6 | Sundhedsfremme og forebyggelse
HC.7 | Sundhedsvæsenets styring, ledelse og administration
HC.9 | Andre sundhedsydelser og tjenester

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
HC.1 | 1 | Behandling | NULL
HC.1.1 | 2 | Behandling under indlæggelse | HC.1
HC.1.1.1 | 3 | Almen behandling under indlæggelse | HC.1.1

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.icha d ON f.icha = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.icha detail ON f.icha = detail.kode AND detail.niveau = 3
  JOIN dim.icha mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
  JOIN dim.icha top ON top.kode = mid.parent_kode AND top.niveau = 1
GROUP BY top.titel
```

## Relaterede tabeller

- **icha_hp**: Sundhedsregnskaber efter udbyder (ICHA-HP)
