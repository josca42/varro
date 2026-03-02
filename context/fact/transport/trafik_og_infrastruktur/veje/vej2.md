table: fact.vej2
description: Investeringer i vejnettet efter investeringstype, enhed og tid
measure: indhold (unit Mio. kr.)
columns:
- invest: values [0=VEJNETTET I ALT, 75=Anlægsudgifter, 80=Drift og vedligeholdelse, 85=Storebæltsforbindelsen, 92=Øresundsforbindelsen]
- enhed: values [2004=Årets priser, 1995=1995-priser, 2000=2000-priser]
- tid: date range 1990-01-01 to 2022-01-01

notes:
- enhed is a CRITICAL measurement selector — every invest+tid combination appears 3 times (once per price base). Failing to filter enhed triples all counts. Always filter to exactly one: enhed='2004' for current prices (årets priser), or enhed='1995'/'2000' for fixed-price time series comparisons.
- invest is hierarchical: 0=VEJNETTET I ALT is the total of 75 (anlæg) + 80 (drift/vedligehold) + 85 (Storebælt) + 92 (Øresund). Don't sum invest without filtering out 0.
- Note that not all enhed values cover the full time range — 1995-priser and 2000-priser have fewer years. For the full 1990–2022 span, use enhed='2004'.
- For a simple total investment time series: WHERE invest='0' AND enhed='2004'.