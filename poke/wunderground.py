import json
from urllib.request import urlopen


def auth():
    with open("etc/auth/wunderground.txt") as f:
        api_key = f.readline().strip()
    return api_key


def get_location():
    with open("etc/location") as f:
        location = f.readline().strip()
    return location


def build_url(args):
    """

    :param args: dictionary of arguments
    :return:
    """
    endpoint = 'http://api.wunderground.com/api'
    features = args.get('features') # should be in list form
    feature_str = '/'.join(features)
    query = 'q/'
    if args.get('query'):
        query += args.get('query')
    else:
        query += get_location()
    parts = [endpoint, feature_str, query]
    url_string = '/'.join(parts) + '.json'
    return url_string


def place_call(args):
    """
    :param args: a dictionary of arguments
    :return:
    """
    url_string = build_url(args)
    with urlopen(url_string) as u:
        json_string = u.read()
    parsed_json = json.loads(json_string)
    return parsed_json
