# mineschwifty

mineschwifty is designed to switch crypto-currency miningsoftware based on the profit calculated bei whattomine.com.
This is NOT completed and NOT tested yet.
If you choose to use it, you use it at your own risk!

Currently targeted are:
-zcash
-eth
-etc

But basically all coins supported by whattomine.com SHOULD work...


To get it working you need to setup the mineschwifty.yml:
Global:
-url
baseurl for the requests

-powercost
cost per kw/h in US$

Per coin:
-command_activate
should be set for each coin to the command necessary to shutdown the current miner (which could be any of the
supported) and and start the miner for that coin.

-powerwall
set it to your powerconsumption in w

-hashrate
set it to the hashrate according to whattomine.com
NOTE: the unit changes between coins. (ETH: mh/s, ZEC: h/s)

again: Use it at your own risk!
