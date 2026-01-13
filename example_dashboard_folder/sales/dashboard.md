# Danish Population Dashboard

::: filters
{% select name="region" label="Region" options="query:regions" default="all" /%}
{% daterange name="period" label="Period" default="all" /%}
:::

::: grid cols=2
{% metric name="total_population" /%}
{% metric name="quarters_shown" /%}
:::

::: tabs
::: tab name="Trend"
{% figure name="population_trend_chart" /%}
:::
::: tab name="Regions"
{% table name="region_table" /%}
:::
::: tab name="Age Groups"
{% figure name="age_chart" /%}
:::
:::
