table: fact.mms1
description: Miljøstøtte efter miljøkategori og tid
measure: indhold (unit Mio. kr.)
columns:
- miljokat: values [SUB05=Miljømotiverede subsidier i alt (1+2+3+4+5), SUB10=1. Forurening i alt, SUB100=1.1 Miljømæssig støtte til landbruget, SUB105=1.2 Støtte til grøn teknologi, SUB110=1.3 Ordninger for glas, papir og pap mv. ... SUB75=5. Bistand i alt, SUB80=5.1 CO2 kreditter i udviklingslande, SUB85=5.2 International miljø- og klimabistand, SUB90=5.3 International miljøstøtte til havmiljø, SUB95=5.4 Klimastøtte vedrørende Arktis]
- tid: date range 1995-01-01 to 2024-01-01

notes:
- miljokat is hierarchical: SUB05 = Miljømotiverede subsidier i alt (grand total, sum of 5 main categories). Main categories: SUB10=Forurening, SUB25=Energi, SUB45=Transport, SUB55=Naturforvaltning, SUB75=Bistand. Sub-codes (SUB100, SUB105...) are breakdowns within each main category. Don't mix levels in a SUM.
- For national total environmental subsidies: WHERE miljokat = 'SUB05'. For top-level split by type: WHERE miljokat IN ('SUB10','SUB25','SUB45','SUB55','SUB75').
- This is the aggregate table with no branche breakdown. For subsidies by industry, use mms3. For subsidies by CEPA environmental purpose, use mms2.