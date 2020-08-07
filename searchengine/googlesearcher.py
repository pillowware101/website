from googlesearch import search
from sys import argv
  
# to search 
query = sys.argv[1]
tld=sys.srgv[2]
num=sys.argv[3]
stop=sys.argv[4]
pause=sys.agv[5]
  
for j in search(query, tld, num, stop, pause): 
    print(j) 
