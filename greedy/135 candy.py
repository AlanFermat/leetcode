def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    idx = 0
    n = len(ratings)
    temp = [1] * n
    while idx < n:
        if idx > 0:
            if ratings[idx] > ratings[idx-1] and temp[idx] <= temp[idx-1]:
                temp[idx] = temp[idx-1] + 1
        idx += 1
    idx -= 1
    while idx > -1:
        if idx < n -1 :
            if ratings[idx] > ratings[idx+1] and temp[idx] <= temp[idx+1]:
                temp[idx] = temp[idx+1]+1
        idx -= 1
    return sum(temp)

ratings = [-1,-8,10,1,0,9]
print (candy(ratings))