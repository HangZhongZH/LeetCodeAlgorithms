# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = preorder.pop(0)
        node = TreeNode(root)
        k = inorder.index(root)
        node.left = self.buildTree(preorder[: k], inorder[: k])
        node.right = self.buildTree(preorder[k: ], inorder[k + 1: ])
        return node
