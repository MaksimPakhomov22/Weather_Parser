import time
import os
import requests
from dotenv import load_dotenv

load_dotenv()


class Weather:

    def __init__(self, city):
        self.city = city

    def get_weather(self):
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'q': self.city, 'APPID': os.getenv('APPID')}

        weather_json = requests.get(url=url, params=params).json()
        wj = weather_json["main"]["temp"]
        temp = wj - 273.15
        return f'{self.city}: {round(temp)}°C'


while True:
    city_ = input('Введите город, или введите "Q" для выхода из программы: ').title().strip()
    try:
        if city_ == 'Q':
            break
        else:
            w = Weather(city_)
            req = w.get_weather()
            print(time.strftime('%X'))
            print(req)
    except:
        print('Неверное название!')
