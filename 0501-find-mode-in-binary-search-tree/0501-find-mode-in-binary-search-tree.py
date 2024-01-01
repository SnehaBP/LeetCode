# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def inorderTraversal(node , freeq):
            if not node:
                return
            inorderTraversal(node.left,freeq)
            freeq[node.val]=freeq.get(node.val,0)+1
            inorderTraversal(node.right,freeq)
        freequency={}
        inorderTraversal(root,freequency)
        maxValue=max(freequency.values())
        modes = [key for key, value in freequency.items() if value == maxValue]
        return modes