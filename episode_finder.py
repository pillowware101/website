import json
import webbrowser
from time import sleep
from tkinter import *

with open('stuff.json', 'r') as f:
    f=f
    x=json.load(f)
y=x[0]["url"]
print('opening ', x[0]["series"], ', episode ', x[0]["episode"], '...')
sleep(5)
webbrowser.open(y)