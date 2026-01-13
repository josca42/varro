"""Sales dashboard outputs."""

from dashboard import output, Metric
import plotly.express as px


@output
def total_revenue(monthly_revenue, filters):
    """Total revenue metric."""
    total = monthly_revenue["revenue"].sum() if not monthly_revenue.empty else 0
    return Metric(
        value=total,
        label="Total Revenue",
        format="currency",
        change=0.12,
        change_label="vs last period",
    )


@output
def total_orders(monthly_revenue, filters):
    """Total orders metric (placeholder using row count)."""
    count = len(monthly_revenue)
    return Metric(
        value=count,
        label="Total Months",
        format="number",
    )


@output
def revenue_trend(monthly_revenue, filters):
    """Monthly revenue line chart."""
    if monthly_revenue.empty:
        return px.line(title="Revenue Trend (No Data)")
    return px.line(
        monthly_revenue,
        x="month",
        y="revenue",
        title="Monthly Revenue",
    )


@output
def top_products_table(top_products, filters):
    """Top products table."""
    return top_products
