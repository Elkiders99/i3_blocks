#!/usr/bin/python
from requests import get
from json import loads
from datetime import datetime
from helper import clickable
import subprocess

tmp_file = '/tmp/vla_snow'
full_forecast = 'https://www.snow-forecast.com/resorts/Cerro-Bayo/6day/mid'
web="http://wttr.in/villa+la+angostura?format=j1"

def noclick():
    snow_chances=[]
    dates=[]
    data = loads(get(web).text)
    weather = data["weather"]

    for day in weather:
        dates.append(day["date"])
        max_chance=0

        reports = day["hourly"]
        for report in reports:
            if max_chance < float(report["chanceofsnow"]):
                max_chance = float(report["chanceofsnow"])
        snow_chances.append(max_chance)

    snow_is_coming=False
    for day, chance in enumerate(snow_chances):
        if chance > 40:
            snow_is_coming=True
            break

    if snow_is_coming:
        weekday = datetime.strptime(dates[day],"%Y-%m-%d").strftime("%a")
        out = f'VLA-> {weekday} 🌧 {snow_chances[day]} % '
        with open(tmp_file,'w') as cache:
            cache.write(out)

def out():
    with open(tmp_file,'r') as f:
        print(f.read())

def leftclick():
    subprocess.Popen(['xdg-open',full_forecast],stdout=subprocess.DEVNULL)

@clickable
def main(button):
    if button == 1:
        leftclick()
    else:
        noclick()
    out()
main()
