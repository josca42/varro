table: fact.uoe2
description: Udgifter til uddannelse efter uddannelsesniveau, finansieringskilde, modsektor og tid
measure: indhold (unit Mio. kr.)
columns:
- uddniv: values [TOT1=Uddannelsesniveauer i alt, H10=Grundskoler, H30=Ungdomsuddannelser, H40=Korte videregående uddannelser, H50=Mellemlange og lange videregående uddannelser]
- finanskilde: values [TOT3=Finansiering i alt, 300=Staten, 310=Kommuner og regioner, 330=Husholdninger, 340=Virksomheder, 350=Internationale kilder]
- modsektor: values [TOT2=Modsektor i alt, 200=Offentlige uddannelsesinstitutioner, 210=Private uddannelsesinstitutioner, 2=Husholdninger]
- tid: date range 2016-01-01 to 2023-01-01

notes:
- All three dimension columns contain aggregate total rows: uddniv='TOT1', finanskilde='TOT3', modsektor='TOT2'. Use TOT codes for pre-summed totals, or filter each column to a specific leaf value to avoid double-counting.
- The finanskilde × modsektor matrix is sparse — not all funding-source-to-receiving-sector combinations exist:
  - finanskilde='330' (Husholdninger) only flows to modsektor='210' (Private institutioner) and TOT2. Households only fund private institutions.
  - finanskilde='350' (Internationale kilder) only appears for H40 and H50 (not H10 grundskoler, not H30 ungdomsuddannelser), and only flows to modsektor='200' (Offentlige).
  - finanskilde='310' (Kommuner og regioner) does not flow to modsektor='2' (Husholdninger).
  - modsektor='2' (Husholdninger as receiving sector) only appears with finanskilde='300' (Staten), '340' (Virksomheder), and 'TOT3' — this captures e.g. SU payments to individuals.
- This table shows who funds education (finanskilde) and which sector receives the money (modsektor). Use uoe1 instead to see how the money is spent (lønudgifter, investeringer, SU, FoU) and at which type of institution.
- The total uddannelsesudgifter matches between uoe1 and uoe2: both show 173 799 Mio. kr. in 2023 at the TOT level, confirming these are two views of the same underlying flows.
- Sample query — financing breakdown by source in 2023: WHERE tid='2023-01-01' AND uddniv='TOT1' AND modsektor='TOT2' (gives one row per finanskilde including TOT3).