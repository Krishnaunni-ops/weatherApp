"""
Student Name: Unni Krishna Prasad Endla
Course Name: Python Programming
Project Title: Weather Forecast Application
"""

import requests

API_KEY = "c4b1f892948856bf61f04a34491c6a62"
CURRENT_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast?"

def get_weather_data(url, params):
    """
    Fetches weather data from the specified URL with the given parameters.
    
    Parameters:
    url (str): The API endpoint URL.
    params (dict): The parameters for the API request.
    
    Returns:
    dict: A dictionary containing weather data.
    """
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    return None

def display_current_weather(data):
    """
    Displays the current weather information.
    
    Parameters:
    data (dict): The weather data dictionary.
    """
    if data and data.get("cod") != "404":
        main = data["main"]
        wind = data["wind"]
        weather = data["weather"][0]
        print("\nCurrent Weather:")
        print(f"Temperature: {main['temp']}°K")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Weather: {weather['description']}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("City Not Found!")

def display_extended_forecast(data):
    """
    Displays the extended weather forecast.
    
    Parameters:
    data (dict): The forecast data dictionary.
    """
    if data and data.get("cod") != "404":
        print("\nExtended Forecast:")
        for forecast in data["list"][:5]:  # Displaying next 5 time intervals (3-hour intervals)
            dt_txt = forecast["dt_txt"]
            main = forecast["main"]
            weather = forecast["weather"][0]
            print(f"{dt_txt} - {weather['description']}, Temp: {main['temp']}°K, Humidity: {main['humidity']}%")
    else:
        print("City Not Found!")

def validate_input(city):
    """
    Validates the user input.
    
    Parameters:
    city (str): The city name or zip code input by the user.
    
    Returns:
    bool: True if input is valid, False otherwise.
    """
    if city.isdigit() or city.isalpha() or (city.replace(" ", "").isalpha()):
        return True
    else:
        print("Invalid input. Please enter a valid city name or zip code.")
        return False

def main():
    """
    Main function to run the weather forecast application.
    """
    city = input("Enter city name or zip code: ")
    if not validate_input(city):
        return

    params = {"q": city, "appid": API_KEY}

    current_weather_data = get_weather_data(CURRENT_WEATHER_URL, params)
    display_current_weather(current_weather_data)

    forecast_data = get_weather_data(FORECAST_URL, params)
    display_extended_forecast(forecast_data)

if __name__ == "__main__":
    main()
