table: fact.foder3
description: Produktion af foder efter foderblanding, periode og tid
measure: indhold (unit Mio. kg)
columns:
- foder1: values [220=Foderblandinger i alt, 225=Kvægfoderblandinger i alt, 240=Kvægfoderblanding med lavt proteinindhold, undtagen til kalve, 245=Kalvefoderblanding med lavt proteinindhold, 230=Kvægfoderblanding med højt proteinindhold, undtagen til kalve ... 310=Andre foderblandinger i alt, 315=Mineralstoffoderblandinger i alt, 325=Mineralstoffoderblandinger til kvæg, 320=Mineralstoffoderblandinger til svin, 330=Diverse foderblandinger]
- periode: values [KAAR=Kalenderår, DAAR=Driftsår (1/7 - 30/6)]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- periode is a critical selector — not a breakdown, but two alternative ways to carve the same calendar: KAAR=Kalenderår (Jan–Dec), DAAR=Driftsår (1 Jul – 30 Jun, the traditional agricultural year). These are mutually exclusive periodizations of the same production. Always filter to exactly one. Use `periode='KAAR'` unless you specifically need the farm-year convention.
- foder1 has aggregate codes mixed with detail: 220=Foderblandinger i alt (grand total), 225=Kvægfoderblandinger i alt, 310=Andre foderblandinger i alt, 315=Mineralstoffoderblandinger i alt. Do not sum a subtotal and its components together.
- This table covers production of compound feed (foderblandinger), not total consumption. Use foder1/foder2 for consumption.