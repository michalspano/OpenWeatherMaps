# -*- coding: utf-8 -*-
# author: @michalspano
# utils.arg_parser.py
# Contains the arg_parser function

from argparse import ArgumentParser


def arg_parser_init():
    '''Define and initialize the argument parser'''

    parser = ArgumentParser(description='OpenWeatherAPI CLI')
    parser.add_argument('-l', '--location', type=str, metavar='', required=True, help='the location to get the weather data for')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--simple', action='store_true', help='display the data in a simple way (default)')
    group.add_argument('-sc', '--scientific', action='store_true', help='display the data in a scientific way')
    parser.add_argument('-o', '--output', type=str, metavar='', help='write to a markdown file')

    # parse the arguments
    return parser.parse_args()
