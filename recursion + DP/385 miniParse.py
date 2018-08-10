def parse(s):
    """
    :type s: str
    :rtype: NestedInteger
    """
    # s = "[123,[456,[789]]]"
    st = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "[":
            st.append("[")
            i += 1
        elif ch.isdigit() or ch == '-':
            sign = 1
            if ch == '-':
                sign = -1
                i += 1
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num*10 + int(s[i])
                i += 1
            st.append(NestedInteger(num*sign))
        elif ch == ',':
            i += 1
        elif ch == "]":
            temp = []
            while st[-1] != "[":
                temp.append(st.pop())
            st.pop()
            ni = NestedInteger()
            while temp:
                e = temp.pop()
                ni.add(e)
            st.append(ni)
            i += 1
    return st.pop()

s = "3,[123,[-12]]"
print (parse(s))