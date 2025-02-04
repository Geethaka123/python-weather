from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="matara"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n*** Get current weather conditions ***\n')

    city = input('\nplz enter a city name: ')

    # Check for empty strings or strings with only spaces
    if not bool(city.strip()):
        city = "matara"

    weather_data = get_current_weather(city)

    print('\n')
    pprint(weather_data)