table: fact.svin
description: Svinebestanden den 1. i  kvartalet efter type og tid
measure: indhold (unit 1.000 stk.)
columns:
- type: values [D29=Svin i alt, D181=Søer i alt, D18=Avlsorner, D25=Sopolte (50 kg-) til avl, D19=Gylte (1. gangs drægtige), D20=Drægtige søer, andre, D23=Goldsøer, D22=Diegivende søer, D223=Pattegrise hos søer, D226=Fravænnede svin under 50 kg., D28=Slagtesvin, 50- kg, D282=Orner og søer til slagtning, D291=Sæsonkorrigerede tal, svin i alt]
- tid: date range 1998-01-01 to 2025-07-01

notes:
- indhold is in 1.000 stk. (thousands), not individual animals.
- type has 13 codes but D291=Sæsonkorrigerede tal, svin i alt was discontinued after 2019 — only 12 codes appear for post-2019 queries. Use D29=Svin i alt for the unadjusted total.
- type values are hierarchical: D29=Svin i alt contains all subtypes. D181=Søer i alt contains D18+D25+D19+D20+D23+D22 (all individual sow categories). D223+D226 are piglets/weaners. Don't sum all type codes.
- No geographic or farm-size breakdown — national quarterly totals only. For regional svin data use hdyr07 or komb07.