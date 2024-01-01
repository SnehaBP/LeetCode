# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            leftDept=dfs(node.left)
            rightDept=dfs(node.right)
            diameter=max(diameter,leftDept + rightDept)
            return 1+max(leftDept,rightDept)
        diameter=0
        dfs(root)
        return diameter