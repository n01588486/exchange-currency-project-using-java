if __name__ == '__main__':
    inHandCurrency = input("please enter the currency in hand: ")

    requiredCurrency = input("please enter the currency required: ")

    totalAmount = float(input("please enter amount: "))

    exchangeRate = float(input("please enter exchange rate:"))

    exchangeAmount = totalAmount * exchangeRate
    print("Total exchange amount: " + str(exchangeAmount))
