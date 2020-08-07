import sys
from os import listdir, basename
import re
import json
from crawler2 import getTitle

keyword=sys.argv[1]
keyword=str(keyword)
filelist=[]
db='C:\\Users\\monik\\Documents\\searchengine\\db'
filestoparse=listdir(db)
for file in filestoparse:
    with open(file,  'r') as f:
        filecontent=str(f.read())
        result=re.findall(keyword, filecontent)
        webrankscore=len(result)
        if len(result)>=2:
            filelist.append(basename(f.name))
            counter=0
            for x in range(len(filecontent):
                y=x-1
                if filecontent[x]==keyword:
                    counter+=1
results={}
x=1
for item in filelist:
    results[x]=filelist.index(item)
    x+=1
    results[x]=getTitle(item)
out_file = open("C:\\Users\\monik\\Documents\\searchengine\\results.json", "w+") 
json.dump(results, out_file) 
out_file.close()

