from datetime import datetime
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
terms = ['doge', 'dogecoin', 'Doge', 'Dogecoin', 'DOGE']

# create twitter stream listener
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # check tweet for terms
        term_used = find_terms(terms, status.text)
        # place a market order if term in tweet
        if term_used == True:
            order = client.create_market_order('DOGE-BTC', Client.SIDE_BUY, size=100)
            send_alert('fork-elon alert!', 'Elon tweeted about dogecoin at {0}! Bought 100.'.format(str(datetime.now())))
        else:
            send_alert('fork-elon alert!', 'Elon tweeted, but not about dogecoin at {0}.'.format(str(datetime.now())))

# define streaming function
def streamtweets():
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(follow=['44196397'])

# run streaming function
streamtweets()
