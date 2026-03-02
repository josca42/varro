table: fact.dnbsk1
description: Transaktioner med kort i Danmark efter transaktionstype, kortudstedelsesland, datatype og tid
measure: indhold (unit -)
columns:
- transakt1: values [TOT=1. Total, POS=1.1. Point Of Sale (POS), CNP=1.2. Card Not Present (CNP)]
- kortudsted: values [TOT=1. Kort udstedt i alle lande, DK=1. 1. Kort udstedt i Danmark, UDL=1.2. Kort udstedt i alle lande ekskl. Danmark]
- data: values [BELOEB=Værdi (kr.), ANTAL=Antal (stk.)]
- tid: date range 2019-01-01 to 2025-10-12

notes:
- `data` uses different names than other tables in this group: BELOEB=Værdi (kr.) and ANTAL=Antal (stk.). Always filter to one.
- Both transakt1 and kortudsted have TOT aggregate codes. All 9 combinations (3×3) exist in the data. To get a single total: WHERE transakt1='TOT' AND kortudsted='TOT'. Summing without filtering will multiply counts by 3 on each axis.
- transakt1: POS=physical Point of Sale, CNP=Card Not Present (online/remote). TOT=POS+CNP aggregate.
- kortudsted: DK=Danish-issued, UDL=foreign-issued cards used in Denmark. TOT=DK+UDL aggregate.
- Note: values are in raw kr. and stk. (not 1.000 stk. or mio. kr. like other tables). Watch out when comparing with dnbstk or dnbsts.
- tid has daily precision (goes to 2025-10-12 vs quarterly for most others). Coverage starts 2019 vs 2016 for the rest — use dnbstk for older data.
- This is the only table that captures foreign-issued cards used in Denmark (kortudsted='UDL') alongside domestic cards — useful for total market coverage of Danish card terminals.