def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    
    def multiSingleDigit(num, d):
        temp = 0
        factor = 1
        for j in range(len(num)-1, -1, -1):
            temp += int(num[j])* int(d) * factor
            factor *= 10
        return temp
    ans = 0
    f = 1
    for j in range(len(num1)-1, -1, -1):
        ans += multiSingleDigit(num2,num1[j]) * f
        f *= 10
    return str(ans)


num = "343"
d = "9"
print (multiSingleDigit(num, d))