#!/usr/bin/python
import json, requests
import yaml

f = open('mineschwifty.yml')
# use safe_load instead load
config = yaml.safe_load(f)
f.close()

sortbuffer_val = 0;
sortbuffer_key = '';

def get_profit_index(key, coin):
   "sort the coin by profit"
   global sortbuffer_key,sortbuffer_val
   #hack-adi-hack, das dollarsign muss weg :-)
   profit_val= float(coin['profit'][1:])
   if ( profit_val > sortbuffer_val):
       sortbuffer_key = key
       sortbuffer_val = profit_val
   return (sortbuffer_key,sortbuffer_val)


for i in (config['coins']):
    params=dict(
        hr = config['coins'][i]['hashrate'],
        p = config['coins'][i]['powerwall'],
        cost = config['powercost']
    )
    resp = requests.get(url=config.get('url')+str(config['coins'][i]['index'])+'.json', params=params)
    data = json.loads(resp.text)
    get_profit_index(i,data)

print sortbuffer_key,sortbuffer_val

print config['coins'][sortbuffer_key]['command_activate']
#exec(config['coins'][sortbuffer_key]['command_activate'])