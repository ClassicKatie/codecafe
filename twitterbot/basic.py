#!/user/bin/env python
import get_auth # import our helper file for accessing twitter

"""
What this file provides:

"""

def write(message):
    """

    :param message: string message to write
    :return:
    """
    api = get_auth.connect()
    api.update_status(status=message)
    return

def get_followers():
    api = get_auth.connect()
    me = api.me() # User object
    followers = api.followers(me.id)
    return followers

def get_statuses(user):
    api = get_auth.connect()
    statuses = api.user_timeline(user.id)
    return statuses

def say_roll_tide(this_status):
    # status is a status object
    api = get_auth.connect()
    message = "@" + this_status.user.screen_name + " ROLL TIDE"
    api.update_status(in_reply_to_status_id=this_status.id, status=message)
    return

def get_timeline():
    api = get_auth.connect()
    return api.home_timeline(count=100)

def main():
    """
    This function runs our twitter bot script.
    This is what our cron job will call on the interval

    :return: None
    """
    print("Debug!")
    followers = get_followers()
    """
    for follower in followers:
        statuses = get_statuses(follower)
        for status in statuses:
            says_bama = False
            if (status.text == "So how's your evening been?"):
                says_bama = True
            # Check for the word 'Bama' in status.text; set to true if so
            if (says_bama):
                say_roll_tide(status)
    #write("debug")
    """

    statuses = get_timeline()
    for status in statuses:
        says_bama=False
        if (status.text == "Bama"):
            says_bama = True
            # Check for the word 'Bama' in status.text; set to true if so
        if (says_bama):
            say_roll_tide(status)
    return


if __name__ == '__main__': # boilerplate for running the script
    exit(main())