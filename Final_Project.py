import sys, os, pygame, random, requests
from pygame.locals import *

# Инициализируем переменные
# Начальное положение корабля
import sys
# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {"geocode": toponym_to_find, "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    # обработка ошибочной ситуации
    pass

# Преобразуем ответ в json-объект
json_response = response.json()
# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]
# Долгота и Широта :
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

delta = "0.005"

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": ",".join([delta, delta]),
    "l": "map"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)
# Преобразуем ответ в json-объект
json_response = response.json()

# Получаем первую найденную организацию.
organization = json_response["features"][0]["properties"]["CompanyMetaData"]
# Название организации.
org_name = organization["name"]
# Адрес организации.
org_address = organization["address"]

# Получаем координаты ответа.
org_point = json_response["properties"]["ResponseMetaData"]["SearchResponse"]["Point"]["coordinates"]

delta = "0.005"

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
        "ll": address_ll, # позиционируем карту центром на наш исходный адрес
        "spn": ",".join([delta, delta]),
        "l": "map",
        "pt": "{ll},pm2dgl".format(org_point)
        }

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)