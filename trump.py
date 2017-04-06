#!/usr/bin/env python
#
########################################################################
#								        #
# python script to print trumps latest tweet                           #
#								        #
# Nick Abbott | April 5, 2017 | Just because I'm bored                 #
#								                                                       #
########################################################################

import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

tweet = api.user_timeline(screen_name = "realDonaldTrump", count = 1)[0]

print tweet.text
