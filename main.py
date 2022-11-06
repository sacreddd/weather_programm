import requests
from bs4 import BeautifulSoup

#найти: кол-во облаков; температура; скорость ветра; влажность; давление;
url = "https://www.meteoservice.ru/weather/hourly/lefortovo"
pagebs = BeautifulSoup(requests.get(url).text, "lxml")
today_waether = pagebs.find('div', class_="forecast-rows hourly-vertical")
print(today_waether)
for i in range(23):
    gg = today_waether.find('div', onclick="$(this).toggleClass('expanded')")
    print(gg)
    break
