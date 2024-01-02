# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def tiltAndSum(node):
            if not node:
                return 0, 0  
            leftTilt, leftSum = tiltAndSum(node.left)
            rightTilt, rightSum = tiltAndSum(node.right)
            currentTilt = abs(leftSum - rightSum)
            currentSum = node.val + leftSum + rightSum
            return leftTilt + rightTilt + currentTilt, currentSum
        totalTilt, _ = tiltAndSum(root)
        return totalTilt