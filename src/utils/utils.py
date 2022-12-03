# -*- coding: utf-8 -*-
# author: @michalspano
# utils.utils.py
# Contains custom functions, classes

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


def throw_error(message: str) -> None:
    '''Throw an error'''
    print(f'{Colors.RED}ERROR: {message}{Colors.RESET}')
    exit(1)