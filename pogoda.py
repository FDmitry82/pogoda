import requests

API_key = "56441434804e9fc59c7388be4240656b&lang=ru"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Введите название города. Пример (Moscow, Pervouralsk, Ekaterinburg): ")
Final_url = base_url + "&units=metric&appid=" + API_key + "&q=" + city_name
weather_data = requests.get(Final_url).json()

# Вытаскиваем из JSON Имя города
name_city = weather_data['name']
# Вытаскиваем из JSON температуру
temp = weather_data['main']['temp']
# Вытаскиваем из JSON давление
pressure = weather_data['main']['pressure']
# Вытаскиваем из JSON влажность
humidity = weather_data['main']['humidity']
# Вытаскиваем из JSON скорость ветра
wind_speed = weather_data['wind']['speed']
# Вытаскиваем из JSON что сейчас на небе
description = weather_data['weather'][0]['description']
# Вытаскиваем из JSON Штрота
latitude = weather_data['coord']['lat']
# Вытаскиваем из JSON долгота
longitude = weather_data['coord']['lon']

# Printing Data
print('\nГород: ', name_city,
      '\nТемпература C`: ', temp,
      '\nСкорость ветра : ',wind_speed,
      '\nДавление : ',pressure,
      '\nВлажность : ',humidity,
      '\nОписание неба : ',description,
      '\nШирота : ',latitude,
      '\nДолгота : ',longitude)

print('\nСписок всех параметров JSON: ', weather_data)