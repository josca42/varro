table: fact.dnprnd
description: Specifikation til Nationalbankens balance efter balance, instrument og tid
measure: indhold (unit Mia. kr.)
columns:
- balanc: values [A=Aktiv, N=Nettoaktiv, P=Passiv]
- instrument: values [IB=Indskudsbeviser (Jan. 2005 -), IR=Pengepolitiske indlån, nettoindestående på folio (Jan. 2005 -), NS=Penge- og realkreditinstitutters nettostilling over for Nationalbanken (Jan. 2005 -), UR=Pengepolitiske udlån total (Jan. 2005 - ), U7=Pengepolitiske udlån 7 dage (Apr. 2012), U6=Pengepolitiske udlån 6 måneder (24. Feb. 2012 - dec. 2014), P3=Pengepolitiske udlån 3 År (Apr. 2012 - 25. september 2015), XU=Ekstraordinære pengepolitiske udlån 7 dage (marts 2020 - ), X3=Ekstraordinære pengepolitiske udlån 3 mdr (marts 2020 - )]
- tid: date range 2005-01-03 to 2025-10-29

notes:
- Daily data on Nationalbanken's monetary policy instruments (indskudsbeviser, folio, pengepolitiske udlån etc.).
- balanc distinguishes balance sheet side: A=asset, P=liability, N=net. Don't sum across balanc values — they measure different sides of the same transactions.
- instrument: UR=total pengepolitiske udlån (= U7 + U6 + P3 + XU + X3). NS=nettostilling is a net figure. Don't sum UR with its sub-components.
- Some instruments only exist for sub-periods (date ranges noted in instrument labels). Queries spanning long periods will have NULLs for instruments not yet created.
- Unit is mia. kr. (billions).