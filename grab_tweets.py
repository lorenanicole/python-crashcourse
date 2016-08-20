import requests
from requests_oauthlib import OAuth1
import json
from pprint import pprint
import base64
import pylab
import nltk

twitter_api = "https://api.twitter.com/1.1/"

CONSUMER_KEY = "FILL ME IN"
CONSUMER_SEC = "FILL ME IN"
oauth_token = "FILL ME IN"
oauth_secret = "FILL ME IN"

def get_twitter_client(oauth_token, oauth_secret):
	"""
	param: oauth_secret - oauth secret from twitter
	param: oauth_secret - oauth_token from twitter
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
	return json.loads(response.content)

def post_tweet(twitter_client, tweet):
	"""
	Posts a tweet to an authenticated twitter user's account.
	param: twitter_client - Twitter Oauth credentials
	param: tweet - String of twitter text
	return: The Twitter API response as well as the http status code
	"""
	response = requests.post(twitter_api + "statuses/update.json", data={"status": tweet}, auth=twitter_client)
	return json.loads(response.content), response.status_code

def cowsay(text):
	"""
	Cow ASCII art. I mean. Win win :-).
	"""
	headers = {'X-Mashape-Key' : 'DSIsxD7caXmshIShinSXM2rDBkkrp1sowCpjsnJnouVH8ptZDZ'}
	response = requests.get("https://ascii.p.mashape.com/cowsay?style=default&text=" + text.encode("UTF-8"), headers=headers)
	return base64.b64decode(json.loads(response.content).get("contents").get("cowsay"))

def ascii_image(text):
	"""
	ASCII art. YAY =^.^=!!
	"""
	headers = {'X-Mashape-Key' : 'DSIsxD7caXmshIShinSXM2rDBkkrp1sowCpjsnJnouVH8ptZDZ'}
	response = requests.post("https://ascii.p.mashape.com/image2ascii", data = {"format":"color"}, headers=headers)
	return base64.b64decode(json.loads(response.content).get("contents").get("cowsay"))


if __name__ == "__main__":

	twitter_client = get_twitter_client(oauth_token, oauth_secret)

	# print cowsay("Give me something to tweet ")
	# tweet = raw_input(" ")
	# response, response_code = post_tweet(twitter_client, tweet)

	# if response == 200:



	timeline = get_timeline(twitter_client)

	# for tweet in get_timeline(twitter_client):
	# 	print "\n"
	# 	screen_name = tweet.get("user").get("screen_name")
	# 	print screen_name + "says:"
	# 	tweet_text = tweet.get("text").replace (" ", "+")
	# 	print base64.b64decode(json.loads(requests.get("https://ascii.p.mashape.com/cowsay?style=default&text=" + tweet_text.encode("UTF-8"), headers=headers).content)["contents"]["cowsay"])
	# 	print "\n"
	# 	print "================================================"


	words = {}

	for tweet in timeline:
		# if "the" in tweet.get("text"):
		# 	pprint(tweet)
		# print twitter.keys()
		text = tweet.get("text").replace(",","").replace(":","").replace(".","").split(" ")
		for word in text:
			if words.get(word, 0):
				words[word] += 1
			else:
				words[word] = 1

	words = {word.lower(): count for word, count in words.iteritems() if word and word not in nltk.corpus.stopwords.words('english')}

	pylab.pie(words.values()[:10], labels=words.keys()[:10], shadow=True)

	pylab.show()