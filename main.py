import requests
from bs4 import BeautifulSoup

#найти: кол-во облаков; температура; скорость ветра; влажность; давление;
url = "https://www.meteoservice.ru/weather/hourly/lefortovo"
pagebs = BeautifulSoup(requests.get(url).text, "lxml")
today_waether = pagebs.find('div', class_="forecast-rows hourly-vertical")
gg = today_waether.find_all('div', onclick="$(this).toggleClass('expanded')")
print('bruh')

# for i in range(23):
#     gg = today_waether.find('div', onclick="$(this).toggleClass('expanded')")
#     hh = gg.text
#     print(hh)
#     break



# markers = ['облака', 'облаков', 'давление']
# for i in range(len(hh)):
#     if hh[i] in markers or :





