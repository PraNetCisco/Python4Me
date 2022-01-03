import requests
  
url = "http://api.openweathermap.org/data/2.5/weather?q=London&units=imperial&appid=67da29cb91129f1a68c1c06c1be92daa"
request = requests.get(url)

weather_json = request.json()
print(weather_json)

main_weather = weather_json['main']
coordinates = weather_json['coord']

temp = main_weather['temp']
print ("The Circus's current temperature is", temp)
