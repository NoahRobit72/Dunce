import requests
import json

def fetch_weather_data(url, api_key):
    # Append API key as a query parameter
    url_with_key = f'{url}?apikey={api_key}'

    # Send GET request
    response = requests.get(url_with_key)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        write_message_to_json(data, "weatherData.json")
        print("Message printed.")
    else:
        print('Request failed with status code:', response.status_code)

def write_message_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)



def main():
    # Example usage
    url = 'https://dataservice.accuweather.com/forecasts/v1/hourly/12hour/30602'
    api_key = 'bu1k5RzAQkW00uDa7RKCeWd9hyLMREAe'
    
    
    # Your main function code here
    print("Running the main function.")
    fetch_weather_data(url, api_key)


if __name__ == "__main__":
    main()

