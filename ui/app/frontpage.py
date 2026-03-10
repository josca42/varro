from fasthtml.common import A, Div, Footer, Img, Nav, P, Section, Span, Title

from ui.components import GameOfLifeAnimation

_STAMPS = [
    {"topic": "Bolig",        "slug": "bolig",        "rotate": "-2deg", "y": "8px"},
    {"topic": "Forsvar",      "slug": "forsvar",       "rotate": "1.5deg", "y": "-4px"},
    {"topic": "Indvandring",  "slug": "indvandring",  "rotate": "-1deg", "y": "6px"},
    {"topic": "Økonomi",      "slug": "økonomi",      "rotate": "2.5deg", "y": "-6px"},
    {"topic": "Pension",      "slug": "pension",      "rotate": "-1.5deg", "y": "4px"},
    {"topic": "Sundhed",      "slug": "sundhed",      "rotate": "1deg",  "y": "-8px"},
    {"topic": "Ulighed",      "slug": "ulighed",      "rotate": "-2.5deg", "y": "5px"},
]


def _stamp(topic, slug, rotate, y):
    return A(
        Img(src=f"/static/images/maps/{slug}.png", alt=topic, cls="stamp-img"),
        Span(topic, cls="stamp-label"),
        href=f"/dashboard/{slug}",
        cls="stamp",
        style=f"--rotate: {rotate}; --y: {y}",
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

    stamps = [_stamp(**s) for s in _STAMPS]

    stamps_desktop = Div(*stamps, cls="stamps-row stamps-desktop")

    stamps_mobile = Div(
        Div(
            *[_stamp(**s) for s in _STAMPS],
            *[_stamp(**s) for s in _STAMPS],
            cls="stamps-marquee-track",
        ),
        cls="stamps-row stamps-mobile",
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
            cls="flex flex-col items-center text-center gap-6 px-6",
        ),
        stamps_desktop,
        stamps_mobile,
        cls="pt-24 pb-0 md:pt-36 bg-base-200",
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
