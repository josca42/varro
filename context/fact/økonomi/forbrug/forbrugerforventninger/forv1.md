table: fact.forv1
description: Forbrugerforventninger (nettotal) efter indikator og tid
measure: indhold (unit -)
columns:
- indikator: values [F1=Forbrugertillidsindikatoren, F2=Familiens økonomiske situation i dag, sammenlignet med for et år siden, F3=Familiens økonomiske  situation om et år, sammenlignet med i dag, F4=Danmarks økonomiske situation i dag, sammenlignet med for et år siden, F5=Danmarks økonomiske situation om et år, sammenlignet med i dag, F9=Anskaffelse af større forbrugsgoder, fordelagtigt for øjeblikket, F6=Priser i dag, sammenlignet med for et år siden, F7=Priser om et år, sammenlignet med i dag, F8=Arbejdsløsheden om et år, sammenlignet med i dag, F10=Anskaffelse af større forbrugsgoder, inden for de næste 12 mdr., F11=Anser det som fornuftigt at spare op i den nuværende økonomiske situation, F12=Regner med at kunne spare op i de kommende 12 måneder, F13=Familiens økonomiske situation lige nu: kan spare/penge slår til/ bruger mere end man tjener]
- tid: date range 1974-10-01 to 2025-10-01

notes:
- Monthly frequency. Each row is one indikator for one month. Always filter to a specific indikator — summing across all 13 produces a meaningless total.
- indhold is a net balance score (% positive minus % negative responses). Can be negative. F1 (Forbrugertillidsindikatoren) is the headline composite index; F2–F13 are component indicators.
- F1 ranges roughly -37 to +16; F11 (vilje til opsparing) is the most positive indicator (3 to 84).
- Not all indicators start in 1974. The earlier observations only cover a subset; coverage grows over time. Check MIN(tid) per indikator if you need a specific start date.
- Example: SELECT tid, indhold FROM fact.forv1 WHERE indikator = 'F1' ORDER BY tid — gives the monthly confidence index series.