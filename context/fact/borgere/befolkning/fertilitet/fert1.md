table: fact.fert1
description: Samlet fertilitet (15-49 år) efter herkomst og tid
measure: indhold (unit Pr. 1.000 kvinder)
columns:
- herkomst: values [AK=Alle kvinder, IKV=Indvandrerkvinder fra vestlige lande, IKIV=Indvandrerkvinder fra ikke-vestlige lande, EKV=Efterkommerkvinder fra vestlige lande, EKIV=Efterkommerkvinder fra ikke-vestlige lande, DKK=Kvinder med dansk oprindelse]
- tid: date range 1986-01-01 to 2024-01-01

notes:
- Simple 2-column table (herkomst, tid). No joins needed.
- herkomst values are mutually exclusive groups: DKK (dansk oprindelse), IKV/IKIV (indvandrere fra vestlige/ikke-vestlige lande), EKV/EKIV (efterkommere fra vestlige/ikke-vestlige lande). AK=Alle kvinder is the national total.
- To get overall national fertility trend, filter herkomst='AK'. To compare by origin group, select the specific codes — do not sum them to get AK, use AK directly.