table: fact.km4
description: Kirkelige handlinger efter sogn, bevægelse og tid
measure: indhold (unit Antal)
columns:
- sogn: values [4001=4001 Esbjerg Personregisterfører, 4002=4002 Vejen Personregisterfører, 4003=4003 Kolding Personregisterfører, 4004=4004 Haderslev Personregisterfører, 4005=4005 Tønder Personregisterfører ... 9357=9357 Torkilstrup-Lillebrænde, 9358=9358 Gråsten-Adsbøl, 9359=9359 Søndbjerg-Odby, 0=0000 Uden placerbar adresse, 9999=9999 Uden fast bopæl]
- bevaegelsev: values [1=Døbte i sognets kirker, 2=Hjemmedøbte i sognet, 3=Døbte - anden dåb, 4=Fremstillede, 5=Vielser i sognet af pastoratets præst, 6=Vielser i sognet af anden præst i folkekirken, 7=Kirkelig velsignelser, 8=Lysninger, 9=Dødsfald registreret, 10=Begravet/bisat under medvirken af pastoratets præster fra sognets kirke, 11=Begravet/bisat under medvirken af pastoratets præster andetsteds end fra sognets kirker, 12=Begravet/bisat under medvirken af andre præster i folkekirken fra sognets kirker, 13=Begravet/bisat under medvirken af andre præster i folkekirken andetsteds end sognets kirke, 14=Begravet/bisat under medvirken af præster fra frimenigheder/andre trossamfund, 15=Begravet/bisat uden gejstlig medvirken, 16=Konfirmerede, 17=Fødte]
- tid: date range 2006-01-01 to 2024-01-01

notes:
- bevaegelsev selects which church event to count. Always filter to the specific event(s) you want — never sum all 17 values together, as they count entirely different things (births, deaths, baptisms, burials, confirmations, weddings).
- Burial sub-types (10–15) together sum to approximately bevaegelsev=9 (Dødsfald registreret). Do NOT include bevaegelsev=9 alongside 10–15 in a SUM — that double-counts deaths. Use 9 as the total, or 10–15 to break down by burial type.
- Total baptisms: bevaegelsev IN ('1','2','3'). Code 1 is by far the largest (church baptisms). Code 4 (Fremstillede) are emergency-baptized infants later presented at church — include if you want all baptism-related actions.
- Total church weddings: bevaegelsev IN ('5','6') — code 5 by parish priest, code 6 by another Church of Denmark priest.
- bevaegelsev=17 (Fødte) counts all births registered in the parish, not just baptisms. bevaegelsev=16 (Konfirmerede) counts confirmations.
- 2,302 distinct sogne. Codes 4001–4007 are "Personregisterfører" (civil registry) entries covering Sønderjylland, not actual parishes — consider excluding them for purely ecclesiastical questions. Codes 0000 and 9999 are residual (unknown/no fixed address). Use ColumnValues("km4", "sogn") to browse all sogne with their labels.
- To aggregate to a higher geographic level (provsti or stift), use km44 instead — km4 has no provsti column.
- Map: /geo/sogne.parquet — merge on sogn=dim_kode. Exclude sogn IN (0, 9999, 4001, 4002, 4003, 4004, 4005, 4006, 4007).