table: fact.auk03
description: Offentligt forsørgede (aktiverede fuldtidsmodtagere) efter område, ydelsestype, køn, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- ydelsestype: values [AKTOT=Aktivering i alt, AKD=Aktiverede dagpengeberettigede, TVED=Vejledning- og opkvalificering i alt (dagpengeberettigede), MED=Mentorstøtte (dagpengeberettigede), SVD=6 ugers selvvalgt uddannelse (dagpengeberettigede), VPD=Virksomhedspraktik (dagpengeberettigede), LTD=Ansættelse med løntilskud (dagpengeberettigede), NYD=Nytteindsats (dagpengeberettigede), ROD=Jobrotation (dagpengeberettigede), AKK=Kommunal aktivering i alt, TVEK=Vejledning- og opkvalificering ialt (Kontanthjælpsberettigede) , MEK=Mentorstøtte (kontanthjælpsberettigede), VPK=Virksomhedspraktik (kontanthjælpsberettigede), LTK=Ansættelse med løntilskud (kontanthjælpsberettigede), NYK=Nytteindsats (kontanthjælpsberettighede), ROK=Jobrotation (kontanthjælpsberettigede, FO=Forsøg (kontanthjælpsmodtagere)]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- tid: date range 2007-01-01 to 2025-04-01
dim docs: /dim/nuts.md
notes:
- This table covers only activated recipients (aktiverede fuldtidsmodtagere), not all public benefit recipients. For total public support recipients use auk01.
- omrade joins dim.nuts (same as auk01): niveau 1 = 5 regioner, niveau 2 = 11 landsdele, niveau 3 = 98 kommuner. omrade='0' = Hele landet, omrade='997' = Uoplyst — neither is in dim.nuts.
- ydelsestype codes are activation-specific: AKTOT (aktivering i alt), AKD (dagpengeberettigede), AKK (kommunal aktivering/kontanthjælpsberettigede), plus many sub-types (TVED, MED, SVD, VPD, LTD, NYD, ROD for dagpenge; TVEK, MEK, VPK, LTK, NYK, ROK, FO for kontanthjælp). AKTOT is the total.
- To avoid overcounting in ydelsestype, pick either AKTOT, or the two main branches (AKD + AKK), or individual sub-types — not a mix of levels.
- Filter kon='TOT', alder='TOT', and pick one omrade niveau for a clean aggregate.
- Quarterly data to 2025-04-01. For annual data use auh03.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN (0, 997).
