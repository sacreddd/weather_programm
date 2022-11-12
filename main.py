import requests
from bs4 import BeautifulSoup
import schedule
import time
import json
from datetime import datetime

url = "https://www.meteoservice.ru/weather/hourly/lefortovo"


def weather_check():
    pagebs = BeautifulSoup(requests.get(url).text, "lxml")
    today_waether = pagebs.find('div', class_="forecast-rows hourly-vertical").find_all('div',
                                                                                        onclick="$(this).toggleClass('expanded')")

    final = [None] * 24
    cnt = 0

    for i in today_waether:
        final[cnt] = {'hour': cnt,
                      'temp': i.find('div', title="Температура").text.strip()[:-1],  # температура в градусах цельсия
                      'obl': i.find('div', class_="small-12 medium-4 columns advanced-params").find('span',
                                                                                                    class_="value").text[
                             :-1],  # кол-во облаков %
                      'davl': i.contents[3].contents[11].find('span', class_="value").text[:-11],  # давление мм рт. ст.
                      'vlazhn': i.contents[3].contents[11].contents[5].contents[1].text[:-1],  # влажность %
                      'windvel': i.contents[3].contents[15].contents[3].contents[1].text[:-4],  # скорость ветра м/c
                      }
        cnt += 1

    try:
        data = json.load(open('data.json'))
    except:
        data = []
    data.append({str(datetime.now()):final})
    with open('data.json', 'w', ) as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


schedule.every().day.at("17:22").do(weather_check)

while True:
    schedule.run_pending()
    time.sleep(1)
