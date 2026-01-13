"""Danish population dashboard outputs."""

from dashboard import output, Metric
import plotly.express as px


@output
def total_population(population_trend, filters):
    """Current total population metric."""
    if population_trend.empty:
        return Metric(value=0, label="Total Population", format="number")

    current = population_trend["population"].iloc[-1]
    # Calculate YoY change if we have enough data
    change = None
    if len(population_trend) >= 5:  # 4 quarters = 1 year
        prev_year = population_trend["population"].iloc[-5]
        change = (current - prev_year) / prev_year

    return Metric(
        value=current,
        label="Total Population",
        format="number",
        change=change,
        change_label="vs last year" if change else None,
    )


@output
def quarters_shown(population_trend, filters):
    """Number of quarters in selected period."""
    return Metric(
        value=len(population_trend),
        label="Quarters",
        format="number",
    )


@output
def population_trend_chart(population_trend, filters):
    """Population trend line chart."""
    if population_trend.empty:
        return px.line(title="Population Trend (No Data)")
    return px.line(
        population_trend,
        x="quarter",
        y="population",
        title="Population Over Time",
    )


@output
def region_table(population_by_region, filters):
    """Population by region table."""
    return population_by_region


@output
def age_chart(age_distribution, filters):
    """Age distribution bar chart."""
    if age_distribution.empty:
        return px.bar(title="Age Distribution (No Data)")
    return px.bar(
        age_distribution,
        x="age_group",
        y="population",
        title="Population by Age Group",
    )
