# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 递归
            return self.helper(root, root)

        def helper(self, root1, root2):
            if root1 == None and root2 == None:
                return True
            if (root1 == None and root2 != None) or (root1 != None and root2 == None):
                return False
            if root1.val == root2.val:
                return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)
            if root1.val != root2.val:
                return False

        ####################################################################################
        # 迭代
        rootnode = [root]
        while rootnode:
            newroot = []
            val = []
            for item in rootnode:
                if item:
                    newroot.append(item.left)
                    newroot.append(item.right)
                    val.append(item.val)
                    continue
                val.append(None)
            if val != val[::-1]:
                return False
            rootnode = newroot
        return True
