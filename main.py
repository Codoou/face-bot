from config import settings
import tweepy

SETTINGS = settings

auth = tweepy.OAuth1UserHandler(
   SETTINGS["consumer_key"], SETTINGS["consumer_secret"],
   SETTINGS["access_token"], SETTINGS["access_token_secret"]
)

api = tweepy.API(auth)

response = api.update_status(
    status="This is a test tweet from the botv2"
)

print(response)