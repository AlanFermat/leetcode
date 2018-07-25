def binaryGap(N):
    """
    :type N: int
    :rtype: int
    """
    binary = bin(N)
    longest, temp = 0, 0
    stack = []
    idx = 0
    n = len(binary)
    print (binary)
    while idx < n:
        if binary[idx] == '1':
            while stack:
                if stack[-1] != '1':
                    stack.pop()
                    temp += 1
                else:
                    temp += 1
                    longest = max(temp, longest)
                    break
            stack.append(binary[idx])
            temp = 0
            
        else:
            stack.append(binary[idx])
        idx += 1
    return longest

N = 0
print (binaryGap(N))