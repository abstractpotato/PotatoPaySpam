import requests, json, time

host = "https://pay.test.api.starch.one"

def get_tx(hash):
    return json.loads(requests.get(f'{host}/txs/internal/{hash}').text)

def spam_tx(tx):
    return json.loads(requests.post(f'{host}/mempool/replicate', json=tx).text)

hash = input("enter tx hash: ")
tx = get_tx(hash)
print(tx)
while True:
    print(spam_tx(tx))
    time.sleep(.5)
