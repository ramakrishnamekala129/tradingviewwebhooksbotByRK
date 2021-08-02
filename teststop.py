import ccxt  # noqa: E402


exchange = ccxt.bitmex({
    'apiKey': 'weq2Y8FevavmNVHN_RO1_JvL',
    'secret': 'Ky3eXdkdWwyE7vKnnzpFUsXxPIhlN7Zokt4Xqu7YainxLN_8',
    'enableRateLimit': True,
})

symbol = 'ETH/USD'  # bitcoin contract according to https://github.com/ccxt/ccxt/wiki/Manual#symbols-and-market-ids
type = 'Stop'  # or 'Market', or 'Stop' or 'StopLimit'
side = 'sell'  # or 'buy'
amount = 1.0
price = None  # or None

# extra params and overrides
params = {
    'stopPx': 1050.0,  # if needed
}

order = exchange.create_order(symbol, type, side, amount, price, params)
print(order)