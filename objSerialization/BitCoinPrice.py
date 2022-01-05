#!/bin/python3

'''
Communicate with coindesk application to get bitcoin prices
https://api.coindesk.com/v1/bpi/currentprice.json
'''
import requests
import json

respo = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
binfo=respo.json()


print('Bitcoin Price as on',binfo['time']['updated'])
print('1 BitCoin = $',binfo['bpi']['USD']['rate'])
