from fasthtml.common import (
    A, Div, Footer, Html, Head, Body, Img, Meta, Nav, P, Section, Span, Title, Video,
)

from ui.components import GameOfLifeAnimation
from ui.core import ui_hdrs_base, DEFAULT_THEME

_STAMPS = [
    {"topic": "Bolig",        "slug": "bolig",        "rotate": "-2deg", "y": "8px"},
    {"topic": "Forsvar",      "slug": "forsvar",       "rotate": "1.5deg", "y": "-4px"},
    {"topic": "Indvandring",  "slug": "indvandring",  "rotate": "-1deg", "y": "6px"},
    {"topic": "Pension",      "slug": "pension",      "rotate": "-1.5deg", "y": "4px"},
    {"topic": "Sundhed",      "slug": "sundhed",      "rotate": "1deg",  "y": "-8px"},
    {"topic": "Ulighed",      "slug": "ulighed",      "rotate": "-2.5deg", "y": "5px"},
]


def _stamp(topic, slug, rotate, y):
    return A(
        Img(src=f"/static/images/maps_webp/{slug}.webp", alt=topic, cls="stamp-img"),
        Video(
            src=f"/static/images/maps_video/{slug}.mp4",
            muted=True, loop=True, playsinline=True,
            preload="none",
            cls="stamp-video",
            **{"x-ref": "video"},
        ),
        Span(topic, cls="stamp-label"),
        href=f"/public/3/{slug}",
        cls="stamp",
        style=f"--rotate: {rotate}; --y: {y}",
        **{
            "x-data": "{}",
            "@mouseenter": "$refs.video.play()",
            "@mouseleave": "$refs.video.pause(); $refs.video.currentTime = 0",
        },
    )


def Frontpage():
    nav = Nav(
        Div(
            Div(
                A(
                    "Log ind",
                    href="/login",
                    cls="text-base text-base-content/60 hover:text-base-content transition-colors no-underline",
                ),
                A(
                    "Kom i gang",
                    href="/signup",
                    cls="btn btn-primary rounded-lg text-base px-6",
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
            Div(
                P(
                    "Med tal skal land forstås",
                    cls="text-4xl md:text-7xl font-serif font-medium text-base-content max-w-3xl leading-tight",
                ),
                P(
                    "Alle har en holdning. Få har prøvet at forstå.",
                    cls="text-xl md:text-2xl text-base-content max-w-xl leading-relaxed mt-3",
                ),
                cls="flex flex-col items-center text-center",
            ),
            A(
                Span("Tænk selv →", **{"x-show": "!hover"}),
                Span("Det er lettere end du tror →", **{"x-show": "hover", "x-cloak": True}),
                href="/signup",
                cls="btn btn-primary px-12 h-14 rounded-lg text-base font-medium tracking-wide",
                **{
                    "x-data": "{ hover: false }",
                    "@mouseenter": "hover = true",
                    "@mouseleave": "hover = false",
                },
            ),
            cls="flex flex-col items-center text-center gap-8 px-6",
        ),
        stamps_desktop,
        stamps_mobile,
        cls="pt-16 pb-0 md:pt-24 bg-base-200",
    )

    footer = Footer(
        Div(
            Span("Varro", cls="text-sm font-medium text-base-content/40"),
            Span("© 2026", cls="text-sm text-base-content/25"),
            cls="max-w-5xl mx-auto px-6 flex items-center justify-between",
        ),
        cls="py-8 bg-base-200",
    )

    return Html(
        Head(
            Title("Varro — Danish AI State Statistician"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            *ui_hdrs_base,
        ),
        Body(
            Div(nav, hero, footer, cls="min-h-screen bg-base-200", data_slot="public-frontpage"),
            data_theme=DEFAULT_THEME,
        ),
    )
