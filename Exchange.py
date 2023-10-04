if __name__ == '__main__':
    crossRateTable = {
        "CAD": {"CAD": 1}
    }

    inHandCurrency = input("please enter the currency in hand (from): ")

    requiredCurrency = input("please enter the currency required (to): ")

    totalAmount = float(input("please enter amount (current currency value): "))

    exchangeRate = crossRateTable[inHandCurrency][requiredCurrency]

    exchangeAmount = totalAmount * exchangeRate
    print("Total exchange amount: " + str(exchangeAmount))
