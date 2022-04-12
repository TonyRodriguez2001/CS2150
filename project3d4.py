def add(a,b,base):
  
    charList = list(base.strip(" "))
    print(charList[0])
    print("Hello")
    len_a = len(a)
    len_b = len(b)
    
    baseX = len(base)
    
    s = ""
    sum = ""
  
    diff = abs(len_a - len_b)
      
    # Padding 0 in front of the
    # number to make both numbers equal
    for i in range(1,diff+1):
        s += ord(charList[0])
      
    # Condition to check if the strings
    # have lengths mis-match
    if (len_a < len_b):
        a = s + a
    else:
        b = s + b
  
    carry = 0;
      
    # Loop to find the find the sum
    # of two integers of base B
    for i in range(max(len_a, len_b) - 1,-1,-1):
          
        # Current Place value for
        # the resultant sum
        curr = carry + (ord(a[i]) -ord(charList[0])) + ( ord(b[i]) - ord(charList[0]))
  
        # Update carry
        carry = curr // baseX
  
        # Find current digit
        curr = curr % baseX
  
        # Update sum result
        sum = chr(curr + ord(charList[0])) + sum
         
        if (carry > 0):
            sum = chr(carry + ord(charList[0]) + sum
        
    print(sum)
    return sum
    
duodecimal = '0123456789AB'
add('123','123',duodecimal)
