import requests
import os

key = os.environ['API_KEY']
headers = {'X-CMC_PRO_API_KEY': key, 'Accepts': 'application/json'}

params = {'start': '1', 'limit': '4', 'convert': 'INR'}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params, headers=headers).json()

coins = json['data']
# print(coins)

coin = {}

for c in coins:
  # print(c['symbol'], int(c['quote']['INR']['price']))
  # print(c)
  if (c['symbol'] == 'BTC'):
    coin['BTC'] = [
      c['symbol'], c['slug'],
      round(int(c['quote']['INR']['price']), 2),
      c['quote']['INR']['percent_change_24h']
    ]
  elif (c['symbol'] == 'ETH'):
    coin['ETH'] = [
      c['symbol'], c['slug'], c['quote']['INR']['price'],
      c['quote']['INR']['percent_change_24h']
    ]
  elif (c['symbol'] == 'USDT'):
    coin['USDT'] = [
      c['symbol'], c['slug'], c['quote']['INR']['price'],
      c['quote']['INR']['percent_change_24h']
    ]
  else:
    coin['BNB'] = [
      c['symbol'], c['slug'], c['quote']['INR']['price'],
      c['quote']['INR']['percent_change_24h']
    ]
