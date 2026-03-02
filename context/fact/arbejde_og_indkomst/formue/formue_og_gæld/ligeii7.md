table: fact.ligeii7
description: Ligestillingsindikator for median nettoformue efter indikator, alder, familietype og tid
measure: indhold (unit -)
columns:
- indikator: values [LAK1=Mænd (kr.), LAK2=Kvinder (kr.), LAF3=Formuegab (pct.)]
- alder: values [IALT=Alder i alt, 1829=18-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover]
- famtyp: values [FAMIALT=Familier i alt, ENL=Enlige, PAF=Parfamilier]
- tid: date range 2014-01-01 to 2023-01-01

notes:
- Mixed units across indikator — never sum or average across indikator values: LAK1=mænd median nettoformue (kr.), LAK2=kvinder median nettoformue (kr.), LAF3=formuegab (pct., how much lower women's wealth is relative to men's).
- Filter to one indikator per query. For LAF3 (gap percentage), a higher value means a larger gender gap.
- alder='IALT' is the total; famtyp='FAMIALT' is total across family types. Filter both unless breaking out.
- Pre-computed gender gap indicator — use this table instead of joining two formue11 queries when the question is specifically about the gender gap.
