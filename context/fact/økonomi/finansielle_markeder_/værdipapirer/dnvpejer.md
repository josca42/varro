table: fact.dnvpejer
description: Ejerkoncentration i realkreditobligationer efter ISIN og tid
measure: indhold (unit Koncentrationsmål)
columns:
- isin: values [1919=DK0000205089, 1=DK0002000181, 2=DK0002000264, 3=DK0002000348, 4=DK0002000421 ... 3311=LU1153686487, 3312=LU1153686560, 3313=LU1153686644, 3041=LU1157395655, 3227=LU1159240792]
- tid: date range 2005-01-01 to 2025-09-01

notes:
- isin is an integer surrogate key mapping to ISIN strings. Use ColumnValues("dnvpejer", "isin", fuzzy_match_str="DK0002...") to find specific bonds.
- indhold is a concentration measure (Koncentrationsmål), not Mio. kr. — do not sum across ISINs. Each row is the concentration index for one bond at one point in time.
- The table covers only realkreditobligationer (mortgage bonds), not other bond types.