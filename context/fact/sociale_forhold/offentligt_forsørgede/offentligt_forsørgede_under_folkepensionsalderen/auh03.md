table: fact.auh03
description: Offentligt forsørgede (aktiverede fuldtidsmodtagere) efter område, ydelsestype, køn, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- ydelsestype: values [AKTOT=Aktivering i alt, AKD=Aktiverede dagpengeberettigede, TVED=Vejledning- og opkvalificering i alt (dagpengeberettigede), MED=Mentorstøtte (dagpengeberettigede), SVD=6 ugers selvvalgt uddannelse (dagpengeberettigede), VPD=Virksomhedspraktik (dagpengeberettigede), LTD=Ansættelse med løntilskud (dagpengeberettigede), NYD=Nytteindsats (dagpengeberettigede), ROD=Jobrotation (dagpengeberettigede), AKK=Kommunal aktivering i alt, TVEK=Vejledning- og opkvalificering ialt (Kontanthjælpsberettigede) , MEK=Mentorstøtte (kontanthjælpsberettigede), VPK=Virksomhedspraktik (kontanthjælpsberettigede), LTK=Ansættelse med løntilskud (kontanthjælpsberettigede), NYK=Nytteindsats (kontanthjælpsberettighede), ROK=Jobrotation (kontanthjælpsberettigede, FO=Forsøg (kontanthjælpsmodtagere)]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- Annual version of auk03 (activated recipients only). Latest to 2024-01-01.
- omrade joins dim.nuts: niveau 1-3. omrade='0' = Hele landet, omrade='997' = Uoplyst — not in dim.nuts. Filter by niveau for a single geographic level.
- ydelsestype codes are activation-specific (AKTOT = total). Don't mix hierarchy levels (AKTOT covers AKD+AKK; each of those covers sub-types).
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN (0, 997).
