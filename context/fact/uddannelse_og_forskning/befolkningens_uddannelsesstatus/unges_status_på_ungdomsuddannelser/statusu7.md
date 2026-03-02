table: fact.statusu7
description: 18-25 årige efter uddannelsesstatus, alder, gns. grundskolekarakter for dansk og matematik og tid
measure: indhold (unit Antal)
columns:
- uddstat: values [AA_TOTAL=Uddannelsesstatus i alt, FULDFOERT=Fuldført uddannelse, IGANG=Igangværende uddannelse, AFBRUDT=Afbrudt uddannelse, INGENREG=Ingen registreret uddannelse]
- alder: values [IALT=Alder i alt, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25=25 år]
- dkmat: values [0=I alt, 20=Mindre end 2, 21=2-4,99, 22=5-8,99, 23=9 eller mere, 99=Uoplyst]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- No dimension joins — all columns have inline values. dkmat=0 is "I alt" (total), dkmat=99 is "Uoplyst". 4 grade bands: 20 (<2), 21 (2–4.99), 22 (5–8.99), 23 (9+).
- 3 dimension columns (uddstat, alder, dkmat). To compare education outcomes by grade band: filter uddstat='AA_TOTAL', alder='IALT', then group by dkmat (exclude 0 to avoid total row).
- The grade measure is the average of the primary school exit grades in Danish and Math combined. Higher grades strongly predict continuation in upper secondary education.