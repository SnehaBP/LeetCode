# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            def isLeaf(node):
                return node and not node.right and not node.left
            res=0
            if root.left and isLeaf(root.left):
                res+=root.left.val
            else:
                res+=self.sumOfLeftLeaves(root.left)
            res+=self.sumOfLeftLeaves(root.right)
        return res