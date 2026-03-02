table: fact.idrtil01
description: Tilskuertal til udvalgte sportsgrene efter sportsgren, tilskuere og kampe og tid
measure: indhold (unit Antal)
columns:
- sports: values [SPO005=Ishockey - Landsholdet - herrer, SPO010=Ishockey - Superisligaen - herrer, SPO015=Ishockey -Superisligaen play-off og slutspil - herrer, SPO020=Ishockey - Superisligaen sæsonen totalt - herrer, SPO025=Fodbold - Landsholdet - herrer ... SPO095=Håndbold - Håndboldligaen grundspil - kvinder, SPO100=Håndbold - Håndboldligaen play-off og slutspil - kvinder, SPO105=Håndbold - Håndboldligaen sæsonen totalt- kvinder, SPO110=Håndbold - 1. Division - herrer, SPO115=Håndbold - 1. Division - kvinder]
- tilskuer: values [ENH05=Tilskuere (antal), ENH10=Kampe (antal), ENH15=Tilskuergennemsnit pr. kamp]
- tid: date range 2006/2007 to 2024/2025

notes:
- tilskuer is a measurement-type selector: ENH05=total tilskuere, ENH10=antal kampe, ENH15=tilskuergennemsnit pr. kamp. MUST filter to one value — mixing them gives nonsense sums.
- Every sports/tid combination has exactly 3 rows (one per tilskuer value). Forgetting the tilskuer filter triples all sums.
- sports encodes sport + league + gender in one code. Many leagues have both "grundspil" and "sæsonen totalt" entries (e.g., SPO010+SPO015+SPO020 for ishockey Superisligaen). Filtering to "sæsonen totalt" codes avoids double-counting grundspil and play-off.
- tid uses season format ("2006/2007"), not calendar year — the column stores this as a string, not a date.
- To get total football (herrer landshold) attendance: `WHERE sports='SPO025' AND tilskuer='ENH05'`.