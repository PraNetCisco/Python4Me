import requests

def get_weather_desc_and_temp(city):
    api_key = "710c60a653a5b61c51f671789c9ad2ce"
    state = "California"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"
    #url2 = "http://api.openweathermap.org/data/2.5/weather?q="+city+"+state+""&appid="+api_key+"&units=imperial"
        
    request = requests.get(url)
    json = request.json()
        
    # print (json)

    description = json.get("weather")[0].get("description")
    temp_max = json.get("main").get("temp_max")
    temp_min = json.get("main").get("temp_min")
    
    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}
    
def main ():
    
    city = input("Enter the name of the city:\n")
    weather_dict = get_weather_desc_and_temp(city)
    print ("Weather today in", city, "is", weather_dict.get('description'))
    print ("Max temp today in", city, "is", weather_dict.get('temp_max'))
    print ("Min temp today in", city, "is", weather_dict.get('temp_min'))

main()