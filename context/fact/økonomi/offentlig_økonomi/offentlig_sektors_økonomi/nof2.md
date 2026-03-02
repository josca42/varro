table: fact.nof2
description: Offentlig forvaltning og service efter forbrugsart, funktion, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- forbrugsart: values [P3S13=Offentlige forbrugsudgifter, P31S13=Offentlige individuelle forbrugsudgifter, P32S13=Offentlige kollektive forbrugsudgifter]
- funktion: join dim.cofog on funktion=kode::text [approx]
- prisenhed: values [V=Løbende priser, LAN=2020-priser, kædede værdier]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/cofog.md

notes:
- funktion uses CO-prefixed codes (CO01–CO10 for COFOG niveau=1, COT=total). To join dim.cofog: `JOIN dim.cofog d ON d.kode = REPLACE(f.funktion, 'CO', '')::INTEGER AND d.niveau = 1`. E.g. 'CO01'→1, 'CO10'→10. COT has no dim match — handle separately.
- forbrugsart: P3S13=Offentlige forbrugsudgifter i alt = P31S13 (individuelle) + P32S13 (kollektive). These 3 values cover the same expenditure at different granularities — never sum all 3. Filter to P3S13 for totals or use P31S13+P32S13 for the split.
- prisenhed is a measurement selector: V=Løbende priser, LAN=2020-priser. Every forbrugsart×funktion×tid row appears twice. Always filter to one.
- Annual (2015–2024). Cross-table of forbrugsart × COFOG function × price base.