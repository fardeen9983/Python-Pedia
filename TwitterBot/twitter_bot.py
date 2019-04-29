"""
This File contains all the code required to create a Twitter Bot
"""

# import python library for Twitter
import tweepy

# Assign the consumer keys and access tokens
CONSUMER_KEY = 'dqDKc3Jis3FnkxqFW5RcWc8Dn'
CONSUMER_SECRET = '51ZVBTZ6V7wbNTBJFcA9zVsCYK3MnhGObZnzS5DLYrnakQPuSn'
ACCESS_TOKEN = '927951233570168832-Ee0Wp2tew393e7CEu2W2BL5ptnfXlga'
ACCESS_SECRET = 'fkNu49qbtN5GBckpuPLnJ1tIZNCAIP9M0RuIYinGC0tPc'

# Set tweepy authentication and set access to gain the Tweepy API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
