import requests

API_KEY = "API_KEY" # enter your own key here
WS_URL = "http://api.weatherstack.com/current"

city = "city" # enter your city here

parameters = {'access_key': API_KEY, 'query': city}

response = requests.get((WS_URL), parameters)
js = response.json()

temperature = js['current']['temperature']
theDate = js['location']['localtime']
city = js['location']['name']
country = js['location']['country']

print(f"The temperature in {city}, {country} on {theDate} is {temperature} degrees Ceslius")