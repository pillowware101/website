import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = input('what is the url you want to download')
filename=url

response = urllib.request.urlopen(url)
webContent = response.read()
webContent=str(webContent)

