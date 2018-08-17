from collections import defaultdict as dd
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        d = dd(list)
        temp = [(root, 0)]
        res = []
        for node, pos in temp:
            if node:
                d[pos] += [node.val]
                temp += [(node.left, pos-1)]
                temp += [(node.right, pos+1)]
        for key in sorted(d):
            res.append(d[key])
        return res