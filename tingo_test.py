from websocket import create_connection
import simplejson as json
import time
ws = create_connection("wss://api.tiingo.com/fx")

subscribe = {
        'eventName':'subscribe',
        'authorization':'11fecb0b1707bb991e11c6dffbaadd61a025e04c',
        'eventData': {
            'thresholdLevel': 2
    }
}

ws.send(json.dumps(subscribe))
while True:
    print(ws.recv())
    time.sleep(1)