if __name__ == '__main__':
    crossRateTable = {
        "CAD": {"CAD": 1, "USD": 0.7625},
        "USD": {"CAD": 1.3118, "USD": 1},
        "EUR": {"CAD": 1.4983, "USD": 1.1417},
        "GBP": {"CAD": 1.6832, "USD": 1.2829},
        "JPY": {"CAD": 0.0117, "USD": 0.0089},
        "CNY": {"CAD": 0.1890, "USD": 0.1440},
        "CHF": {"CAD": 1.3160, "USD": 1.0029},
        "INR": {"CAD": 0.0179, "USD": 0.0137}
    }

    inHandCurrency = input("please enter the currency in hand (from): ")

    requiredCurrency = input("please enter the currency required (to): ")

    totalAmount = float(input("please enter amount (current currency value): "))

    exchangeRate = crossRateTable[inHandCurrency][requiredCurrency]

    exchangeAmount = totalAmount * exchangeRate
    print("Total exchange amount: " + str(exchangeAmount))
