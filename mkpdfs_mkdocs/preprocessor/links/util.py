import os

from weasyprint import urls
from bs4 import BeautifulSoup


# check if href is relative --
# if it is relative it *should* be an html that generates a PDF doc
def is_doc(href: str):
    if urls.url_is_absolute(href):
        return False
    if os.path.isabs(href):
        return False

    return True


def rel_pdf_href(href: str):
    head, tail = os.path.split(href)
    filename, _ = os.path.splitext(tail)

    internal = href.startswith('#')
    if not is_doc(href) or internal:
        return href

    return urls.iri_to_uri(os.path.join(head, filename + '.pdf'))

def abs_asset_href(href: str, base_url: str):
    if urls.url_is_absolute(href) or os.path.isabs(href):
        return href

    return urls.iri_to_uri(urls.urljoin(base_url, href))

# makes all relative asset links absolute
def replace_asset_hrefs(soup: BeautifulSoup, base_url: str):
    for link in soup.find_all('link', href=True):
        link['href'] = abs_asset_href(link['href'], base_url)

    for asset in soup.find_all(src=True):
        asset['src'] = abs_asset_href(asset['src'], base_url)

    return soup


def normalize_href(href: str, rel_url: str):
    """
    Normalize href to site root
    foo/bar/baz/../../index.html -> foo/index.html
    :param href:
    :param rel_url:
    :return:

    >>> normalize_href("../../index.html", "foo/bar/baz/page.html")
    'foo/index.html'

    >>> normalize_href("page2.html#abcd", "foo/bar/baz/page.html")
    'foo/bar/baz/page2.html#abcd'

    >>> normalize_href("#section", "foo/bar/baz/page.html")
    'foo/bar/baz/page.html#section'

    >>> normalize_href("/index.html", "foo/bar/baz/page.html")
    '/index.html'

    >>> normalize_href("http://example.org/index.html", "foo/bar/baz/page.html")
    'http://example.org/index.html'
    """
    if not is_doc(href):
        return href
    if href.startswith("#"):
        return rel_url + href
    rel_dir = os.path.dirname(rel_url)
    return os.path.normpath(os.path.join(rel_dir, href))


def get_body_id(url: str):
    return '{}:'.format(url)