# Snapshot Tool Plan

## Goal

Implement a first-class `Snapshot` agent tool that snapshots a dashboard URL into files the agent can inspect.

## Decisions

- Folder naming uses URL query parameters directly.
- No hash suffix in folder names.
- Use `_` as folder name when there are no query parameters.
- Tool API: `Snapshot(url?: str)`.
- If `url` is omitted, snapshot the user's current browser URL (`ctx.deps.current_url`).
- Tool returns the exact URL that was snapshotted.
- Jupyter `show` image outputs should use the same resize pipeline with a stricter cap than snapshot files.

## Artifact Mapping

- Snapshot folder target:
  - `/dashboards/{slug}/snapshots/{query_folder}/`
- Always write:
  - `dashboard.png` (screenshot of the rendered dashboard URL)
  - `context.url` (the exact URL used for snapshot)
  - `{YYYY-MM-DD}.timestamp` (empty marker for freshness)
- Write output artifacts by `outputs.py` return type:
  - `plotly.graph_objects.Figure` -> `figures/{output_name}.png`
  - `pandas.DataFrame` -> `tables/{output_name}.parquet`
  - `Metric` (and other scalar/text outputs) -> `metrics.json` (keyed by `output_name`)
- Naming:
  - `output_name` is the `@output` function name.
  - file names should be deterministic and stable across runs.
- Figure rendering details:
  - render Plotly figures to PNG bytes via the existing Plotly-to-PNG path.
  - use a selector wait so Playwright captures only after plot render is ready.
- Image size policy:
  - capture screenshots with Playwright `scale="css"` to avoid Retina/device-pixel-ratio bloat.
  - enforce a max pixel budget in Python (default `max_pixels = 1_500_000`) for all PNG artifacts.
  - if `width * height > max_pixels`, downscale proportionally with Pillow (`LANCZOS`) before saving.
  - save PNGs with optimization enabled (`optimize=True`) to keep file sizes reasonable.
  - apply this to `dashboard.png` and all `figures/*.png`.
- Jupyter image size policy:
  - apply resizing to Plotly PNGs returned by the Jupyter tool (`show` path).
  - use a more aggressive cap than snapshot files (default `max_pixels = 1_000_000`).
  - keep proportional downscaling with Pillow (`LANCZOS`) and optimized PNG output.
- Table rendering details:
  - write DataFrames with `to_parquet(..., index=False)`.
  - parquet files are inspected through the `Read` tool parquet support (`df_preview` output).

## Implementation Steps

1. Verify clean baseline after revert and confirm snapshot-related code paths to keep/remove.
2. Implement snapshot service module at `varro/agent/snapshot.py` to generate:
   - `dashboard.png`
   - `figures/*.png`
   - `tables/*.parquet`
   - `metrics.json`
   under `/dashboards/{slug}/snapshots/{query_folder}/`.
3. Implement query-folder naming:
   - `_` when query string is empty.
   - canonical sorted query string folder name when query exists.
4. Add `Snapshot` tool to `varro/agent/assistant.py`:
   - optional `url` parameter
   - fallback to `ctx.deps.current_url` when omitted
   - return snapshotted URL string
5. Update prompts/docs to describe the `Snapshot` tool and remove CLI snapshot script as primary path.
6. Add/adjust tests for:
   - folder naming (`_` vs canonical query)
   - `Snapshot` tool URL fallback behavior
   - snapshot artifacts generation (`dashboard.png`, figures, tables, `metrics.json`) (mock screenshot capture as needed)
   - image-size enforcement (no resize below threshold; proportional resize above threshold)
   - Jupyter Plotly `show` image-size enforcement with the stricter threshold
7. Run compile/tests and report results, including any environment constraints (e.g. DB availability).
