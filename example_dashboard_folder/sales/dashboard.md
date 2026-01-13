# Sales Dashboard

::: filters
{% select name="region" label="Region" options="query:regions" default="all" /%}
{% daterange name="period" label="Period" default="all" /%}
:::

::: grid cols=2
{% metric name="total_revenue" /%}
{% metric name="total_orders" /%}
:::

::: tabs
::: tab name="Trend"
{% figure name="revenue_trend" /%}
:::
::: tab name="Products"
{% table name="top_products_table" /%}
:::
:::


