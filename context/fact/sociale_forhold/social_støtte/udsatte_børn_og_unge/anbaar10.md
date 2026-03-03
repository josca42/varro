table: fact.anbaar10
description: Udslagsgivende årsager til iværksatte anbringelser efter landsdel, årsag til anbringelse, alder, køn og tid
measure: indhold (unit Antal)
columns:
- landdel: join dim.nuts on landdel=kode [approx]; levels [2]
- anbringaarsag: values [UDSLAG1=Misbrug hos barn/ung, UDSLAG2=Kriminalitet hos barn/ung, UDSLAG3=Skole- og uddannelsesproblemer hos barn/ung f.eks. fravær, UDSLAG4=Anden bekymrende adfærd hos barn/ung f.eks. udadreagerende adfærd, UDSLAG5=Betydelig eller varigt nedsat fysisk eller psykisk funktionsevne hos barn/ung, UDSLAG6=Sundhedsforhold hos barn/ung, UDSLAG7=Overgreb mod barn/ung begået af andre end barnets/den unges forældre (seksuelt, fysisk vold eller psykisk vold), UDSLAG8=Anden form for omsorgssvigt over for barn/ung, UDSLAG9=Misbrug hos forældre, UDSLAG10=Kriminalitet hos forældre, UDSLAG11=Anden bekymrende adfærd hos forældre, UDSLAG12=Betydelig eller varigt nedsat fysisk eller psykisk funktionsevne hos forældre, UDSLAG13=Højt konfliktniveau eller vold i hjemmet mellem voksne, UDSLAG14=Utilstrækkelig omsorg fra forældre, UDSLAG15=Fogedsag, hjemløshed eller udsættelse fra bolig, UDSLAG17=Sundhedsforhold hos en eller begge forældre, UDSLAG18=Overgreb mod barn/ung, begået af forældrene (seksuelt, fysisk vold eller psykisk vold), UDSLAG16=Andet, 999=Uoplyst]
- alder1: values [IALT=Alder i alt, 0005=0-5 år, 0611=6-11 år, 1217=12-17 år, 999=Uoplyst alder]
- kon: values [0=I alt, D=Drenge, P=Piger, 9=Uoplyst køn]
- tid: date range 2018-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- CRITICAL: anbringaarsag causes are NOT mutually exclusive. A single placement can have multiple triggering causes registered. In 2023: 3530 new placements nationally but the sum of all causes = 5314. NEVER sum across all anbringaarsag codes — it overcounts placements.
- There is no total/IALT code in anbringaarsag. Each UDSLAG code is an independent count of placements where that cause was a factor. Use each cause separately to answer "how many placements involved X".
- landdel joins dim.nuts at niveau 2 (11 landsdele). Code 0 = national total.
- alder1 here goes only to 12-17 (no 18+ group, unlike other anbaar tables). Missing 18-22 year olds.
- Only goes back to 2018 — shorter series than other anbringelse tables.
- Map: /geo/landsdele.parquet — merge on landdel=dim_kode. Exclude landdel=0.