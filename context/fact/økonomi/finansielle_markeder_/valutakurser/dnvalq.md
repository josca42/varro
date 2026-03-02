table: fact.dnvalq
description: Valutakurser efter valuta, kurstype, opgørelsesmetode og tid
measure: indhold (unit Indeks)
columns:
- valuta: join dim.valuta_iso on valuta=kode [approx]; levels [1]
- kurtyp: values [INX=Indeks (kun nominel effektiv kronekurs), indeks 1980=100, LOI=Timelønsindeks for industrien i Danmark, sæsonkor., indeks 1980=100, LOU=Vægtet timelønsindeks for industrien i udlandet, sæsonkor., indeks 1980=100, RET=Real effektiv kronekurs baseret på timelønninger, indeks 1980=100]
- opgoer: values [A=Kvartalsgennemsnit, B=Beregnet, Y=Årlig stigningstakt]
- tid: date range 1970-01-01 to 2025-04-01
dim docs: /dim/valuta_iso.md

notes:
- This table contains competitiveness indices only — no spot exchange rates. All values are index numbers (base 1980=100 or annual growth rates).
- Only 2 valuta codes: DKK (in dim.valuta_iso) and X00 (trade-weighted basket of foreign countries, not in dim). Never join to dim.valuta_iso for X00.
- kurtyp values: INX=nominal effective exchange rate index (DKK), RET=real effective exchange rate based on hourly wages (DKK), LOI=hourly wage index for Danish industry seasonally adjusted (DKK), LOU=weighted foreign hourly wage index (X00 only).
- opgoer is a required filter: A=quarterly average, B=calculated, Y=annual growth rate. Omit Y if you want levels, not growth rates.
- For a Denmark competitiveness trend: WHERE valuta='DKK' AND kurtyp='RET' AND opgoer='A'