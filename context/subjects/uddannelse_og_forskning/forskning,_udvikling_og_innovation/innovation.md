<fact tables>
<table>
id: oin01dk
description: Innovative arbejdssteder i den offentlige sektor efter sektorer og branche (DB07), innovationstype og tid
columns: oin01, inno, tid (time), indhold (unit Pct.)
tid range: 2016-01-01 to 2023-01-01
</table>
<table>
id: oin02dk
description: Innovative arbejdssteder i den offentlige sektor efter sektorer og branche (DB07), nyhedsgrad og tid
columns: oin01, nyhedsgrad, tid (time), indhold (unit Pct.)
tid range: 2016-01-01 to 2023-01-01
</table>
<table>
id: oin03dk
description: Innovative arbejdssteder i den offentlige sektor efter sektorer og branche (DB07), igangsætter og tid
columns: oin01, oin03, tid (time), indhold (unit Pct.)
tid range: 2016-01-01 to 2023-01-01
</table>
<table>
id: oin04dk
description: Innovative arbejdssteder i den offentlige sektor efter sektorer og branche (DB07), opnået værdier og tid
columns: oin01, oin02, tid (time), indhold (unit Pct.)
tid range: 2016-01-01 to 2023-01-01
</table>
<table>
id: inn21
description: Erhvervslivets innovationsudgifter efter branche og størrelsesgruppe, region, udgiftstype og tid
columns: innbranche, region, udgtyp, tid (time), indhold (unit 1.000 kr.)
tid range: 2020-01-01 to 2022-01-01
</table>
<table>
id: inn22
description: Innovative virksomheder efter branche og størrelsesgruppe, region, innovationstype og tid
columns: innbranche, region, inno, tid (time), indhold (unit Pct.)
tid range: 2020-01-01 to 2022-01-01
</table>
<table>
id: inn23
description: Produktinnovative virksomheder efter branche og størrelsesgruppe, region, produktinnovationstype og tid
columns: innbranche, region, innpro, tid (time), indhold (unit Pct.)
tid range: 2020-01-01 to 2022-01-01
</table>
<table>
id: inn24
description: Procesinnovative virksomheder efter branche og størrelsesgruppe, region, procesinnovationstype og tid
columns: innbranche, region, innproces, tid (time), indhold (unit Pct.)
tid range: 2020-01-01 to 2022-01-01
</table>
<table>
id: inn25
description: Virksomheder efter branche og størrelsesgruppe, region, samarbejdsemne og tid
columns: innbranche, region, innsam, tid (time), indhold (unit Pct.)
tid range: 2020-01-01 to 2022-01-01
</table>
</fact tables>

notes:
- Two distinct populations: oin01dk-oin04dk cover the **public sector** (offentlige arbejdssteder), while inn21-inn25 cover **private sector firms** (erhvervslivet). Never mix results across these groups.
- Public sector tables (oin01dk-oin04dk) span 2016-2023 and break down by sector/branch (oin01). Private sector tables (inn21-inn25) cover only 2020-2022 and break down by industry/size group (innbranche) and region.
- For **which type of innovation** public workplaces adopt: oin01dk. For **novelty degree** (first-mover vs. copy): oin02dk. For **who initiates** innovation: oin03dk. For **outcomes achieved**: oin04dk.
- For **share of innovative private firms** by type: inn22 (headline rates, includes product/process breakdown). For detail on product innovation subtypes: inn23. For process innovation subtypes: inn24. For collaboration topics: inn25. For innovation expenditure amounts: inn21 (the only table with absolute values in 1.000 kr., not percentages).
- All oin tables and inn22-inn25 report percentages — these are independent rates, never sum them. inn21 is the exception: it reports expenditure amounts in 1.000 kr. and its 6 udgtyp categories are additive components of total innovation expenditure.
- The innbranche column (inn21-inn25) encodes two parallel hierarchies in one column: branch breakdown (1000=total, 1010-1050) and size-group breakdown (1055=total, 1060-1075). Always filter to one hierarchy at a time.
- The oin01 column (oin01dk-oin04dk) similarly encodes two hierarchies: sector view (1000=total, 1010-1030) and DB07 branch view (2000=total, 4000-4240). Choose one per query.
- inn21-inn25 all have region joining dim.nuts niveau=1 (5 regions, codes 81-85). Code 0 = national total, not in dim — filter region='0' for national figures.
- Map: inn21-inn25 support choropleth maps at region level via context/geo/regioner.parquet — merge on region=dim_kode. oin01dk-oin04dk have no geographic column.