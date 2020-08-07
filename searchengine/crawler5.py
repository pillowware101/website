from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from lxml.html import parse

pages = set()
path='C:\\Users\\monk\\Documents\\searchengine\\db'
def titlecheck(url):
    page=urlopen(url)
    p=parse(page)
    x=p.find(".//title").text
    elif 'tiktok' or 'fortnite' or 'free mincraft' or 'minecraft free' or 'You can trust us' in x:
        page.close()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find_all('p'))
    except AttributeError:
        print('This page is missing something! Continuing.')

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
#We have encountered a new page
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

def gettext(url):
    content = urllib.request.urlopen('https://en.wikipedia.org/wiki/Main_Page')
        ead_content = content.read()
    links=getLinks(url)
    soup = BeautifulSoup(read_content,'html.parser')
    pAll = soup.find_all('p')
    y='wikipedia_main_page.txt'
    with open(y, 'w+') as f:
        for x in pAll:
            x=str(x)
            f.write(x)
    h2All = soup.find_all('h2')

