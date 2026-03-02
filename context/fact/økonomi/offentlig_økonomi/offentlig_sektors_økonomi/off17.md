table: fact.off17
description: Offentlig forvaltning og service, subsidier (til virksomheder) efter tilskudsart og tid
measure: indhold (unit Mio. kr.)
columns:
- tilskudsart: values [I=I. Dansk finansierede subsidier i alt (II.2+III.), II=II. EU-ordninger i alt (1.1.+2.1.), II.1=II.1. EUs andel af EU-ordninger i alt, II.2=II.2.Dansk andel af EU-ordninger i alt, III=III. Danske ordninger i alt (1.2.+2.2.) ... 2.2.22=2.2.22. Udvikling af kompetence og teknologi, 2.2.23=2.2.23. Højteknologifonden, 2.2.24=2.2.24. Løntilskud ved ansættelse af forsikrede ledige, 2.2.25=2.2.25. Andre PSO-omkostninger, 2.2.26=2.2.26. Andre produktionssubsidier i.a.n.]
- tid: date range 1971-01-01 to 2024-01-01

notes:
- tilskudsart: hierarchical. Top-level aggregates: I=Dansk-finansierede subsidier i alt (=II.2+III), II=EU-ordninger i alt (=II.1+II.2), III=Danske ordninger i alt. Then numbered sub-codes 1.1, 1.2, 2.1, 2.2, 2.2.1...2.2.26 are the detailed components. Don't sum I+II+III or mix aggregates with their components.
- Note: I covers only the Danish-financed share; if you want all subsidies including EU's own contribution, you need I + II.1 (EU's share of EU programs).