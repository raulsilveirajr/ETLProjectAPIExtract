import requests

# url = "https://api.coinbase.com/v2/prices/spot"
url = "https://api.coinbase.com/v2/exchange-rates"

params = {"currency": "BTC"}
headers = {"Accept": "application/json", "User-Agent": "MinhaAplicacao/1.0"}
response = requests.get(url, headers=headers, params=params)
print(response, "\n\n")
print(response.text, "\n\n")
print(response.headers, "\n\n")
print(response.json(), "\n\n")

rates = response.json()["data"]["rates"]

print(f"Preço do bitcoin em USD: {float(rates['USD']):,.2f} \n\n")
print(f"Preço do bitcoin em BRL: {float(rates['BRL']):,.2f} \n\n")

print(response.status_code)
print(response.status_code == requests.codes.ok)
