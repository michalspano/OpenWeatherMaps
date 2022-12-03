# -*- coding: utf-8 -*-
# author: @michalspano
# utils.utils.py
# Contains custom functions, classes

from requests import get
from time import strftime
from utils.color import Colors
from os import linesep as nl # handle different systems
from typing import Final # additional mypy type checking

ENV_VAR: Final[str] = 'API_KEY'


def extract_data(data: dict, is_scientific: bool = False) -> dict:
    '''Extract data from the response'''

    get_icon = lambda d: d['weather'][0]['icon']

    if not is_scientific:
        return {
            'lon': data['coord']['lon'],
            'lat': data['coord']['lat'],
            'description': data['weather'][0]['description'],
            'temp': data['main']['temp'],
            'icon': get_icon(data)
        }
    return {
        "temp_min": data['main']['temp_min'],
        "temp_max": data['main']['temp_max'],
        "pressure": data['main']['pressure'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed'],
        "wind_deg": data['wind']['deg'],
        "clouds": data['clouds']['all'],
        "timezone": data['timezone'],
        "icon": get_icon(data)
    }


def location_to_coordinates(location: str, API: str) -> tuple:

    '''
    Convert location to geographical coordinates:
    - using the API, obtain the coordinates of the given location.
    '''

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={API}"

    response = get(url)
    data = response.json()

    # detect invalid location
    if not data:
        throw_error(f'`{location}` not found')

    return data[0]['lat'], data[0]['lon']


def throw_error(message: str) -> None:
    '''Throw an error message and exit'''
    print(f'{Colors.RED}ERROR: {message}{Colors.RESET}')
    exit(1)


def write_markdown_table(path: str, data: dict, location: str) -> None:
    '''Write the data to a markdown table'''

    icon_url = f"http://openweathermap.org/img/w/{data['icon']}.png"

    # write the heading and the icon
    with open(path, 'w') as f:
        f.write(f'## {location} - {get_current_time()}{nl}{nl}')
        f.write(f'![weather icon]({icon_url}){nl}{nl}')

    # write the table (skip the icon)
    # docs: https://www.markdownguide.org/extended-syntax/
    with open(path, 'a') as f:
        f.write(f'| attribute | value |{nl}')
        f.write(f'| :---: | :---: |{nl}')
        for key, value in data.items():
            if key != 'icon':
                f.write(f"| {key} | {value} |{nl}")


def get_current_time() -> str:
    '''Get current time'''

    return strftime("%Y/%m/%d %H:%M:%S")

