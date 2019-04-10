from bs4 import BeautifulSoup


def modify_html(html: str, href: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.new_tag('a', href=href, title='Download', download=None)
    a['class'] = 'md-content__icon pdf-download-btn'
    i = soup.new_tag('i')
    i['class'] = 'fa fa-download'
    small = soup.new_tag('small')
    small.append(i)
    small.append(' PDF')
    a.append(small)
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
