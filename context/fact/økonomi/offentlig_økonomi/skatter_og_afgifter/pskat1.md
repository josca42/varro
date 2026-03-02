table: fact.pskat1
description: Skatteydernes indkomster og skatter efter type og tid
measure: indhold (unit Mio. kr.)
columns:
- type: values [A1=A.1. Danmarks befolkning ultimo året (1 000 personer), A11=A.1.1 Heraf under ligning (1 000 personer), A111=A.1.1 Antal skatteydere med overskydende skat mv. (1 000 personer), A112=A.1.2 Antal skatteydere med restskat mv. (1 000 personer), A113=A.1.3 Antal skatteydere uden overskydende skat/restskat (1 000 personer) ... H221=I.2.2.1 Til opkrævning via forskudssystemet, H222=I.2.2.2 Til opkrævning via slutsystemet, I1=J.1. Særlig indkomstskat i alt, I11=J.1.1 Til opkrævning, I12=J.1.2 Til udbetaling]
- tid: date range 1987-01-01 to 2023-01-01

notes:
- Despite the stated unit "Mio. kr.", some type codes report counts in 1.000 persons (any type with "personer" in the label, e.g. A1, A11, A111–A113). The unit header is misleading — always check the type label before interpreting indhold.
- type follows a letter-prefix hierarchy (A through I). Single-letter + digit codes are subtotals; longer codes are sub-items. Never sum types without checking the hierarchy — double-counting is easy. Navigate this table like a structured report, picking specific rows of interest.
- Use ColumnValues("pskat1","type") to browse all ~50 type codes with their labels.
