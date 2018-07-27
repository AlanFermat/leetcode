class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1:
            return False
        if not root2:
            return False
        self.seq1 = []
        self.seq2 = []
        def getSeq(temp, root):
            if not root.left and not root.right:
                temp.append(root.val)
            if root.left:
                getSeq(temp,root.left)
            if root.right:
                getSeq(temp, root.right)
        getSeq(self.seq1, root1) 
        getSeq(self.seq2, root2)
        print self.seq1
        print self.seq2
        return self.seq1 == self.seq2
