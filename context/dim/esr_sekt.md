# Erhvervsstatistiske sektorer (ESR) (esr_sekt)

Dimensionstabel for erhvervsstatistiske sektorer (esr).

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedsektor | 4
2 | Delsektor | 45

## Niveau 1 — Hovedsektor

kode | titel
--- | ---
INT | Internationale organisationer
OFF | Offentlig forvaltning og service
UOP | Uoplyst
VIR | Virksomheder og organisationer

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
VIR | 1 | Virksomheder og organisationer | NULL
11 | 2 | Statslige ikke-finansielle kvasi-selskaber | VIR

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.esr_sekt d ON f.esr_sekt = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.esr_sekt detail ON f.esr_sekt = detail.kode AND detail.niveau = 2
  JOIN dim.esr_sekt top ON top.kode = detail.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
