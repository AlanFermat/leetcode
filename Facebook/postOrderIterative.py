# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        if not root:
            return res
        while True:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.right
            if not stack:
                return res[::-1]
            node = stack.pop()
            root = node.left



# build tree from traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        m = {}
        for i in range(len(inorder)):
            m[inorder[i]] = i
        return self.build(postorder, m, 0, len(inorder)-1)

    def build(self, postorder, m, start, end):
        if postorder:
            if start <= end:
                root_val = postorder.pop()
                idx = m[root_val]
                root = TreeNode(root_val)
                root.right = self.build(postorder, m , idx+1, end)
                root.left = self.build(postorder, m, start, idx-1)
                
                return root
        else:
            return 
        
