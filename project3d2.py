def stringToInt(number, base):
    # TODO: implement number parser

        charList = list(base.strip(" "))
        base = len(charList)

        numList = list(number.strip(" "))

        i = len(numList) - 1
        cout  = 0
        base10Val = 0
        while i >= 0:
                symbol = numList[i]
                symVal = charList.index(symbol) * (base ** cout)
                base10Val += symVal
                cout += 1
                i -= 1


        return base10Val

