import requests
import json

url = "https://data.binance.com/api/v3/ticker/24hr"  # url
request = requests.get(url)  # request data
data = json.loads(request.text)  # load data to json
print(data)  # print data
# find price of bitcoin
for i in data:
    if i["symbol"] == "BTCUSDT":
        print(i["lastPrice"])
