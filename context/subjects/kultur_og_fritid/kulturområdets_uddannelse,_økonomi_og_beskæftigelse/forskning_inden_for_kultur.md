<fact tables>
<table>
id: foukul02
description: Årsværk og Personale i den offentlige sektor til Forskning og Udvikling i Kulturen efter fagområde, årsværk og personale, køn og tid
columns: fagomr, aarvaerk, koen, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2023-01-01
</table>
<table>
id: foukul01
description: Udgifter i den offentlige sektor til Forskning og Udvikling i kulturen efter fagområde, udgifter og tid
columns: fagomr, udgift, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- For R&D expenditure (in 1.000 kr.) broken down by field: use foukul01. It has an udgift column — filter to udgift=10 for the total (udgift=20 driftsudgifter + udgift=30 anlægsudgifter sum to udgift=10).
- For R&D personnel by field and gender: use foukul02. It has aarvaerk (40=FTE, 50=headcount) and koen (0=total, 1=mænd, 2=kvinder). Always filter to one aarvaerk value — they are independent measures, not categories.
- Both tables cover 2007–2023 annually and share the same fagomr coding (1000=Kultur i alt aggregate, 1010–1120 individual fields). fagomr=1000 is a grand total row — exclude it when breaking down by field.
- Neither table has regional breakdown or dim table joins — all columns are inline coded values.