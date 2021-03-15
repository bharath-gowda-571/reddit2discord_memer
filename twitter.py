#!/usr/bin/python3
import tweepy

auth=tweepy.OAuthHandler("********","***********")
auth.set_access_token("************","**************")
api=tweepy.API(auth)

def tweet_image(filename,message):
    # filename = 'sample.jpeg'
    api.update_with_media(filename, status=message)
    print("meme tweeted")
# tweet_image("sample.jpeg")
