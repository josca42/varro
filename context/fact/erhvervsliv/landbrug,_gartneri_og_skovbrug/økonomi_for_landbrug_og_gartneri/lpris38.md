table: fact.lpris38
description: Priser for jordbrugets produktionsfaktorer efter produkt, enhed og tid
measure: indhold (unit -)
columns:
- produkt: values [1380=Vinterhvede, udsæd (kr. pr. 100 kg), 1385=Vårhvede, udsæd (kr. pr. 100 kg), 1390=Vinterrug, udsæd (kr. pr. 100 kg), 1392=Hybridrug, udsæd (kr. pr. 100 kg), 1395=Vinterbyg, udsæd (kr. pr. 100 kg) ... 1685=Arbejdsløn, Tarif B (kr. pr. time), 1690=Arbejdsløn, Tarif C (kr. pr. time), 1695=Forpagtningsafgift (kr. pr. ha), 1700=Ejendomsskatter (kr. pr. ha), 1705=Landbrugsjord, købspris (kr. pr. ha)]
- enhed: values [320=Løbende priser, 315=Ændring i forhold til året før (pct.)]
- tid: date range 2020-01-01 to 2024-01-01
notes:
- enhed is a measurement selector: 320=Løbende priser, 315=Ændring ift. året før (pct.). Always filter to ONE enhed.
- produkt covers production input/factor prices: seeds (udsæd), fertilizer (gødning), pesticides (pesticider), energy (olie, diesel), machinery (traktorer), labor (arbejdsløn), land (forpagtning, jordkøbspris). Units differ by produkt — check labels.
- Annual frequency (2020–2024). Counterpart to lpris32 (sale prices) — together they inform the terms-of-trade (lpris22/lpris28 code 0=Bytteforhold).
