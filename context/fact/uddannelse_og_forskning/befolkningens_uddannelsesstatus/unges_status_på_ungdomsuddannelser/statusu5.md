table: fact.statusu5
description: 18-25 årige efter uddannelsesstatus, alder, grundskoleinstitutionstype og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- alder: values [IALT=Alder i alt, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25=25 år]
- grundskol: values [0=I alt, 1011=Efterskoler, 1012=Folkeskoler, 1013=Friskoler og private grundskoler, 1014=Kommunale ungdomsskoler og ungdomskostskoler, 1015=Specialskoler for børn, 1016=Dagbehandlingstilbud og behandlingshjem, 1999=Andre skoler, 9999=Uoplyst]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- No dimension joins — all columns have inline values. grundskol=0 is "I alt" (total), grundskol=9999 is "Uoplyst". The 6 school types (1011–1999) range from efterskoler to kommunale ungdomsskoler to specialskoler.
- 3 dimension columns (uddstat, alder, grundskol). To compare school types: filter uddstat='AA_TOTAL', alder='IALT', then group by grundskol (exclude 0 to avoid double-counting with the total row).
- No uddannelse column — shows education status by primary school type only. Unique among statusu tables for this school-type breakdown.