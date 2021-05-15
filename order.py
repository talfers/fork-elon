from kucoin.client import Client
from keys import *

# init kucoin client
client = Client(kucoin_api_key, kucoin_api_secret, kucoin_api_passphrase)

# check markets
# markets = client.get_markets()
# print(markets)

# make market order
order = client.create_market_order('DOGE-BTC', Client.SIDE_BUY, size=10)
# print(order)
