import os

from .util import is_doc, normalize_href

# normalize href to #foo/bar/section:id
def transform_href(href: str, rel_url: str):
    if not is_doc(href):
        return href
    if '#' not in href:
        href += '#'
    return "#" + normalize_href(href, rel_url).replace("#", ":", 1)

# normalize id to foo/bar/section:id
def transform_id(id: str, rel_url: str):
    head, section = os.path.split(rel_url)

    if len(head) > 0:
        head += '/'

    return '{}{}:{}'.format(head, section, id)
