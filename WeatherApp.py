import requests
import tkinter as tk
from tkinter import simpledialog, messagebox
from math import ceil

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
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

def display_weather_in_gui(weather_data):
    if weather_data:
        city_info = weather_data['city']
        forecasts = weather_data['list']

        # Round up temperature values
        current_temp = ceil(forecasts[0]['main']['temp'])
        min_temp = ceil(forecasts[1]['main']['temp_min'])
        max_temp = ceil(forecasts[1]['main']['temp_max'])  # Use the last element for max temperature

        result_text = (
            f"Weather in {city_info['name']}, {city_info['country']}:\n\n"
            f"Current Temperature: {current_temp}°C\n\n"
            f"Description: {forecasts[0]['weather'][0]['description']}\n\n"
            f"Min Temperature: {min_temp}°C\n\n"
            f"Max Temperature: {max_temp}°C\n\n"
        )

        if 'rain' in forecasts[1]:
            result_text += f"Precipitation: {forecasts[1]['rain']['3h']}mm (3-hour forecast)\n\n"
        else:
            result_text += "Precipitation data not available\n\n"

        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Weather Information", result_text)
    else:
        messagebox.showerror("Error", "Unable to retrieve weather data.")

def get_city_from_user():
    root = tk.Tk()
    root.withdraw()
    city = simpledialog.askstring("City", "Enter city name:")
    return city

def main():
    api_key = 'd3654a5c12054b86b0eff2244171e397'  # Replace with your actual OpenWeatherMap API key
    city = get_city_from_user()

    if city:
        weather_data = get_weather(api_key, city)
        display_weather_in_gui(weather_data)

if __name__ == "__main__":
    main()
