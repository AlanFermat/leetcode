from collections import defaultdict as dd
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = dd(int)
        output = []
        def helper(node):
            if not node:
                return "#"
            else:
                temp = "("
                temp += helper(node.left)
                temp += ","
                temp += str(node.val)
                temp += ","
                temp += helper(node.right)
                temp += ")"
                res[temp] += 1
                if res[temp] == 2:
                    output.append(node)
                return temp

        helper(root)
        return output