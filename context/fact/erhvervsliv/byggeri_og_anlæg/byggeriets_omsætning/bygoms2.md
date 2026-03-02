table: fact.bygoms2
description: Omsætning i byggeri og anlæg efter branche (DB07), arbejdets art og tid
measure: indhold (unit Mio. kr.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- arbart: values [0=Omsætning i alt, 1=Nybyggeri og tilbygning i alt, 10=Nybyggeri og tilbygning, boliger, 11=Nybyggeri og tilbygning, andre, 2=Reparation og vedligeholdelse i alt, 20=Reparation og vedligeholdelse, hovedreparation, boliger, 22=Reparation og vedligeholdelse, hovedreparation, andre, 24=Reparation og vedligeholdelse, vedligeholdelse, boliger, 26=Reparation og vedligeholdelse, vedligeholdelse, andre, 3=Anlægsvirksomhed i alt, 30=Anlægsvirksomhed, nye anlæg, 32=Anlægsvirksomhed, hovedreparation, 34=Anlægsvirksomhed, vedligeholdelse, 4=Anden virksomhed i alt]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/db.md

notes:
- branche07 does NOT join dim.db in practice — only 2 of 9 codes match (432200, 439910 happen to share the 6-digit format). The codes are survey-specific aggregations. Use ColumnValues("bygoms2", "branche07") instead to get all 9 labels: F=Bygge og anlæg (total), 41000=Byggeentreprenører, 42000=Anlægsentreprenører, 43003=Anden specialiseret bygge- og anlægsvirksomhed mv., 43201=El-installation mv., 432200=VVS, 43301=Tømrer- og bygningsvirksomhed mv., 43302=Maler- og glarmestervirksomhed mv., 439910=Murere.
- branche07 has an aggregate: F = sum of all 8 other codes (41000+42000+43003+43201+432200+43301+43302+439910). Sections 41 and 42 each appear as a single block; section 43 is split into 6 specialised sub-trades. Never sum across all 9 codes — that would double-count F.
- arbart has a two-level hierarchy. Single-digit codes are aggregates (0=total, 1=nybyggeri i alt, 2=reparation i alt, 3=anlæg i alt, 4=anden virksomhed i alt). Double-digit codes are sub-categories (10, 11 under 1; 20, 22, 24, 26 under 2; 30, 32, 34 under 3). Filter to either all single-digit OR all double-digit codes to avoid double-counting. Use ColumnValues("bygoms2", "arbart") to see all labels.
- For a simple total omsætning: WHERE branche07='F' AND arbart='0' — one row per tid.
- For omsætning by branche (leaf codes only, no double-count): WHERE branche07 != 'F' AND arbart='0'. This gives 8 rows per tid.
- For omsætning by arbejdets art (top-level only): WHERE branche07='F' AND arbart IN ('1','2','3','4'). This gives 4 rows per tid summing to arbart='0'.