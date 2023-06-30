import requests

url = 'http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/49686'
api_key = 'bu1k5RzAQkW00uDa7RKCeWd9hyLMREAe'

# Construct headers with API key
headers = {'apikey': api_key}

# Send GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Request failed with status code:', response.status_code)
