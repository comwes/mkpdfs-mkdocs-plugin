from bs4 import BeautifulSoup


def modify_html(html: str, href: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.new_tag('a', href=href, title='Télécharger', download=None)
    a['class'] = 'md-icon md-content__icon'
    a.string = '\uE2C4'
    soup.article.insert(0, a)
    return str(soup)


def gen_address (config):
    soup = BeautifulSoup('<body></body>','html5lib')
    address = soup.new_tag('address')
    p = soup.new_tag('p')
    s = "{}\n{}\n".format(config['author'],config['company'])
    p.append(s)
    address.append(p)
    span = soup.new_tag('p', id="copyright")
    span.append(config['copyright'])
    address.append(span)
    return address
