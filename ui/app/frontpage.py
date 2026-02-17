from fasthtml.common import A, Div, Footer, Nav, P, Section, Span, Title

from ui.components import GameOfLifeAnimation


def Frontpage():
    nav = Nav(
        Div(
            A(
                "varro",
                href="/",
                cls="text-lg font-semibold tracking-tight text-base-content no-underline hover:no-underline",
            ),
            Div(
                A(
                    "Sign in",
                    href="/login",
                    cls="text-sm text-base-content/60 hover:text-base-content transition-colors no-underline",
                ),
                A(
                    "Get Started",
                    href="/signup",
                    cls="btn btn-primary btn-sm",
                ),
                cls="flex items-center gap-6",
            ),
            cls="max-w-5xl mx-auto w-full px-6 flex items-center justify-between",
        ),
        cls="py-5",
    )

    hero = Section(
        Div(
            GameOfLifeAnimation(
                width=660, height=180, cell_size=3,
                text="VARRO", color="#9b2743", autoplay=100,
            ),
            P(
                "The Danish AI State Statistician",
                cls="text-lg text-base-content/55 max-w-xl leading-relaxed",
            ),
            A(
                "Get Started for Free \u2192",
                href="/signup",
                cls="btn btn-primary px-8 h-11 rounded-lg text-sm font-medium tracking-wide",
            ),
            P(
                "Free to explore. No credit card required.",
                cls="text-sm text-base-content/35",
            ),
            cls="flex flex-col items-center text-center gap-6",
        ),
        cls="pt-24 pb-20 md:pt-36 md:pb-28 px-6 bg-base-200",
    )

    features = Section(
        Div(
            _feature(
                "Conversational analysis",
                "Ask questions in plain language. Get tool-backed statistical analysis with transparent methodology and reproducible results.",
            ),
            _feature(
                "Interactive dashboards",
                "Browse curated dashboards built from real Danmarks Statistik data with filters, charts, and live visualizations.",
            ),
            _feature(
                "Open & verifiable",
                "Every analysis traces back to official public statistics. Fully reproducible, fully transparent.",
            ),
            cls="max-w-4xl mx-auto grid md:grid-cols-3 gap-12 md:gap-16",
        ),
        cls="py-20 md:py-28 px-6 bg-base-100",
    )

    footer = Footer(
        Div(
            Span("varro", cls="text-sm font-medium text-base-content/40"),
            Span("\u00a9 2026", cls="text-sm text-base-content/25"),
            cls="max-w-5xl mx-auto px-6 flex items-center justify-between",
        ),
        cls="py-8 bg-base-200",
    )

    return Title("Varro \u2014 Danish AI State Statistician"), Div(
        nav,
        hero,
        features,
        footer,
        cls="min-h-screen bg-base-200",
        data_slot="public-frontpage",
    )


def _feature(title, description):
    return Div(
        Div(cls="w-8 h-0.5 bg-primary/30 mb-5"),
        Div(title, cls="text-sm font-semibold text-base-content mb-3"),
        P(description, cls="text-sm text-base-content/55 leading-relaxed"),
    )
