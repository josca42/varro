table: fact.lpris22
description: Prisindeks for jordbrugets salg og køb efter produkt, enhed og tid
measure: indhold (unit -)
columns:
- produkt: values [0=Jordbrugets bytteforhold, 5=Jordbrugets salgsprodukter i alt (1+2+3+4), 8=Vegetabilske salgsprodukter i alt (1+2), 10=Landbrugsprodukter (1+3+4), 12=1. Vegetabilske salgsprodukter, landbrug ... 610=6.1.5. Transportmidler i alt, 615=6.1.5.1. Traktorer, 620=6.1.5.2. Motorkøretøjer ekskl. traktorer, 625=6.2. Bygningsinvesteringer, 630=6.3. Grundforbedring]
- tal: values [178=Indeks (2020=100), 210=Ændring i forhold til kvartalet før (pct.), 310=Ændring i forhold til samme kvartal året før (pct.)]
- tid: date range 2020-01-01 to 2025-04-01
notes:
- tal is a measurement selector: 178=Indeks (2020=100), 210=Ændring ift. kvartal før (pct.), 310=Ændring ift. samme kvartal året før (pct.). Always filter to ONE tal.
- Values are price indices (2020=100), not actual prices. Do not sum across produkt — indices are not additive.
- produkt has a deep hierarchy: bytteforhold (0), aggregate categories (5, 8, 10, 12…), and detailed sub-items. Code 0=Jordbrugets bytteforhold is the terms-of-trade ratio (salg/køb). Filter to specific level.
- Quarterly frequency. For annual equivalents use lpris28 (same produkt, same tal codes but annual, through 2024).
