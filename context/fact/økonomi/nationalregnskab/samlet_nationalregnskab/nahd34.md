table: fact.nahd34
description: 3.1 Kapital, investering mv. (detaljeret) efter transaktion og tid
measure: indhold (unit Mio. kr.)
columns:
- transakt: values [B8GK=B.8g Bruttoopsparing, D9K=D.9r Modtaget kapitaloverførsler, D91K=D.91r Modtaget kapitalskatter, D92K=D.92r Modtaget investeringstilskud, D99K=D.99r Modtaget andre kapitaloverførsler, D9D=D.9p Betalt kapitaloverførsler, D91D=D.91p Betalt kapitalskatter, D92D=D.92p Betalt investeringstilskud, D99D=D.99p Betalt andre kapitaloverførsler, P51C4D=P.51c Forbrug af fast realkapital, B101GD=B.101 Ændringer i nettoformue forårsaget af opsparing og kapitaloverførsler, P51GD=P.51g Faste bruttoinvesteringer, P51C5D=P.51c Forbrug af fast realkapital, P52D=P.52 Lagerforøgelser, P53D=P.53 Anskaffelser minus afhændelser af værdigenstande, NPD=NP Anskaffelser af ikke-finansielle ikke-producerede aktiver, netto, B9D=B.9 Fordringserhvervelse, netto]
- tid: date range 1995-01-01 to 2024-01-01
notes:
- No prisenhed column (løbende priser only). Single measure per transakt×tid.
- 'Detaljeret' capital account from 1995 — covers savings, capital transfers (D.9), investment (P.51G), inventories (P.52), and net lending (B9D).
- Note P51C appears twice (P51C4D and P51C5D) representing the same depreciation figure in different accounting stages — pick one. B9D=fordringserhvervelse netto is the bottom-line balance.
