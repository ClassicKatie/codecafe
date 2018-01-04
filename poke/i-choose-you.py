#!user/bin/env python
import random

from wunderground import place_call
from pokemon import stats
import get_auth

import pdb

def get_weather_forecast():
    """
    Get weather forecast for the next 10 days
    :return:
    """
    args = {
        'features': ['forecast10day', 'astronomy', 'tide', 'alerts']
    }
    result = place_call(args)
    return result

def get_weather_conditions():
    """
    Get current conditions
    :return:
    """
    args ={
        'features': ['conditions', 'astronomy', 'tide', 'alerts']
    }
    result = place_call(args)
    pdb.set_trace()
    return result.get('current_observation')

def current_pokemon():
    pokemon = []
    with open ('poke/current.txt') as f:
        pokemon.append(f.readline().strip())
        pokemon.append(f.readline().strip())
        pokemon.append(f.readline().strip())
        pokemon.append(f.readline().strip())
        pokemon.append(f.readline().strip())
        pokemon.append(f.readline().strip())
    return pokemon

def select_pokemon():
    """
    Get current weather information
    :return:
    """
    current_list = current_pokemon()
    poke_stats = stats()
    weather_info = get_weather_conditions()
    if (weather_info.get('weather') == 'Rainy'):
        for pokemon in current_list:
            # Is there a water type pokemon?
            print(pokemon)
        print("Rain!")
    elif (weather_info.get('weather') == 'Sunny'):
        print("Sunny!") # return a grass pokemon

    return random.choice(pokemon)

def i_choose_you(monster):
    message = "I choose you, " + monster
    api = get_auth.connect()
    api.update_status(message)
    api.update_profile(description=monster)
    return

def what_is_current():
    api = get_auth.connect()
    user = api.me()
    return user.get('description')

def main():
    """
    This function runs our twitter bot script.
    This is what our cron job will call on the interval

    :return: None
    """
    #current = what_is_current() # What is the current pokemon?
    new = select_pokemon() # What is the new pokemon
    '''
    if (current != new):
        i_choose_you(new) 
    '''

    i_choose_you(new)
    return


if __name__ == '__main__': # boilerplate for running the script
    exit(main())