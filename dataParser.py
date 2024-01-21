import json
# Parse JSON data Exchange 1
with open("./datafiles/Exchange_1.json", "r") as file:
    json_data = file.read()

data1 = json.loads(json_data)

# Parse JSON data Exchange 2
with open("./datafiles/Exchange_2.json", "r") as file:
    json_data = file.read()

data2 = json.loads(json_data)

# Parse JSON data Exchange 3
with open("./datafiles/Exchange_3.json", "r") as file:
    json_data = file.read()

data3 = json.loads(json_data)

# # unique symbols
# unique_symbols = set(item['Symbol'] for item in data)

# unique_symbols_list = list(unique_symbols)

# print("Unique Symbols:", unique_symbols_list)

# unique types
unique_msg = set(item['MessageType'] for item in data3)

unique_msg_list = list(unique_msg)

print("Unique messages:", unique_msg_list)


def extract_latest_order_prices(filedata):
    latest_order_prices = {}

    # parse data
    for item in filedata:
        if item['MessageType'] == 'Trade':
            symbol = item['Symbol']
            order_price = item['OrderPrice']

            if symbol not in latest_order_prices or latest_order_prices[symbol]['TimeStamp'] < item['TimeStamp']:
                latest_order_prices[symbol] = {'OrderPrice': order_price, 'TimeStamp': item['TimeStamp']}

    # latest trade price
    symbols_latest_prices = {symbol: filedata['OrderPrice'] for symbol, filedata in latest_order_prices.items()}
    if len(symbols_latest_prices) == 0:
        symbols_latest_prices['None'] = 0.00

    return list(symbols_latest_prices.items())

Ex1_symbols_latest_prices_list = extract_latest_order_prices(data1)
Ex2_symbols_latest_prices_list = extract_latest_order_prices(data2)
Ex3_symbols_latest_prices_list = extract_latest_order_prices(data3)

