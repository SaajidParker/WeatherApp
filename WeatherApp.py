import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data.get('message', 'Unknown error')}")
            return None

    except requests.ConnectionError:
        print("Failed to connect to the API.")
        return None

def display_weather(weather_data):
    if weather_data:
        main_info = weather_data['main']
        weather_info = weather_data['weather'][0]

        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Temperature: {main_info['temp']}°C")
        print(f"Description: {weather_info['description']}")
    else:
        print("Unable to retrieve weather data.")

def main():
    api_key = 'd3654a5c12054b86b0eff2244171e397'  # Replace with your actual OpenWeatherMap API key
    city = input("Enter city name: ")

    weather_data = get_weather(api_key, city)

    display_weather(weather_data)

if __name__ == "__main__":
    main()
