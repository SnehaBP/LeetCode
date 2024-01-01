# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorderTraversal(node):
            nonlocal prevValue,minDiff
            if not node:
                return 
            inorderTraversal(node.left)
            if prevValue is not None:
                minDiff=min(minDiff,node.val-prevValue)
            prevValue=node.val
            inorderTraversal(node.right)
        minDiff=float('inf')
        prevValue=None
        inorderTraversal(root)
        return minDiff