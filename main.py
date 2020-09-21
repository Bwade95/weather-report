import requests

API_KEY = "API_KEY" # enter your own key here
WS_URL = "http://api.weatherstack.com/current"

cities = []
with open('cities.txt') as f:
  for line in f:
    cities.append(line.strip())
print(cities)

for city in cities:
  parameters = {'access_key': API_KEY, 'query': city} 
  response = requests.get((WS_URL), parameters)
  js = response.json()

  temperature = js['current']['temperature']
  theDate = js['location']['localtime']
  city = js['location']['name']
  country = js['location']['country']

  with open(f"{city}.txt", "a") as f:
    f.write(f"Date/Time: {theDate}, Temperature(Celsius): {temperature}\n")