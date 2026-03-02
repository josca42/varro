table: fact.lpris10
description: Salgspriser på udvalgte landbrugsprodukter efter produkt, enhed og tid
measure: indhold (unit -)
columns:
- produkt: values [1000=Hvede (kr. pr. 100 kg), 1005=Rug (kr. pr. 100 kg), 1010=Byg (kr. pr. 100 kg), 1015=Havre (kr. pr. 100 kg), 1020=Triticale (kr. pr. 100 kg) ... 1310=Sopolte, levende, 22 uger, notering (kr. pr. stk.) (2005-2017), 1315=Slagtekyllinger, levende vægt, notering (kr. pr. 100 kg), 1320=Mælk med faktisk fedt- og proteinprocent (kr. pr. 100 kg), 1325=Mælk, 4,2 pct. fedt og 3,4 pct. protein (kr. pr. 100 kg), 1360=Mink (kr. pr. skind)]
- enhed: values [320=Løbende priser, 200=Ændring i forhold til måneden før (pct.), 300=Ændring i forhold til samme måned året før (pct.)]
- tid: date range 2005-01-01 to 2025-08-01
notes:
- enhed is a measurement selector: 320=Løbende priser, 200=Ændring ift. måneden før (pct.), 300=Ændring ift. samme måned året før (pct.). Always filter to ONE enhed — every (produkt, tid) row appears three times.
- produkt codes include the unit in their label (kr. pr. 100 kg, kr. pr. stk., kr. pr. skind). Units differ across products — don't sum across produkt.
- Some products have limited time ranges noted in their titles (e.g., sopolte "(2005-2017)"). These products return no rows for tid after 2017.
- Monthly frequency, longest price series (from 2005). For annual aggregated sale prices use lpris32.
