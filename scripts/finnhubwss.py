import websocket
import holidays
import pytz
import datetime
import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
tickerSymbol = config['GENERAL']['Symbol']
tz = pytz.timezone(config['GENERAL']['timeZone'])
marketTZ = pytz.timezone(config['GENERAL']['MarketTZ'])

us_holidays = holidays.US()

if(config['GENERAL']['Sandbox']):
    apiKey = config['FINNHUB']['sandbox_apiKey']
    print("###SANDBOX###")
    print("Sandbox API Key: " + apiKey)
else:
    apiKey = config['FINNHUB']['apiKey']
    #print("Not Sandbox")

def printTZ():
        print("Current Local Time:") 
        print(datetime.datetime.now(tz))
        print("Current NY Time:") 
        print(datetime.datetime.now(marketTZ))

def marketCheck(now = None):
        if not now:
            now = datetime.datetime.now(marketTZ)
        openTime = datetime.time(hour = 9, minute = 30, second = 0)
        closeTime = datetime.time(hour = 16, minute = 0, second = 0)

        # Holidays
        if now.strftime('%Y-%m-%d') in us_holidays:
            print("US Holiday, market is closed")
            return False
        # If before 0930 or after 1600
        if (now.time() < openTime) or (now.time() > closeTime):
            print("Before/After market hours, market is closed")
            return False
        # Weekends
        if now.date().weekday() > 4:
            print("Weekend, market is closed")
            return False
        return True  

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### stopped ###")

def on_open(ws):
    #ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"' + tickerSymbol + '"}')
#    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
#    ws.send('{"type":"subscribe","symbol":"IC MARKETS:1"}')

def getNews():
    r = requests.get('https://finnhub.io/api/v1/company-news?symbol=' + tickerSymbol + '&from=2021-03-01&to=2021-03-09&token=c15ug3748v6ootkk5en0')
    print(r.json())


def gogogo():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token="+apiKey,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    printTZ()
    if marketCheck() == True:
        print("Market is open")
        gogogo()
    else:
        print("Market is closed. most recent data:")
        r = requests.get('https://finnhub.io/api/v1/quote?symbol=' + tickerSymbol + '&token=' + apiKey)
        print(r.json())
        with open('data.json', 'w') as outfile:
            json.dump(r.json(), outfile)
