#!user/bin/env python
import csv

def stats():
    with open('poke/stats.csv', 'U') as f:
        reader = csv.DictReader(f)
    return reader

def get_recent_tweets():
    return

def get_messages():

    return


def main():
    """
    This function runs our twitter bot script.
    This is what our cron job will call on the interval

    :return: None
    """

    return
