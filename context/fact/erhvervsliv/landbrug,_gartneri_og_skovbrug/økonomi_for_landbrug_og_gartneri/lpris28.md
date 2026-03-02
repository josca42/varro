table: fact.lpris28
description: Prisindeks for jordbrugets salg og køb efter produkt, enhed og tid
measure: indhold (unit -)
columns:
- produkt: values [0=Jordbrugets bytteforhold, 5=Jordbrugets salgsprodukter i alt (1+2+3+4), 8=Vegetabilske salgsprodukter i alt (1+2), 10=Landbrugsprodukter (1+3+4), 12=1. Vegetabilske salgsprodukter, landbrug ... 610=6.1.5. Transportmidler i alt, 615=6.1.5.1. Traktorer, 620=6.1.5.2. Motorkøretøjer ekskl. traktorer, 625=6.2. Bygningsinvesteringer, 630=6.3. Grundforbedring]
- tal: values [178=Indeks (2020=100), 315=Ændring i forhold til året før (pct.)]
- tid: date range 2020-01-01 to 2024-01-01
notes:
- tal is a measurement selector: 178=Indeks (2020=100), 315=Ændring ift. året før (pct.). Always filter to ONE tal.
- Same produkt hierarchy as lpris22 (price indices 2020=100). Annual frequency, ends 2024.
- Use when you need year-over-year comparisons or annual index values. For quarterly resolution use lpris22.
