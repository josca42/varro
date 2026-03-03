table: fact.regr55
description: Regionernes regnskaber efter region, hovedkonto, tværgående grupperinger, art og tid
measure: indhold (unit 1.000 kr.)
columns:
- regi07: join dim.nuts on regi07=kode; levels [1]
- funk1: values [11001=1.10.01 Somatiske sygehuse, 11002=1.10.02 Psykiatriske sygehuse og afdelinger, 12010=1.20.10 Almen lægehjælp, 12011=1.20.11 Speciallægehjælp, 12012=1.20.12 Medicin ... 46051=4.60.51 Øvrige omkostninger og indtægter, 46052=4.60.52 Interne forsikringspuljer, 46561=4.65.61 Renter m.v., 47099=4.70.99 Overførsel - Fælles formål og administration, 59099=5.90.99 Overførsel - Renter m.v.]
- tvgrp: values [10=010 Personale, 15=015 Servicejob, 16=016 Løntiskud, 17=017 Andet tilbud ved manglende overholdelse af kvote for løntilskudsstillinger, 18=018 Jobpræmie til regionale arbejdsgivere ... 810=810 Betalinger - andre regioner, 820=820 Betalinger - private sygehuse og institutioner, 830=830 Betalinger - kommuner, 840=840 Betalinger - staten, 888=888 Øvrige grupperinger i alt]
- art: values [UE=Udgifter excl. beregnede omkostninger, UI=Udgifter incl. beregnede omkostninger, TOT=I alt (netto), I=Indtægter, S0=0 Beregnede omkostninger ... S9=9 Interne udgifter og indtægter, 91=9.1 Overførte lønninger, 92=9.2 Overførte varekøb, 94=9.4 Overførte tjenesteydelser, 97=9.7 Interne indtægter]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- regi07 joins dim.nuts. Code 0 = national total (not in dim.nuts); codes 81-85 = 5 regions at niveau=1.
- tvgrp = 20 tværgående (cross-cutting) grouping codes: 10=Personale, 30=Hjælpemidler m.v., 110=IT-udgifter, 310-320=Byggeri, 410-420=Køb/salg af fast ejendom, 710-790=Betalinger til/fra private, 810-840=Betalinger til/fra andre sektorer (kommuner, stat etc.), 888=Øvrige grupperinger i alt. These cross-cuts are not mutually exclusive across the full account — do not sum across all tvgrp codes.
- funk1 has the same 110 detailed function codes as regr31. No aggregate funk1 total.
- art has the same hierarchy as regr31 (52 values, aggregates + detail). Filter to one art value.
- No prisenhed column — values are in 1.000 kr. directly.
- Best used to answer questions like "how much did regions spend on IT?" or "what were payments to municipalities?" — not for total expenditure (use regr31 for that).
- Map: /geo/regioner.parquet — merge on regi07=dim_kode. Exclude regi07=0.