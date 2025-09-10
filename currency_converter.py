import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_URL = "https://api.freecurrencyapi.com/v1/"
API_KEY = os.getenv("CURRENCY_API_KEY")

if not API_KEY:
    raise RuntimeError("API key not found. Please set CURRENCY_API_KEY in your .env file.")


def get_currencies():
    url = f"{BASE_URL}currencies?apikey={API_KEY}"
    try:
        data = requests.get(url, timeout=8).json()
    except requests.RequestException as e:
        print("Error fetching currencies:", e)
        return {}

    if "data" not in data:
        print("Error fetching currencies:", data)
        return {}

    return data["data"]


def print_currencies(currencies):
    for code, info in currencies.items():
        name = info.get("name", "")
        symbol = info.get("symbol", "")
        print(f"{code} - {name} - {symbol}")


def exchange_rate(currency1, currency2):
    url = f"{BASE_URL}latest?apikey={API_KEY}&base_currency={currency1}&currencies={currency2}"
    try:
        data = requests.get(url, timeout=8).json()
    except requests.RequestException as e:
        print("Error fetching exchange rate:", e)
        return None

    if "data" not in data or currency2 not in data["data"]:
        print("Invalid currencies.")
        return None

    rate = data["data"][currency2]
    print(f"{currency1} -> {currency2} = {rate}")
    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} = {converted_amount} {currency2}")
    return converted_amount


def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")


if __name__ == "__main__":
    main()
