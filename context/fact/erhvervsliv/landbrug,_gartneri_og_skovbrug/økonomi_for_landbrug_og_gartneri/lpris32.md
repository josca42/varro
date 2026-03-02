table: fact.lpris32
description: Priser for jordbrugets salgsprodukter efter produkt, enhed og tid
measure: indhold (unit -)
columns:
- produkt: values [1000=Hvede (kr. pr. 100 kg), 1005=Rug (kr. pr. 100 kg), 1010=Byg (kr. pr. 100 kg), 1015=Havre (kr. pr. 100 kg), 1020=Triticale (kr. pr. 100 kg) ... 1334=Mælk, 4,2 pct. fedt og 3,4 pct. protein, konventionel (kr. pr. 100 kg), 1335=Buræg (kr. pr. 100 kg), 1340=Skrabeæg (kr. pr. 100 kg), 1345=Æg fra fritgående høns (kr. pr. 100 kg), 1350=Økologiske æg (kr. pr. 100 kg)]
- enhed: values [320=Løbende priser, 315=Ændring i forhold til året før (pct.)]
- tid: date range 2020-01-01 to 2024-01-01
notes:
- enhed is a measurement selector: 320=Løbende priser, 315=Ændring ift. året før (pct.). Always filter to ONE enhed.
- produkt codes include units in labels (kr. pr. 100 kg for grain, milk, eggs). Don't sum across produkt.
- Annual frequency (2020–2024). For monthly sale prices use lpris10 (longer series from 2005). This table adds organic egg price breakdowns (buræg, skrabeæg, fritgående, økologiske) and a conventional mælk distinction not in lpris10.
