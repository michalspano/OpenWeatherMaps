#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: @michalspano

import argparse
from sys import argv
from os import environ, system
from dotenv import load_dotenv

# contents of the utils package
from utils.utils import *
from utils.formatting import *

def main() -> None:
    '''Main function'''

    # define the command line arguments using the argparse module
    parser = argparse.ArgumentParser(description='OpenWeatherAPI CLI')
    parser.add_argument('-l', '--location', type=str, metavar='', required=True, help='the location to get the weather data for')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--simple', action='store_true', help='display the data in a simple way (default)')
    group.add_argument('-sc', '--scientific', action='store_true', help='display the data in a scientific way')
    parser.add_argument('-o', '--output', type=str, metavar='', help='write to a markdown file')
    args = parser.parse_args()

    # the API_KEY is needed, load it from the .env file (in case it not part of the environment variables)
    if ENV_VAR not in environ:
        load_dotenv()

    # obtain the API key, handle the case when it is not available in the environment variables or .env file
    try:
        API_KEY = environ[ENV_VAR]
    except KeyError:
        throw_error('`{ENV_VAR}` not found in `.env`!')

    # get the location, the obtained coordinates 
    location: str = args.location
    coords = location_to_coordinates(location, API_KEY)
    lat, lon = coords[0], coords[1]

    # TODO: support different units (currently only metric; later: imperial, standard)
    # format the URL 
    url: str = format_api_url(lat, lon, API_KEY, 'metric')

    # make the request, parse data to json
    try:
        response = get(url)
    except Exception as exception:
        throw_error(f'Error: {exception}')
    data = response.json()

    is_scientific: bool = False # default mode

    # display the data in the respective mode
    if args.simple:
        print(format_simple(data, location))
    elif args.scientific:
        is_scientific = True
        print(format_scientific(data, location))
    else:
        print(format_simple(data, location))

    # optionally write the data to a markdown file
    if args.output:
        extracted_data = extract_data(data) if not is_scientific else extract_data(data, is_scientific=True)

        if not args.output.endswith('.md'): # ensure the file extension is .md
            throw_error('`output` file extension must be `.md`!')
        write_markdown_table(args.output, extracted_data, location)


if __name__ == '__main__':
    main()
