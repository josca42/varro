<fact tables>
<table>
id: amr1
description: Befolkningens tilknytning til arbejdsmarkedet (fuldtidspersoner) efter område, socioøkonomisk status, køn, alder og tid
columns: omrade, socio, koen, alder1, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: amr2
description: Befolkningens tilknytning til arbejdsmarkedet (fuldtidspersoner) efter socioøkonomisk status, køn, alder, herkomst og tid
columns: socio, kon, alder, herkomst, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- Use amr1 for regional breakdown (99 kommuner + national aggregate omrade='0'), broken down by socio/koen/alder1. Use amr2 for herkomst (ethnic origin) breakdown — national level only.
- Both tables cover annual data 2008–2023, use the same 26 socio codes, and share the same age bands and gender values (M/K only, no totals).
- Neither table has pre-aggregated total rows for any dimension. Always sum the categories you don't filter on.
- The 26 socio codes are mutually exclusive and exhaustive — they partition the full population. Summing all codes gives total population (~5.94M in 2023). Common filters: socio='21' for ordinarily employed (~2.4M), socio='50' for unemployed, socio='150' for folkepension recipients.
- amr1 gotcha: omrade='0' (Hele landet) is not in dim.nuts and is dropped on a direct join. Filter omrade='0' without joining dim.nuts for national queries.
- Map: amr1 supports choropleth at kommune level — context/geo/kommuner.parquet, merge on omrade=dim_kode, exclude omrade='0'.