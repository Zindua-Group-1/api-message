import pywhatkit
import requests


api_key='2d435de4a2683a4780c7ec1c23f1a0cb'

phone_number=input('Phone number:')
city=input('City:')

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"


response = requests.get(url)
data=response.json()

condition=data['weather'][0]['main']
description=data['weather'][0]['description']
temp=data['main']['temp']
country=data['sys']['country']

pywhatkit.sendwhatmsg(phone_number,f'The weather of {city} is:\n{condition}\nDescription: {description} \nTemperature: {temp} celcius \nCountry: {country} ',17,37,15)