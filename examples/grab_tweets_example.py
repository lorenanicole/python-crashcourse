
# /usr/bin/python

import requests
from requests_oauthlib import OAuth1
# import base64
# import pylab
import nltk
# import codecs

# reader = codecs.getreader("utf-8")

twitter_api = "https://api.twitter.com/1.1/"

CONSUMER_KEY = "FILL ME IN"
CONSUMER_SEC = "FILL ME IN"
oauth_token = "FILL ME IN"
oauth_secret = "FILL ME IN"

def get_twitter_client(oauth_token, oauth_secret):
	"""
	param: oauth_secret - oauth secret from twitter
	param: oauth_token - oauth_token from twitter
	return: an instance of OAuth
	"""
	return OAuth1(CONSUMER_KEY,
                      CONSUMER_SEC,
                      oauth_token,
                      oauth_secret)

def get_timeline(twitter_client):
	"""
	Retrieves an authenticated twitter user's home timeline.
	param: twitter_client - Twitter Oauth credentials
	return: dict of twitter user's home timeline
	"""
	response = requests.get(twitter_api + "statuses/home_timeline.json", auth=twitter_client)
	return response.json()

def post_tweet(twitter_client, tweet):
	"""
	Posts a tweet to an authenticated twitter user's account.
	param: twitter_client - Twitter Oauth credentials
	param: tweet - String of twitter text
	return: The Twitter API response as well as the http status code
	"""
	response = requests.post(twitter_api + "statuses/update.json", data={"status": tweet}, auth=twitter_client)
	return response.json(), response.status_code

if __name__ == "__main__":

	twitter_client = get_twitter_client(oauth_token, oauth_secret)

	timeline = get_timeline(twitter_client)

	for tweet in timeline:
		print("\n")
		screen_name = tweet.get("user").get("screen_name")
		print(screen_name, " says: ", tweet.get("text"))
		# tweet_text = tweet.get("text").replace (" ", "+")
		print("================================================")


	words = {}

	for tweet in timeline:
		text = tweet.get("text").replace(",","").replace(":","").replace(".","").split(" ")
		for word in text:  # idea: use nltk to filter out stop words
			if words.get(word, 0):
				words[word] += 1
			else:
				words[word] = 1  # histogram of words seen

