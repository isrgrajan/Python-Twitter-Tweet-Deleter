import os
import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET

def delete_tweets(tweet_ids):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    counter = 0
    for tweet_id in tweet_ids:
        try:
            api.get_status(tweet_id)
            api.destroy_status(tweet_id)
            counter += 1
            print(f"Deleted tweet with ID {tweet_id}")
            if counter % 100 == 0:
                os.system('cls' if os.name=='nt' else 'clear')
        except tweepy.NotFound as e:
            print(f"Failed to delete tweet with ID {tweet_id}: {e}")
        except Exception as e:
            print(f"An error occurred while deleting tweet with ID {tweet_id}: {e}")
