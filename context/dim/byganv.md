# Bygningsanvendelse (byganv)

Bygningsanvendelseskoderne følger de koder, der findes i [Bygnings- og BoligRegistret (BBR)](https://teknik.bbr.dk/kodelister), men grupperes til statistiske formål. Bygningsanvendelsen har tre niveauer, hvoraf der kun offentliggøres på niveau et og to. Niveau tre er endnu ikke implementeret i offentliggørelsen af statistikken.

## Struktur

Niveau | Beskrivelse | Antal kategorier
--- | --- | ---
1 | Hovedgruppe | 3
2 | Undergruppe | 29
3 | Detailkode | 89

## Niveau 1 — Hovedgruppe

kode | titel
--- | ---
105 | Beboelsesbygninger
205 | Erhvervsbygninger
405 | Øvrige bygninger

## Hierarki-eksempel

kode | niveau | titel | parent_kode
--- | --- | --- | ---
105 | 1 | Beboelsesbygninger | NULL
110 | 2 | Stuehuse til landbrugsejendome | 105
110 | 3 | Stuehuse til landbrugsejendom | 110

## Brug

Simpel join:

```sql
SELECT f.indhold, d.titel
FROM fact.<fact_tabel> f
JOIN dim.byganv d ON f.byganv = d.kode
WHERE d.niveau = 1
```

Aggregering via parent_kode (fra fineste til groveste niveau):

```sql
SELECT top.titel, SUM(f.indhold)
FROM fact.<fact_tabel> f
  JOIN dim.byganv detail ON f.byganv = detail.kode AND detail.niveau = 3
  JOIN dim.byganv mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
  JOIN dim.byganv top ON top.kode = mid.parent_kode AND top.niveau = 1
GROUP BY top.titel
```
