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
