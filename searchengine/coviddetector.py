import requests
from sys import argv

country=argv[1]
url='https://coronavirus-19-api.herokuapp.com/countries/'
try:
    json1=requests.get(url).json()
    json1.country=country
    print(json1)
except:
    print('could not load json')
