import cbpro
import time

data = open('passphrase', 'r').read().splitlines()

key = data[0]
passphrase = data[1]
b64secret = data[2]

auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)

print(auth_client.buy(price="10.0", size="2.1", order_type="limit", product_id="ETH-GBP"))
print(auth_client.buy(size="10", order_type="market", product_id="ETH-GBP"))
print(auth_client.sell(price="2000000.00", size="10", order_type="limit", product_id="BTC-GBP"))
print(auth_client.sell(size="10", order_type="market", product_id="BTC-GBP"))
print(auth_client.place_limit_order(product_id="BTC-GBP", side="buy", price="10.00", size="2"))
print(auth_client.cancel_all(product_id="BTC-GBP"))
print(auth_client.get_orders())

sell_price = 80000
sell_amount = 0.3
buy_price = 25000
buy_amount = 0.2

while True:
    price = float(auth_client.get_product_ticker(product_id="BTC-GBP")['price'])
    if(price <= buy_price):
        print("Buying Bitcoin")
        auth_client.buy(size=buy_amount, order_type="market", product_id="BTC-GBP")
    elif price >= sell_price:
        print("Selling Bitcoin")
        auth_client.sell(size=sell_amount, order_type="market", product_id="BTC-GBP")
    else:
        print(f"Nothing going down... {price:,}!")
    time.sleep(10)