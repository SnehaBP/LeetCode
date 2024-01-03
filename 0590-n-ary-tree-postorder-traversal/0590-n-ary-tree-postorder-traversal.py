"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        if not root:
            return res
        def preorderTraversal(node):
            if not node:
                return 
            for child in node.children:
                preorderTraversal(child)
            res.append(node.val)
        preorderTraversal(root)
        return res