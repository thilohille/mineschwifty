#!/usr/bin/python
from __future__ import print_function
import yaml
import requests

f = open('mineschwifty.yml')
config = yaml.safe_load(f)

# state file. contains the key of the curren coin
try:
    s = open(config['statefilename'],'rw+')
    state = s.readline()
except IOError:
    s = open(config['statefilename'],'w+')
    state=''

sortbuffer_val = 0
sortbuffer_key = ''

def control_miner(coin, command):
    print(config['coins'][coin][command])
    #exec(config['coins'][coin][command]);


def get_profit_index(key, coin):
    """sort the coin by profit"""
    global sortbuffer_key, sortbuffer_val
    # hack-adi-hack, das dollarsign muss weg :-)
    profit_val = float(coin['profit'][1:])
    if profit_val > sortbuffer_val:
        sortbuffer_key = key
        sortbuffer_val = profit_val
    return sortbuffer_key, sortbuffer_val


for i in (config['coins']):
    params = dict(
        hr=config['coins'][i]['hashrate'],
        p=config['coins'][i]['powerwall'],
        cost=config['powercost']
    )
    resp = requests.get(url=config.get('url')+str(config['coins'][i]['index'])+'.json', params=params)
    get_profit_index(i, resp.json())


if sortbuffer_key != state:
    print(sortbuffer_key, sortbuffer_val)
    #if we know the current miner, we stop it
    if state in config['coins']:
        control_miner(state,'command_stop')
        #exec(config['coins'][state]['command_stop'])
    else:
        #try to stop all possible miners..
        for c in config['coins']:
            control_miner(c,'command_stop')
            #exec(config['coins'][state]['command_stop'])
    #then we start the new miner
    control_miner(sortbuffer_key,'command_start')
    state = sortbuffer_key
    s.write(state)
f.close()

