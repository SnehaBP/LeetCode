# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(node,leaveList):
            if node:
                if not node.left and not node.right:
                    leaveList.append(node.val)
                getLeaves(node.left,leaveList)
                getLeaves(node.right,leaveList)
        list1=[]
        list2=[]
        getLeaves(root1,list1)
        getLeaves(root2,list2)
        return list1==list2