import requests
from bs4 import BeautifulSoup
import json

#найти: кол-во облаков; температура; скорость ветра; влажность; давление;
url = "https://www.meteoservice.ru/weather/hourly/lefortovo"
pagebs = BeautifulSoup(requests.get(url).text, "lxml")
today_waether = pagebs.find('div', class_="forecast-rows hourly-vertical").find_all('div', onclick="$(this).toggleClass('expanded')")

final = [None]*24
cnt = 0

for i in today_waether:
    final[cnt] = [i.find('div', title="Температура").text.strip()[:-1], #температура в градусах цельсия
                  i.find('div', class_="small-12 medium-4 columns advanced-params").find('span', class_="value").text[:-1], #кол-во облаков %
                  i.contents[3].contents[11].find('span', class_="value").text[:-11], #давление мм рт. ст.
                  i.contents[3].contents[11].contents[5].contents[1].text[:-1], #влажность %
                  i.contents[3].contents[15].contents[3].contents[1].text[:-4], #скорость ветра м/c
                  ]
    cnt += 1
print(final)





