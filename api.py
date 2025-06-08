import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "f0009cec-59a7-4611-b6b2-3d8180bfbf90"
}
response = requests.get(url, headers=headers)
print(response.status_code, response.json())

if response.status_code == 200:
    data = response.json()
    print(data)

    coins = data['data']
    for x in coins:
        print(x['symbol'], x['quote']['USD']['price'])


