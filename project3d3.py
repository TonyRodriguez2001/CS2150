def stringToInt(number, base):
    # TODO: implement number parser

        charList = list(base.strip(" "))
        base = len(charList)

        n, k, a, b = int(number), base, 0, 0

        index = 0
        numList = []

        while n > 0.0:
            b = n % base
            numList.append(charList[int(b)])
            a = (n - b) / k
            n -= b
            n /= k
            index += 1
        
        numString = ""
        
        i = len(numList) - 1
        while i >= 0:
            numString += numList[i]
            i -= 1

        return numString
