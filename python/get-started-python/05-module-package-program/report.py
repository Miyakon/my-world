#!/usr/bin/env python3

def get_description():
    """ Return random weather like pro """
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)