from bs4 import BeautifulSoup


def modify_html(html: str, href: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.new_tag('a',
                     href=href,
                     title='Download',
                     download=None
                     )
    a['class'] = 'md-content__icon pdf-download-btn'
    i = soup.new_tag('i')
    i['class'] = 'fa fas fa-download'
    small = soup.new_tag('small')
    a.append(i)
    small.append(' PDF')
    a.append(small)
    if soup.article:
        soup.article.insert(0, a)
    else:
        soup.find('div', **{'role': 'main'}).insert(0, a);
    return str(soup)


def modify_html_material(html: str, href: str) -> str:
    # Taken from mkdocs-pdf-export-plugin for material theme.
    # https://github.com/zhaoterryy/mkdocs-pdf-export-plugin/blob/46af862318c92996913a81cab07cc998a871c2cb/mkdocs_pdf_export_plugin/themes/material.py#L65-L71
    a_tag = "<a class=\"md-content__button md-icon\" download href=\"%s\" title=\"PDF Export\">" % href
    icon = '<svg style="height: 1.2rem; width: 1.2rem;" viewBox="0 0 384 512" xmlns="http://www.w3.org/2000/svg"><path d="M224 136V0H24C10.7 0 0 10.7 0 24v464c0 13.3 10.7 24 24 24h336c13.3 0 24-10.7 24-24V160H248c-13.2 0-24-10.8-24-24zm76.45 211.36l-96.42 95.7c-6.65 6.61-17.39 6.61-24.04 0l-96.42-95.7C73.42 337.29 80.54 320 94.82 320H160v-80c0-8.84 7.16-16 16-16h32c8.84 0 16 7.16 16 16v80h65.18c14.28 0 21.4 17.29 11.27 27.36zM377 105L279.1 7c-4.5-4.5-10.6-7-17-7H256v128h128v-6.1c0-6.3-2.5-12.4-7-16.9z"></path></svg>'
    button_tag = a_tag + icon + "</a>"
    insert_point = "<article class=\"md-content__inner md-typeset\">"
    html = html.replace(insert_point, insert_point + button_tag)
    return html


def gen_address(config):
    soup = BeautifulSoup('<body></body>',
                         'html5lib'
                         )
    address = soup.new_tag('address')
    p = soup.new_tag('p')
    for k, line in {'author': config['author'],
                    'company': config['company']}.items():
        if line:
            sp = soup.new_tag('p', **{'class': k})
            sp.append("{}".format(line))
            p.append(sp)
    address.append(p)
    if config['copyright']:
        span = soup.new_tag('p',
                            id="copyright"
                            )
        span.append(config['copyright'])
        address.append(span)
    return address


def is_external(href: str):
    return href.startswith('http://') or href.startswith('https://')
