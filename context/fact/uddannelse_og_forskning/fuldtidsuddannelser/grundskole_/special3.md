table: fact.special3
description: Elever, grundskolen (efterskoler) efter specialundervisning og tid
measure: indhold (unit Antal)
columns:
- elev: values [0=Elever i alt, 5=Modtager ikke specialundervisning, 6=Modtager specialundervisning, uoplyst timetal]
- tid: date range 2011-01-01 to 2023-01-01

notes:
- Covers only efterskoler (residential continuation schools). For all grundskole types, use special1 or special2.
- Very minimal: elev (0=total, 5=ingen specialundervisning, 6=specialundervisning uoplyst timetal) × tid. Data ends 2023.