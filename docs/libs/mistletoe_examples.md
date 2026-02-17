<fasthtml example of modified mistletoe render>
import fasthtml.common as fh
from fasthtml.common import Div, P, Span, FT
from enum import Enum, auto
from functools import partial
from itertools import zip_longest
from typing import Union, Tuple, Optional, Sequence
from fastcore.all import *
import copy, re, httpx, os
import pathlib
from mistletoe.html_renderer import HTMLRenderer
from mistletoe.span_token import Image
import mistletoe
from lxml import html, etree

franken_class_map = {
    'h1': 'uk-h1 text-4xl font-bold mt-12 mb-6',
    'h2': 'uk-h2 text-3xl font-bold mt-10 mb-5', 
    'h3': 'uk-h3 text-2xl font-semibold mt-8 mb-4',
    'h4': 'uk-h4 text-xl font-semibold mt-6 mb-3',
    
    # Body text and links
    'p': 'text-lg leading-relaxed mb-6',
    'a': 'uk-link text-primary hover:text-primary-focus underline',
    
    # Lists with proper spacing
    'ul': 'uk-list uk-list-bullet space-y-2 mb-6 ml-6 text-lg',
    'ol': 'uk-list uk-list-decimal space-y-2 mb-6 ml-6 text-lg',
    'li': 'leading-relaxed',
    
    # Code and quotes
    'pre': 'bg-base-200 rounded-lg p-4 mb-6',
    'code': 'uk-codespan px-1',
    'pre code': 'uk-codespan px-1 block overflow-x-auto',
    'blockquote': 'uk-blockquote pl-4 border-l-4 border-primary italic mb-6',
    
    # Tables
    'table': 'uk-table uk-table-divider uk-table-hover uk-table-small w-full mb-6',
    'th': '!text-left p-2 font-semibold',
    'td': 'p-2',
    
    # Other elements
    'hr': 'uk-divider-icon my-8',
    'img': 'max-w-full h-auto rounded-lg mb-6'
}

# %% ../nbs/02_franken.ipynb
def apply_classes(html_str:str, # Html string
                  class_map=None, # Class map
                  class_map_mods=None # Class map that will modify the class map map (for small changes to base map)
                 )->str: # Html string with classes applied
    "Apply classes to html string"
    if not html_str: return html_str
    # Handles "Unicode strings with encoding declaration are not supported":
    if html_str[:100].lstrip().startswith('<?xml'): html_str = html_str.split('?>', 1)[1].strip()
    class_map = ifnone(class_map, franken_class_map)
    if class_map_mods: class_map = {**class_map, **class_map_mods}
    try:
        html_str = html.fragment_fromstring(html_str, create_parent=True)
        for selector, classes in class_map.items():
            # Handle descendant selectors (e.g., 'pre code')
            xpath = '//' + '/descendant::'.join(selector.split())
            for element in html_str.xpath(xpath):
                existing_class = element.get('class', '')
                new_class = f"{existing_class} {classes}".strip()
                element.set('class', new_class)
        return ''.join(etree.tostring(c, encoding='unicode', method='html') for c in html_str)
    except (etree.ParserError,ValueError): return html_str

# %% ../nbs/02_franken.ipynb
class FrankenRenderer(HTMLRenderer):
    "Custom renderer for Franken UI that handles image paths"
    def __init__(self, *args, img_dir=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.img_dir = img_dir

    
    
    def render_image(self, token):
        "Modify image paths if they're relative and self.img_dir is specified"
        template = '<img src="{}" alt="{}"{} class="max-w-full h-auto rounded-lg mb-6">'
        title = f' title="{token.title}"' if hasattr(token, 'title') else ''
        src = token.src
        if self.img_dir and not src.startswith(('http://', 'https://', '/', 'attachment:', 'blob:', 'data:')):
            src = f'{pathlib.Path(self.img_dir)}/{src}'
        return template.format(src, token.children[0].content if token.children else '', title)

# %% ../nbs/02_franken.ipynb
def render_md(md_content:str, # Markdown content
             class_map=None, # Class map
             class_map_mods=None, # Additional class map
             img_dir:str=None, # Directory containing images
             renderer=FrankenRenderer # custom renderer
             )->FT: # Rendered markdown
    "Renders markdown using mistletoe and lxml with custom image handling"
    if md_content=='': return md_content
    html_content = mistletoe.markdown(md_content, partial(renderer, img_dir=img_dir))
    return NotStr(apply_classes(html_content, class_map, class_map_mods))

</fasthtml example of modified mistletoe render>


<misteltoe contrib examples>
"""
GitHub Wiki support for mistletoe.
"""

import re
from mistletoe.span_token import SpanToken
from mistletoe.html_renderer import HtmlRenderer


__all__ = ['GithubWiki', 'GithubWikiRenderer']


class GithubWiki(SpanToken):
    pattern = re.compile(r"\[\[ *(.+?) *\| *(.+?) *\]\]")

    def __init__(self, match):
        self.target = match.group(2)


class GithubWikiRenderer(HtmlRenderer):
    def __init__(self, **kwargs):
        """
        Args:
            **kwargs: additional parameters to be passed to the ancestor's
                      constructor.
        """
        super().__init__(GithubWiki, **kwargs)

    def render_github_wiki(self, token):
        template = '<a href="{target}">{inner}</a>'
        target = self.escape_url(token.target)
        inner = self.render_inner(token)
        return template.format(target=target, inner=inner)

"""
Table of contents support for mistletoe.

See `if __name__ == '__main__'` section for sample usage.
"""

import re
from mistletoe.html_renderer import HtmlRenderer
from mistletoe import block_token


class TocRenderer(HtmlRenderer):
    """
    Extends HtmlRenderer class for table of contents support.
    """
    def __init__(self, *extras, depth=5, omit_title=True, filter_conds=[], **kwargs):
        """
        Args:
            extras (list): allows subclasses to add even more custom tokens.
            depth (int): the maximum level of heading to be included in TOC.
            omit_title (bool): whether to ignore tokens where token.level == 1.
            filter_conds (list): when any of these functions evaluate to true,
                                current heading will not be included.
            **kwargs: additional parameters to be passed to the ancestor's
                      constructor.
        """
        super().__init__(*extras, **kwargs)
        self._headings = []
        self.depth = depth
        self.omit_title = omit_title
        self.filter_conds = filter_conds

    @property
    def toc(self):
        """
        Returns table of contents as a block_token.List instance.
        """
        def get_indent(level):
            if self.omit_title:
                level -= 1
            return ' ' * 4 * (level - 1)

        def build_list_item(heading):
            level, content = heading
            template = '{indent}- {content}\n'
            return template.format(indent=get_indent(level), content=content)

        lines = [build_list_item(heading) for heading in self._headings]
        items = block_token.tokenize(lines)
        return items[0]

    def render_heading(self, token):
        """
        Overrides super().render_heading; stores rendered heading first,
        then returns it.
        """
        rendered = super().render_heading(token)
        content = self.parse_rendered_heading(rendered)
        if not (self.omit_title and token.level == 1
                or token.level > self.depth
                or any(cond(content) for cond in self.filter_conds)):
            self._headings.append((token.level, content))
        return rendered

    @staticmethod
    def parse_rendered_heading(rendered):
        """
        Helper method; converts rendered heading to plain text.
        """
        return re.sub(r'<.+?>', '', rendered)


TOCRenderer = TocRenderer
"""
Deprecated name of the `TocRenderer` class.
"""

from mistletoe import HtmlRenderer
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name as get_lexer, guess_lexer
from pygments.styles import get_style_by_name as get_style
from pygments.util import ClassNotFound


class PygmentsRenderer(HtmlRenderer):
    formatter = HtmlFormatter()
    formatter.noclasses = True

    def __init__(self, *extras, style='default', fail_on_unsupported_language=False, **kwargs):
        """
        Args:
            extras (list): allows subclasses to add even more custom tokens.
            style (str): short name of the style to be used by Pygments' `HtmlFormatter`,
                      see `pygments.styles.get_style_by_name()`.
            fail_on_unsupported_language (bool): whether to let Pygments' `ClassNotFound`
                      be thrown when there is an unsupported language found on
                      a code block.
                      If `False`, then language is guessed instead of throwing the error.
            **kwargs: additional parameters to be passed to the ancestor's
                      constructor.
        """
        super().__init__(*extras, **kwargs)
        self.formatter.style = get_style(style)
        self.fail_on_unsupported_language = fail_on_unsupported_language

    def render_block_code(self, token):
        code = token.content
        lexer = None

        if token.language:
            try:
                lexer = get_lexer(token.language)
            except ClassNotFound as err:
                if self.fail_on_unsupported_language:
                    raise err

        if lexer is None:
            lexer = guess_lexer(code)

        return highlight(code, lexer, self.formatter)
</misteltoe contrib examples>