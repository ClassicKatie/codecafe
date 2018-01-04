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


def main():
    """
    This function runs our twitter bot script.
    This is what our cron job will call on the interval

    :return: None
    """
    print("Debug!")
    write("debug")
    return


if __name__ == '__main__': # boilerplate for running the script
    exit(main())