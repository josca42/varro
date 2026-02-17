---
name: denmark-map
description: Create plotly choropleth maps of Danish administrative regions (kommuner, landsdele, regioner). Use when visualizing geographic data on a map, creating choropleths, or when fact data has an `omrade` column joinable to `dim.nuts`.
---

# Denmark Map Plots

Create choropleth maps using GeoParquet boundary files at `/geo/`. See `/geo/README.md` for schema, loading, and merge patterns.

## When to Use

- User asks for a map, geographic visualization, or choropleth
- Fact data has an `omrade` column (check `dim.nuts` for geographic codes)
- Comparing values across kommuner, landsdele, or regioner

## Choosing Geo Level

Query `dim.nuts.niveau` for the `omrade` values in your data:

| niveau | File | Use case |
|--------|------|----------|
| 1 | `regioner.parquet` (5 regions) | High-level regional comparison |
| 2 | `landsdele.parquet` (11 areas) | Provincial breakdown |
| 3 | `kommuner.parquet` (99 municipalities) | Detailed local comparison |

If the data has mixed levels, filter to one level before mapping.

## Data Prep

```python
import geopandas as gpd
geo = gpd.read_parquet("/geo/kommuner.parquet")
df = df[df["omrade"] != 0]  # drop whole-country aggregate
merged = geo.merge(df, left_index=True, right_on="omrade")
```

After merge, use `merged.index` for `locations` and `merged.geometry` for `geojson`.

## Chat Pattern (static PNG)

Use `px.choropleth` — produces a clean static map for PNG export:

```python
fig = px.choropleth(
    merged,
    geojson=merged.geometry,
    locations=merged.index,
    color="indhold",
    hover_name="navn",
    fitbounds="locations",
    basemap_visible=False,
)
fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
```

`fitbounds="locations"` auto-zooms to Denmark — critical for chat where the map renders as PNG. `basemap_visible=False` removes the world map background.

Return with `show=["fig"]` to render the figure in chat.

## Dashboard Pattern (interactive)

Use `px.choropleth_map` with a tile basemap:

```python
fig = px.choropleth_map(
    merged,
    geojson=merged.geometry,
    locations=merged.index,
    color="indhold",
    hover_name="navn",
    map_style="carto-positron",
    center={"lat": 56.0, "lon": 10.5},
    zoom=5.5,
)
```

Denmark center: `lat=56.0, lon=10.5`, zoom `5.5` fits the mainland and islands. Bornholm (far east) may appear small — zoom `5.0` if it matters.

## Customization

**Color scales:** `Blues`, `YlOrRd`, `Viridis` work well. For diverging data (above/below average), use `RdBu` with `color_continuous_midpoint`.

**Hover:** `fig.update_traces(hovertemplate="<b>%{hovertext}</b><br>%{z:,.0f}<extra></extra>")`

**Colorbar:** `fig.update_layout(coloraxis_colorbar=dict(title="", thickness=15, len=0.6))`

## Pitfalls

- **Forgot `omrade != 0`**: merge silently drops the aggregate row but the data count won't match — filter explicitly
- **Wrong geo level**: kommune codes merged against region boundaries produces an empty map with no error
- **Multiple time periods**: aggregate or filter to one period before mapping — multiple rows per `omrade` creates duplicate geometries
