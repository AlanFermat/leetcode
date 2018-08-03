def parse(s):    
    stack = {}
    depth = 1
    idx = 0
    n = len(s)
    multiplier = 1
    num= ""
    while idx < n:
        if s[idx] == '[':
            num = ""
            multiplier = 1
            depth += 1
        elif s[idx] == '-':
            multiplier = -1
        elif s[idx].isdigit():
            num += s[idx]
        elif s[idx] == ',' or s[idx] == ']':
            number = int(num) * multiplier
            stack[depth] = number
        idx += 1
    return stack

s = "3,[123,[-12]]"
print (parse(s))