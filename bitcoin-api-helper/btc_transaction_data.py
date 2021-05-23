import requests
import json

def get_testnet_txn_data_from_wallet_address(address):
    try:
        url = 'https://api.blockcypher.com/v1/btc/test3/addrs/%s/full?limit=50'%address
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content.decode('UTF-8'))

            received_balance = int(data.get("total_received"))/100000000
            sent_balance = int(data.get("total_sent"))/100000000
            balance = int(data.get("balance"))/100000000
            unconfirmed_balance = int(data.get("unconfirmed_balance"))/100000000
            final_balance = int(data.get("final_balance"))/100000000

            return_data = {
                "wallet_address" : data.get("address", None),
                "total_sent_balance" : sent_balance, 
                "total_received": received_balance,
                "total_balance" : balance,
                "unconfirmed_balance" : unconfirmed_balance,
                "final_balance" : final_balance,
                "number_of_txn" : data.get("n_tx", None),
                "unconfirmed_n__of_txn" : data.get("unconfirmed_n_tx", None),
                "final_nuber_of_txn" : data.get("final_n_tx", None),
                "txn_list" : data.get("txs", None)  # TODO --> edits data from list
            }

            return return_data
        else:
            return({'msg' : "Something wrong"})

    except Exception as e:
        print(e.message)



def get_testnet_txn_data_from_block_number(block_number):
    try:
        url = 'https://api.blockcypher.com/v1/btc/main/blocks/%s'%block_number
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.content.decode('UTF-8'))

            return_data = {
                "hash" : data.get("hash", None),
                "height" : data.get("height", None), 
                "chain": data.get("chain", None),
                "total" : data.get("total", None),
                "fees" : data.get("fees", None),
                "size" : data.get("size", None),
                "vsize" : data.get("vsize", None),
                "ver" : data.get("ver", None),
                "time" : data.get("time", None),
                "received_time" : data.get("received_time", None),
                "coinbase_addr" : data.get("coinbase_addr", None),
                "relayed_by" : data.get("relayed_by", None),
                "bits" : data.get("bits", None),
                "nonce" : data.get("nonce", None),
                "n_tx" : data.get("n_tx", None),
                "prev_block" : data.get("prev_block", None),
                "mrkl_root" : data.get("mrkl_root", None),
                "txids_list" : data.get("txids"),             # TODO --> edits data from list
            }

            return return_data
        else:
            return({'msg' : "Something wrong"})

    except Exception as e:
        print(e)
