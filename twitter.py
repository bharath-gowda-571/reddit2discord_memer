#!/usr/bin/python3
import tweepy

auth=tweepy.OAuthHandler("tFeGrVNDfR4CAPLEEx2Tt52l2","AiCxk3I2NoGK4SgAzqK57VSQIQpwQXSUBiWToSDQacvKJRVxFQ")
auth.set_access_token("816185268390793216-1jqnlBk4kam4rtHBQKYMdqzdbEdJg50","b7M7rpNCzoVtapkAZQz8jwzzMcvYyULQOSWSsuFwzapne")
api=tweepy.API(auth)

def tweet_image(filename):
    # filename = 'sample.jpeg'
    api.update_with_media(filename)#, status=message)
    print("meme tweeted")
# tweet_image("sample.jpeg")