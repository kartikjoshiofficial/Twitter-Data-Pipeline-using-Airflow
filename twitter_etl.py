import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key="6YC6jjM0hd33eoFJuGRYxFoRk"
access_secret="croMFUr5SpG3IQwXqq0uMyzDxXwOImk54IKAps3VFrfMdQc5FC"
consumer_key="1612316174519537665-gOrCCgqWvYD5L9khPnn3cVGlVGqMKp"
consumer_secret="wAvFwzIngQARbUumg5rNlzloVpAQ16cHcivkBN1HQouNt"


#twitter authentication      https://docs.tweepy.org/en/stable/authentication.html
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

#Creating an API object
api = tweepy.API(auth)


usernm = "@" + input("Enter Twitter Username: ")

tweets = api.user_timeline(screen_name= usernm,
                           #200 is the maximum count of tweets
                           count = 200,
                           include_rts = False,
                           #rts means retweets
                           #necessary to keep it as false otherwise only the first 140 words can be considered
                           tweet_mode = 'extended'
                          )
print(tweets)

tweet_list = []
for tweet in tweets:
    text = tweet._json["full_text"]
    
    refined_tweet = {"user": tweet.user.screen_name,
                     'text' : text,
                     'favorite_count' : tweet.favorite_count,
                     'retweet_count' : tweet.retweet_count,
                     'created_at' : tweet.created_at}
    
    tweet_list.append(refined_tweet)
    
df =  pd.DataFrame(tweet_list)
df.to_csv("D:/Data Engineer Projects/twitter_etl/twitter_data.csv")