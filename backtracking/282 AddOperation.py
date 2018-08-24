def addOperators(num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    if not num:
        return []
    if len(num) == 1:
        return int(num) == target
    
    def helper(number, start, t,path, last_num,res, target):
        if start == len(number) and t == target:
            res.append(path)
        for end in range(start+1, len(number)+1):
            subnum = number[start:end]
            if len(subnum) > 1 and subnum[0] == "0":
                break
            cur = int(subnum)
            if start == 0:
                helper(number, end, t + cur,path + str(cur), cur, res,target)
            else:
                helper(number, end, t + cur, path + "+" + str(cur), cur, res, target)
                helper(number, end, t - cur, path + "-" + str(cur), -cur,res, target)
                helper(number, end, t - last_num + last_num * cur, path + "*" + str(cur), cur*last_num,res, target)
                
            
                
            
    res = []
    helper(num, 0, 0, '', 0,res, target)
    return res

num = "12321"
target = 8
print (addOperators(num, target))