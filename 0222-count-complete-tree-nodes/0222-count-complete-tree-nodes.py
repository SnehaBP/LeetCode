# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lHeight=0
        cur=root
        while cur and cur.left:
            lHeight+=1
            cur=cur.left
        rHeight=0
        cur=root
        while cur and cur.right:
            rHeight+=1
            cur=cur.right
        if lHeight==rHeight:
            return 2**(lHeight+1)-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        
            