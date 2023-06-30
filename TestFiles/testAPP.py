import requests

url = 'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/49686'
api_key = 'bu1k5RzAQkW00uDa7RKCeWd9hyLMREAe'

# Append API key as a query parameter
url_with_key = f'{url}?apikey={api_key}'

# Send GET request
response = requests.get(url_with_key)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Request failed with status code:', response.status_code)
