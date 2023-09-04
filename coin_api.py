import requests
import os

key = os.environ['API_KEY']
headers = {'X-CMC_PRO_API_KEY': key, 'Accepts': 'application/json'}

params = {'start': '1', 'limit': '4', 'convert': 'INR'}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params, headers=headers).json()

coins = json['data']

for c in coins:
  print(c['symbol'], int(c['quote']['INR']['price']))
