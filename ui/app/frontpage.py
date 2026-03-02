from fasthtml.common import A, Div, Footer, Img, Nav, P, Section, Span, Title

from ui.components import GameOfLifeAnimation

_STAMPS = [
    {"topic": "Befolkning",    "slug": "befolkning",    "rotate": "0deg",  "z": 10},
    {"topic": "Arbejdsmarked", "slug": "arbejdsmarked", "rotate": "3deg",  "z": 20},
    {"topic": "Bolig",         "slug": "bolig",         "rotate": "-2deg", "z": 30},
    {"topic": "Uddannelse",    "slug": "uddannelse",    "rotate": "-5deg", "z": 40},
    {"topic": "Sundhed",       "slug": "sundhed",       "rotate": "1deg",  "z": 50},
    {"topic": "Indkomst",      "slug": "indkomst",      "rotate": "5deg",  "z": 60},
]


def _stamp(topic, slug, rotate, z):
    return A(
        Img(src=f"/static/images/stamps/{slug}.png", alt=topic, cls="stamp-img"),
        Span(topic, cls="stamp-label"),
        href=f"/dashboard/{slug}",
        cls="stamp",
        style=f"--rotate: {rotate}; z-index: {z}",
    )


def Frontpage():
    nav = Nav(
        Div(
            Div(
                A(
                    "Sign in",
                    href="/login",
                    cls="text-sm text-base-content/60 hover:text-base-content transition-colors no-underline",
                ),
                A(
                    "Get Started",
                    href="/signup",
                    cls="btn btn-primary btn-sm rounded-lg",
                ),
                cls="flex items-center gap-6",
            ),
            cls="max-w-5xl mx-auto w-full px-6 flex items-center justify-end",
        ),
        cls="py-4",
    )

    hero = Section(
        Div(
            GameOfLifeAnimation(
                width=660, height=180, cell_size=3,
                text="VARRO", color="#9b2743", autoplay=100,
            ),
            P(
                "The Danish AI State Statistician",
                cls="text-xl md:text-2xl text-base-content/50 max-w-xl leading-relaxed",
            ),
            A(
                "Get Started for Free →",
                href="/signup",
                cls="btn btn-primary px-8 h-11 rounded-lg text-sm font-medium tracking-wide",
            ),
            Div(
                *[_stamp(**s) for s in _STAMPS],
                cls="stamps-row",
            ),
            cls="flex flex-col items-center text-center gap-6",
        ),
        cls="pt-24 pb-20 md:pt-36 md:pb-28 px-6 bg-base-200",
    )

    footer = Footer(
        Div(
            Span("Varro", cls="text-sm font-medium text-base-content/40"),
            Span("© 2026", cls="text-sm text-base-content/25"),
            cls="max-w-5xl mx-auto px-6 flex items-center justify-between",
        ),
        cls="py-8 bg-base-200",
    )

    return Title("Varro — Danish AI State Statistician"), Div(
        nav,
        hero,
        footer,
        cls="min-h-screen bg-base-200",
        data_slot="public-frontpage",
    )
