import sys
import requests
import json

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
try:
    bitnum = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

response = requests.get(
    "https://api.coindesk.com/v1/bpi/currentprice.json"
)

o = response.json()
rate = o["bpi"]["USD"]["rate"]
price = rate.replace(",", "")

amount = float(price) * bitnum
print(f"${amount:,.4f}")
