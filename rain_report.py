#!/usr/bin/python
from requests import get
from json import loads
from datetime import datetime
from helper import clickable, open_with_less,Block
from pathlib import Path


full_web = "http://wttr.in/huillapima"
web= "http://wttr.in/huillapima?format=j1"
tmp_file = '/tmp/huillapima_weather'
tmp_file_short = '/tmp/huillapima_weather_out'
# Si tenemos probabilidad de lluvia de mas del 40% 

def noclick():
    rain_chances=[]
    rain_totals=[]
    dates=[]
    data = loads(get(web).text)
    weather = data["weather"]
    for day in weather:
        dates.append(day["date"])
        max_chance=0
        total_daily_rain=0
        reports = day["hourly"]

        for report in reports:
            if max_chance < float(report["chanceofrain"]):
                max_chance = float(report["chanceofrain"])
                total_daily_rain += float(report["precipMM"])

        rain_totals.append(total_daily_rain)
        rain_chances.append(max_chance)

    rain_is_coming=False
    for day, chance in enumerate(rain_chances):
        if chance > 0.5:
            rain_is_coming=True
            break
    if rain_is_coming:
        weekday = datetime.strptime(dates[day],"%Y-%m-%d").strftime("%a")
        stri = 'ECA:' + weekday + "🌧" + rain_chanc[day] + '% ' + rain_totals[day]+"mm"
        data = get(full_web).text
        with open(tmp_file,'w') as f:
            f.write(data)
        with open(tmp_file_short,'w') as f:
            f.write(stri)


def leftclick():
    open_with_less(tmp_file,font='mono=9',window_class='Weather')

def out():
    try:
        with open(tmp_file_short) as f:
            return f.read()
    except:
        return '' 



block = Block(out,noclick=noclick,leftcmd=leftclick)
block()
