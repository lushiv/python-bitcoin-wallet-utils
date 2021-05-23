import requests
import json

def get_btc_market_data(currency_id):
    try:
        url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=%s&ids=bitcoin&order=market_cap_desc&per_page=100&page=1&sparkline=false'%currency_id
        response = requests.get(url)
        if response.status_code == 200:
            data = response.content.decode('UTF-8')

            market_data = json.loads(data)[0]
            
            return market_data
        else:
            return({'msg' : "Something wrong"})

    except Exception as e:
        print(e.message)


get_btc_market_data(currency_id='usd')