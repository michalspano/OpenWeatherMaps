# -*- coding: utf-8 -*-
# author: @michalspano
# utils.formatting.py
# Contains formatting functions, custom functions

from utils.utils import extract_data
from utils.color import Colors
from os import linesep as nl # handle different systems

def format_api_url(lat: float, lon: float, KEY: str, unit: str) -> str:
    '''Format the URL'''

    return f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={KEY}&units={unit}'


def format_simple(fetched_data: dict, location: str) -> str:
    '''Format the output (simple version)'''

    data = extract_data(fetched_data)

    lat = data['lat']
    lon = data['lon']
    description = data['description']
    temp = data['temp']

    # return the formatted output (simple version)
    return f"{Colors.GREEN}{location}{Colors.RESET} ({lat}°, {lon}°) ~ " \
           f"'{description}' ({Colors.CYAN}{temp}°C{Colors.RESET})"


def format_scientific(fetched_data: dict, location: str) -> str:
    '''Format the output (scientific version)'''

    simple = format_simple(fetched_data, location) # used as a base
    data = extract_data(fetched_data, is_scientific=True)

    ''' 
    Gathering additional data from the API response for the scientific version.
    Explanation: this approach (storing the values in new variables) might seem redundant, but it's not.
    It's done to make the code more readable and easier to maintain.
    '''

    temp_min = data['temp_min'] 
    temp_max = data['temp_max']
    pressure = data['pressure']
    humidity = data['humidity']
    wind_speed = data['wind_speed']
    wind_deg = data['wind_deg']
    clouds = data['clouds']
    timezone = data['timezone']

    # return the formatted output (scientific version)
    return f"{simple}{nl}" \
           f"\t\t\t{Colors.GRAY}...{Colors.RESET}{nl}" \
           f"\t{Colors.ORANGE}min: {temp_min}°C\t\tmax: {temp_max}°C{Colors.RESET}{nl}" \
           f"\t{Colors.YELLOW}pressure: {pressure} hPa\thumidity: {humidity}%{Colors.RESET}{nl}" \
           f"\t{Colors.BLUE}wind speed: {wind_speed} m/s\twind deg: {wind_deg}°{Colors.RESET}{nl}" \
           f"\t{Colors.VIOLET}clouds: {clouds}%\t\ttimezone: {timezone}s{Colors.RESET}"
