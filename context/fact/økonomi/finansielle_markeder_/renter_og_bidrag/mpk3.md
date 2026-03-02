table: fact.mpk3
description: Rentesatser, ultimo (pct p.a.) efter type og tid
measure: indhold (unit Pct. pro anno)
columns:
- type: values [5500601001=Nationalbankens diskonto, 5500602001=Nationalbankens udlåns- og indskudsbevisrente (-2009M05), 5500602011=Nationalbankens udlånsrente (2009M06- ), 5500602021=Nationalbankens indskudsbevisrente (2009M06- ), 5500603001=Pengemarkedsrentesats 3 måneder, DKK (-2012M09), 5500604001=Pengemarkedsrentesats 3 måneder, Euro (-2011M08), 5500701001=Obligationsrentegennemsnit: Enhedspriotitetsobligationer, 5500701002=Obligationsrentegennemsnit: Samtlige serier, 5500701003=Obligationsrentegennemsnit: Statsobligationer mv., 5500701004=10 årig statsobligation, 5500702001=Effektiv pantebrevsrente (-2009M09), 6050=Obligationsrentegennemsnit: Almindelige og særlige realkreditobligationer (-2014M08), 6059=CIBOR, løbetid 3 måneder]
- tid: date range 1985-01-01 to 2025-09-01
notes:
- type encodes the specific interest rate series as a numeric code (e.g. 5500601001=Nationalbankens diskonto). These are independent series — never sum across type values.
- Several series have an end date embedded in the label (e.g. "(-2012M09)" or "(-2009M05)"). Querying for recent periods on discontinued series returns no rows.
- Monthly data from 1985; for a simple overview of current benchmark rates, filter to type IN ('5500602011', '5500602021') for the two Nationalbank rates active since 2009M06.
