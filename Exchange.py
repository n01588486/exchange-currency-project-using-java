def nToMoneyStr(n: float) -> str:
    if n != 0 and abs(n) < 0.01:
        return "0.01"
    strn = str(n*100)
    strn = strn.split(".")[0]
    if abs(n) < 1:
        if len(strn) == 1:
            return "0.0" + strn
        else:
            return "0." + strn
    else:
        return strn[:-2] + "." + strn[-2:]


if __name__ == '__main__':
    crossRateTable = {
        "CAD": {"CAD": 1, "USD": 0.7625, "EUR": 0.6681, "GBP": 0.5944,
                "JPY": 85.2902, "CNY": 5.2936, "CHF": 0.7604, "INR": 55.7528},
        "USD": {"CAD": 1.3118, "USD": 1, "EUR": 0.8761, "GBP": 0.7796,
                "JPY": 111.8642, "CNY": 6.9430, "CHF": 0.9971, "INR": 73.1157},
        "EUR": {"CAD": 1.4983, "USD": 1.1417, "EUR": 1, "GBP": 0.8900,
                "JPY": 127.7273, "CNY": 7.9270, "CHF": 1.1384, "INR": 83.4803},
        "GBP": {"CAD": 1.6832, "USD": 1.2829, "EUR": 1.1237, "GBP": 1,
                "JPY": 143.5219, "CNY": 8.9068, "CHF": 1.2792, "INR": 93.8001},
        "JPY": {"CAD": 0.0117, "USD": 0.0089, "EUR": 0.0078, "GBP": 0.0070,
                "JPY": 1, "CNY": 0.0621, "CHF": 0.0089, "INR": 0.6536},
        "CNY": {"CAD": 0.1890, "USD": 0.1440, "EUR": 0.1261, "GBP": 0.1123,
                "JPY": 16.1130, "CNY": 1, "CHF": 0.1436, "INR": 10.5313},
        "CHF": {"CAD": 1.3160, "USD": 1.0029, "EUR": 0.8783, "GBP": 0.7818,
                "JPY": 112.1951, "CNY": 6.9630, "CHF": 1, "INR": 73.3300},
        "INR": {"CAD": 0.0179, "USD": 0.0137, "EUR": 0.0120, "GBP": 0.0107,
                "JPY": 1.5301, "CNY": 0.0950, "CHF": 0.0136, "INR": 1}
    }
    while(1):
        inHandCurrency = input("Please enter currency in hand: ")

        requiredCurrency = input("Please enter currency required: ")

        totalAmount = float(input("Please enter amount (currency value): "))

        exchangeRate = crossRateTable[inHandCurrency][requiredCurrency]

        exchangeAmount = totalAmount * exchangeRate
        print(nToMoneyStr(totalAmount) + " in " + inHandCurrency + " is equivalent to " +
              nToMoneyStr(exchangeAmount) + " in " + requiredCurrency)

        print("*" * 45)
