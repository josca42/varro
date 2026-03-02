table: fact.ligeui4
description: Ligestillingsindikator for modtagere af specialundervisning i grundskolen (offentlige skoler og specialområdet) efter indikator, klassetrin, herkomst og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1111=Drenge (pct.), LA2222=Piger (pct.), LA3333=Forskel mellem drenge og piger (procentpoint)]
- klasse: values [TOT=I alt, U20=U20 0. klassetrin, U21=U21 1. klassetrin, U22=U22 2. klassetrin, U23=U23 3. klassetrin, U24=U24 4. klassetrin, U25=U25 5. klassetrin, U26=U26 6. klassetrin, U27=U27 7. klassetrin, U28=U28 8. klassetrin, U29=U29 9. klassetrin, U30=U30 10. klassetrin]
- herkomst: values [TOT=I alt, 10=Personer med dansk oprindelse, 20=Indvandrere, 30=Efterkommere, 0=Uoplyst herkomst]
- tid: date range 2011-01-01 to 2024-01-01

notes:
- indhold is a percentage or percentage-point value, not a count. Never sum across rows or across indikator values.
- indikator is a rate selector: LA1111=Drenge (pct.), LA2222=Piger (pct.), LA3333=Forskel drenge minus piger (procentpoint). LA3333 = LA1111 − LA2222 — report indicators separately.
- herkomst coding differs from other tables in this subject: 10=dansk oprindelse, 20=indvandrere, 30=efterkommere (vs 5/4/3 in special1/2 and uddakt20). Use ColumnValues("ligeui4", "herkomst") to confirm codes.
- Covers only offentlige skoler og specialområdet (not private/free schools).