table: fact.flyv33
description: Passagertransport med rute- og charterfly mellem danske lufthavne efter påstigning, afstigning og tid
measure: indhold (unit 1.000 personer)
columns:
- pastig1: values [F10010=FRA LUFTHAVNE I ALT, F10015=Fra København, F10020=Fra Billund, F10025=Fra Aarhus, F10030=Fra Aalborg, F10035=Fra Karup, F10040=Fra Esbjerg, F10045=Fra Bornholm, F10050=Fra Sønderborg, F10055=Fra Roskilde, F10060=Fra Thisted, F10070=Fra øvrige lufthavne]
- afstig1: values [T10010=TIL LUFTHAVNE I ALT, T10015=Til København, T10020=Til Billund, T10025=Til Aarhus, T10030=Til Aalborg, T10035=Til Karup, T10040=Til Esbjerg, T10045=Til Bornholm, T10050=Til Sønderborg, T10055=Til Roskilde, T10060=Til Thisted, T10070=Til øvrige lufthavne]
- tid: date range 2004-01-01 to 2024-01-01

notes:
- Origin-destination matrix for domestic flights between Danish airports only. F10010 and T10010 are totals — both are included as rows in the data.
- To get total departures from one airport: filter pastig1=F1001X, afstig1=T10010 (uses the pre-computed destination total). To get flows between two specific airports: filter both pastig1 and afstig1 to the specific codes.
- Do NOT sum all rows without excluding the total codes (F10010 / T10010) — that would double-count. When summing individual route cells (excluding total rows), you get the complete flow matrix.
- Annual data.
