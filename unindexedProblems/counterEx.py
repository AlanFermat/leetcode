from collections import Counter
"""
Counter
"""
nums = [1,2,3,3,2,4,1,2,3,0]
c= Counter(nums)
print c


"""
sorted
"""
x = [1,2,3,2,1,3,-3]
x = sorted(x, key = abs, reverse = True)
print x


"""
all
"""

print all([True, 1, {}])