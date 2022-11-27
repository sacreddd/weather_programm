import matplotlib.pyplot as plt
import json


def gdraw(data):
    global text
    with open('data.json', 'r', encoding='utf-8') as f:
        text = json.loads(f.read())  # закинули json в переменную
        for i in range(len(text)):  # перебираем дни
            if text[i].get(data) is not None:
                hour = []
                temp = []
                obl = []
                davl = []
                vlazhn = []
                windvel = []
                for y in text[i].values():  # перебираем часы
                    for k in y:
                        # adding values from json file to arrays
                        hour.append(int(k['hour']))
                        temp.append(k['temp'])
                        obl.append(int(k['obl']))
                        davl.append(int(k['davl']))
                        vlazhn.append(int(k['vlazhn']))
                        windvel.append(int(k['windvel']))

                plt.figure(figsize=(15, 7))  # picture's size
                plt.subplots_adjust(wspace=0.2, hspace=0.3)  # distance between graphs
                plt.suptitle(f"Данные на {data}")
                # clouds

                plt.subplot(2, 2, 1)  # position of graph on picture
                plt.title("Облака")  # title's name
                plt.xlabel('час')  # x axis's name
                plt.plot(hour, obl)  # arrays for graph
                plt.xticks(hour)  # step for every hour

                # temperature

                plt.subplot(2, 2, 2)
                plt.title("Температура")
                plt.xlabel('час')
                plt.ylabel('C')
                plt.plot(hour, temp)
                plt.xticks(hour)

                # wind's speed

                plt.subplot(2, 2, 3)
                plt.title("Скорость ветра")
                plt.xlabel('час')
                plt.ylabel('м/с')
                plt.plot(hour, windvel)
                plt.xticks(hour)

                # humidity

                plt.subplot(2, 2, 4)
                plt.title("Влажность")
                plt.xlabel('час')
                plt.ylabel('%')
                plt.plot(hour, vlazhn)
                plt.xticks(hour)

                # print & save graphs
                plt.savefig(f"{data}.png")
