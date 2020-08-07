import urllib
import requests
from Tkinter import *

root = Tk()
L1 = Label(root, text="query")
E1 = Entry(root, bd =5)
query=str(E1)
url=urllib.urlopen('https://www.ecosia.org')
def ecosiaSearch(query):
    with requests.session() as c:
        query = {'q': query}
        urllink = requests.get(url, params=query)
        print urllink.url

ecosiaSearch('Linkin Park')



E1.pack(side = RIGHT)
L1.pack( side = LEFT)
root.mainloop()
