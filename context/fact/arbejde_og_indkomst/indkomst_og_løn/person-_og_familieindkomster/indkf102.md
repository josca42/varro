table: fact.indkf102
description: Familiernes indkomst før skat efter område, enhed, ejer/lejer af bolig, familietype, indkomstinterval og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- enhed: values [102=Familier i gruppen (Antal), 110=Indkomstbeløb (1.000 kr.), 117=Gennemsnit for familier i gruppen (kr.)]
- boligartud: values [TOT=I alt, EJ=Beboet af ejer, LEJ=Beboet af lejer]
- famtype: values [FAIA=Familier i alt, FAUB=Familier uden børn, FAMB=Familier med børn, PAIA=Par i alt, PAUB=Par uden børn, PAMB=Par med børn, ENIA=Enlige i alt, ENUB=Enlige uden børn, ENMB=Enlige med børn]
- indkintb: values [99=I alt, 800=Under 200.000 kr., 810=200.000 - 299.999 kr., 815=300.000 - 399.999 kr., 820=400.000 - 499.999 kr., 600=500.000 - 599.999 kr., 825=600.000 kr. og derover]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at levels 1 (5 regioner) and 2 (landsdele). No kommune detail here.
- omrade='0' is national aggregate, not in dim.nuts.
- indkintb total code is '99' (not '0' like person tables). Very coarse brackets (only 6 non-total values, starting from "under 200.000 kr.").
- boligartud: TOT/EJ/LEJ. Filter to TOT for overall.
- famtype column (note: this table uses 'famtype' not 'famtyp' — different column name from indkf111/indkf112).
- enhed selector (3 types). Always filter to one.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
