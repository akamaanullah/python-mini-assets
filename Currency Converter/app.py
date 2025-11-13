import requests

def convert_currency(amount, from_currency, to_currency):
    # Fetch the latest exchange rates from the API
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Error: Unable to fetch data from the API."

    data = response.json()

    # Check if the currency exists in the API response
    if to_currency not in data['rates']:
        return f"Error: Unable to find exchange rate for {to_currency}."

    # Get the conversion rate
    conversion_rate = data['rates'][to_currency]
    return amount * conversion_rate

# Taking user inputs for amount and currency
amount = float(input("Enter the amount you want to convert: "))
from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()

# Convert the currency and print the result
result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}.")
