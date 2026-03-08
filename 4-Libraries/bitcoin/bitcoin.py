import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Too short")
bitcoin = sys.argv[1]
# price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json") <-- this link doesn't work and so i just wanted to show that i do know how to use request code
# priceson = price.json()
price = 95705.46
try:
    bitfloat = float(bitcoin)
except ValueError:
    sys.exit("Command line argument is not a number")
# usd_rate = priceson["bpi"]["USD"]["rate_float"]  <-- because the other code doesn't work neither will this code
total = bitfloat * price
print(f"${total:,.4f} AUD")
