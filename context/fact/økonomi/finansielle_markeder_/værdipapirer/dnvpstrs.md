table: fact.dnvpstrs
description: Strukturerede obligationer fordelt på forskellige karakteristika efter underliggende aktivtype, optionstyper, hovedstolsgaranti, løbetid (oprindelig løbetid), kupontype, værdiansættelse, datatype og tid
measure: indhold (unit Mio. kr.)
columns:
- uakt: values [T=Alle aktivtyper, A=Aktier, V=Valuta, I=Rente, R=Råvarer, X=Andet, M=Multi (kombination af de nævnte aktivtyper), Z=Ikke oplyst]
- opt: values [T=Alle optionstyper, A=Asiatisk, B=Basket, C=Capped/Floored, 1=Asiatisk + Basket, 2=Basket + Capped/Floored, 3=Asiatisk + Basket + Capped/Floored, Z=Øvrige kombinationer (inkl. plain vanilla)]
- hoved1: values [T=Alle papirer uanset hovedstolsgaranti, G=Hovedstolsgaranti 100 %, O=Hovedstolsgaranti over 100 %, D=Delvis hovedstolsgaranti (<100 %), I=Ingen hovedstolsgaranti, Z=Ikke oplyst]
- lobetid1: values [T=Alle løbetider/uspecificeret, 1=Oprindelig løbetid <= 1 år, 3=1 år < Oprindelig løbetid <= 3 år, 5=3 år < Oprindelig løbetid <= 5 år, 9=5 år < Oprindelig løbetid (inkl. uendelig løbetid)]
- kupon1: values [T=Alle kupontyper, N=Nulkuponobligation, F=Fast kuponrente (ekskl. nulkupon), V=Variabel kuponrente]
- vaerdian: values [B=Markedsværdi, N=Nominel værdi, U=Antal produkter/ISIN]
- data: values [8=Beholdning, 4=Nettotilgang, 9=Kursreguleringer (omvurderinger)]
- tid: date range 1999-12-01 to 2025-08-01

notes:
- vaerdian and data are measurement selectors that multiply rows. Filter both: vaerdian='B' (markedsværdi) or 'N' (nominel) or 'U' (antal ISIN produkter); data=8 (beholdning). Note: data codes here are 8/4/9, not 1/2/3 as in dnvpdks/dnvpu.
- data values: 8=Beholdning, 4=Nettotilgang, 9=Kursreguleringer — do not sum across these.
- All dimension columns have "T" (total/alle) as an aggregate value. For a simple total of all structured bonds: uakt='T', opt='T', hoved1='T', lobetid1='T', kupon1='T', vaerdian='B', data=8.
- vaerdian='U' gives count of products/ISINs (antal) rather than a monetary value — ensure correct interpretation when selecting this.
- This table is for karakteristika-breakdown of strukturerede obligationer. For investor-sector breakdown see dnvpstrh.