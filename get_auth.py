#!/usr/bin/python
from tweepy import OAuthHandler
import tweepy

def connect():
    with open("etc/auth/auth.txt", "r") as authFile:
        consumerKey = authFile.readline().strip()
        consumerSecret = authFile.readline().strip()
        accessKey = authFile.readline().strip()
        accessToken = authFile.readline().strip()
        twitter_auth = OAuthHandler(consumerKey, consumerSecret)
        twitter_auth.set_access_token(accessKey, accessToken)
        api = tweepy.API(twitter_auth)
    return api


def get_token():
    # Get authorization information from secure file
    with open("etc/auth/auth.txt", "r") as authFile:
        consumerKey = authFile.readline().strip()
        consumerSecret = authFile.readline().strip()

    # Authenticate the twitter consumer key
    twitter_auth = OAuthHandler(consumerKey, consumerSecret)
    twitter_auth.secure = True
    authUrl = twitter_auth.get_authorization_url()

    # go to this URL to authorize
    print("PLase visit this link and authorize the app ==> " + authUrl)
    print ("Eneter the Authorization PIN")

    # Write the access tokens to file
    pin = input().strip() # strip the new line character from pressing 'enter'
    token = twitter_auth.get_access_token(verifier=pin)
    with open("etc/auth/tokens.txt", "w") as accessTokenFile:
        accessTokenFile.write(token[0]+'\n') # '\n' indicates a newline char
        accessTokenFile.write(token[1]+'\n')
    return
