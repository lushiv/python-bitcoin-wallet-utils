import requests

def get_current_btc_price(currency_id):
    try:
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=%s'%currency_id
        response = requests.get(url)
        if response.status_code == 200:
            data = response.content.decode('UTF-8')

            print(data)

            return data
        else:
            return({'msg' : "Something wrong"})

    except Exception as e:
        print(e.message)