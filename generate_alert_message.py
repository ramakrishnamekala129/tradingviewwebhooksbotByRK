from auth import get_token
import requests
"""
This function will take a lot of the tedious work out of generating alert messages!
Simply follow the onscreen input prompts, at the end a string with everything you need
will be output, allowing you to copy and paste into tradingview!
"""


def generate_alert_message():
    print('Enter type: (limit, market, etc.)')
    type = input()
    print('Enter Side (buy or sell):')
    side = input()
    print('Enter Amount:')
    amount = input()
    print('Enter Symbol:')
    symbol = input()
    print("Auto or Manual By True or False")
    auto=input()
    if type == 'limit':
        print('Enter limit price:')
        price = input()
    else:
        price = 'None'
    key = get_token()

    print("Copy:\n")
    output = {"type": type, "side": side, "auto":auto,"amount": amount, "symbol": symbol, "price": price, "key": key}
    print(str(output).replace('\'', '\"'))



def alert_message(data):
    type=data['type']
    side=data['side']
    amount =  data['amount']
    symbol=data['symbol']
    if data['type']=='limit':
        if data['price']!=None:
            price=data['price']
    else:
        price=None
    key=get_token()
    auto = data['auto']
    print("Copy:\n")
    output = {"type": type, "side": side,"auto":bool(auto) ,"amount": int(amount), "symbol": symbol, "price": price, "key": key}
    print(str(output).replace('\'', '\"'))
    int(output['amount'])
    return output
    

