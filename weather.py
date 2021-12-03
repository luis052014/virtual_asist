import requests, json 
from os import getenv
from dotenv import load_dotenv



def weather_api(city_name):
    api_key = getenv("WEATHER_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404" or x["cod"] != "401":
        y = x["main"]
        temperature = y["temp"]
        pressure = y["pressure"]
        humidity = y["humidity"]
        z = x["weather"] 
        description = z[0]["description"] 
        temperature=round(temperature-273.15, 2)

        traslator = {
            'broken clouds':'Poco nublado',
            'overcast clouds':'Nublado',
            'sacattered clouds':'Nuves Dispersas',
            'light rain':'Lluvia ligera',
            'clear sky':'Cielo limpio',
            'few clouds':'Pocas nuves',
            'moderate rain':'Lluvia moderada',
            'mist':'Neblina'
            }
        traslation = description
        for k, v in traslator.items():
            if k == description:
                traslation = v

        clima = 'la temperatura en '+ city_name+ ' es de '+ str(temperature)+ ' grados celsius, con una presion atmosferica de '+ str(pressure)+ ', '+str(humidity)+' porciento de humedad,  '+ str(traslation)

        return str(clima)
