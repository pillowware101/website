from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import re

pages = set()
def getText(domain, pageUrl):
    html=urlopen(domain+pageUrl)
    bs = BeautifulSoup(html.read(), 'html.parser')
    nameList = [bs.findAll('p'), bs.findAll('h1'), bs.findAll('h2'),
        bs.findAll('h3'), bs.findAll('h4'), bs.findAll('h5'), bs.findAll('h6'), bs.findall('title')]
    url=domain+pageUrl
    url='C:\\Users\\monik\\Documents\\searchengine\\db'+url
    with open(url,  'w+') as f:
        f.write(nameList)
        f.close()

def getTitle(url):
    html=urlopen(url)
    bs = BeautifulSoup(html.read(), 'html.parser')
    title=bs.findall('title')
    return title
    
def getLinks(pageUrl, domain):
    global pages
    url=domain+pageUrl
    html = urlopen(domain+pageUrl)
    bsObj = BeautifulSoup(html, features='lxml')
    text=getText(domain, pageUrl)
    title=getTitle
    for link in bsObj.findAll("a"):
        with open (url, 'w+') as f:
            f.write(link)
            f.write(text)
            f.write(title)
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
#We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(domain,  newPage)

urluno=sys.argv[1]

getTitle(urluno)
