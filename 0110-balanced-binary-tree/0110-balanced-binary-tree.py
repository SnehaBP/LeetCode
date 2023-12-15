# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalenced(node):
            if not node:
                return 0
            lNode=checkBalenced(node.left)
            rNode=checkBalenced(node.right)
            if lNode==-1 or rNode==-1 or abs(lNode-rNode)>1:
                return -1
            else:
                return 1+max(lNode,rNode)
        return checkBalenced(root)!=-1