import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#f = open('helloworld.txt','w')

# Consumer keys and access tokens, used for OAuth
access_token = "3348771613-QAi7lNsh1wdZzaBqVftpzGgyzl62sFF9KLBTiCH"
access_token_secret = "5cIUgORFfTwDOSZWWDcWr4o3BOjO5uOOPviK9xsL3cOHF"
consumer_key = "UhuLKGNFGBSoQRD8ad3wu0Unz"
consumer_secret = "Dy501fQbzuhGsr4JGTAMOzZgjAHRFfqwM5FGLXO66CCrfi71GK"


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump').items():
    print(status._json['text'])

#f.close()
