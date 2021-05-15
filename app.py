import tweepy
from kucoin.client import Client
from keys import *
from functions import *

# twitter api auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

# init kucoin client
client = Client(kucoin_api_key, kucoin_api_secret, kucoin_api_passphrase)

# init twitter api
api = tweepy.API(auth, wait_on_rate_limit=True)

# choose terms to watch
terms = ['doge', 'dogecoin']

# create twitter stream lister
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # check tweet for terms
        term_used = find_terms(terms, status.text)
        # place a market order if term in tweet
        if term_used == True:
            order = client.create_market_order('DOGE-BTC', Client.SIDE_BUY, size=100)
            print('Elon tweeted about Doge! Bought 5.')
        print('Tweeted!')

# define streaming function
def streamtweets():
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(follow=['1122227682219937792'])

# run streaming function
streamtweets()
