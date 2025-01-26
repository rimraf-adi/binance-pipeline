from config import API_KEY,SECRET
from binance import Client

client = Client(API_KEY,SECRET)
depth = client.get_order_book(symbol = 'BTCUSDT')


print(depth)