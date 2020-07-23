#!/usr/bin/python
from requests import get
from helper import open_with_less, Block
from pathlib import Path

url="http://wttr.in/?format=1"
url_full="http://wttr.in/"
report = '/tmp/bs_as_weather'
tmp_out = '/tmp/bs_as_weather_out'

def noclick():
    data = get(url_full).text
    with open(report,"w") as f:
        f.write(data)
    with open(tmp_out,'w') as f:
        f.write(get(url).text)

def leftclick():
    if not Path(tmp_out).exists() and Path(report).exists():
        noclick()
        leftclick()
    else:
        open_with_less(report,font='mono-9',window_class='Weather')


def out():
    with open(tmp_out) as f:
        return f.read().rstrip('\n')

block = Block(out,noclick=noclick,leftcmd=leftclick)
block()
