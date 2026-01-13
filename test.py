from ui import daisy_app
from fasthtml.common import Script
from varro.db.db import engine
from varro.dashboard import mount_dashboards

# Plotly JS for chart rendering
plotly_hdr = Script(src="https://cdn.plot.ly/plotly-2.35.2.min.js")

# Alpine.js for tab interactivity
alpine_hdrs = (
    Script(src="https://unpkg.com/@alpinejs/ui@3.15.3/dist/cdn.min.js", defer=True),
    Script(
        src="https://unpkg.com/@alpinejs/collapse@3.15.3/dist/cdn.min.js", defer=True
    ),
    Script(src="https://unpkg.com/@alpinejs/focus@3.15.3/dist/cdn.min.js", defer=True),
    Script(src="https://unpkg.com/alpinejs@3.15.3/dist/cdn.min.js", defer=True),
)
# Create FastHTML app with DaisyUI + Plotly + Alpine.js
app, rt = daisy_app(hdrs=(plotly_hdr, *alpine_hdrs))

# Mount dashboards from the example folder
dashboards = mount_dashboards(app, engine, "example_dashboard_folder")

# Run the server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5001)
