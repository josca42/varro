# Danish Population Dashboard

::: filters
<filter-select name="region" label="Region" options="query:regions" default="all" />
<filter-date name="period" label="Period" default="all" />
:::

::: grid cols=2
<metric name="total_population" />
<metric name="quarters_shown" />
:::

::: tabs
::: tab name="Trend"
<fig name="population_trend_chart" />
:::
::: tab name="Regions"
<df name="region_table" />
:::
::: tab name="Age Groups"
<fig name="age_chart" />
:::
:::
