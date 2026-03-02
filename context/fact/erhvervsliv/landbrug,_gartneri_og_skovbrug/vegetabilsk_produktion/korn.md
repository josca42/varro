table: fact.korn
description: Anvendelsen af korn efter afgrøde, periode, oprindelse, type og tid
measure: indhold (unit Mio. kg)
columns:
- afgrode: values [A6=Korn i alt, H105=Hvede, H130=Rug, H140=Triticale, H145=Byg, H172=Havre og blandsæd, H615=Majs mv]
- periode: values [KAAR=Kalenderår, DAAR=Driftsår (1/7 - 30/6)]
- oprind: values [4=I alt dansk og importeret, 5=Dansk produceret, 10=Importeret]
- type: values [410=Høst efter svind, 415=Import, 420=Lagre primo, 425=udsæd, 430=Eksport, 435=Formaling til mel, gryn mv., 440=Industriformål, 445=Lagre ultimo, 450=Foderforbrug]
- tid: date range 1995-01-01 to 2024-01-01

notes:
- This table tracks the full grain balance sheet. type has 9 values covering both stocks (lagre primo/ultimo) and flows (høst, import, udsæd, eksport, formaling, industri, foder). These are conceptually different things — never sum all types together.
- periode distinguishes Kalenderår (KAAR) vs. Driftsår 1/7–30/6 (DAAR). Crucially, oprind=5 (Dansk) and oprind=10 (Importeret) only appear with DAAR. oprind=4 (I alt) appears with both KAAR and DAAR. If you use KAAR, you can only get oprind=4 (total). Filter periode consistently.
- afgrode=A6 (Korn i alt) is the aggregate across all grain types. Specific codes (H105, H130, H140, H145, H172, H615) are children. Don't sum A6 with the specific crops.
- No regional breakdown. National-level only.