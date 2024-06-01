# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inOrderTraversal(root):
            if not root:
                return []
            return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right)
        def newBST(nums):
            if not nums:
                return
            newRoot = TreeNode(nums[0])
            cur = newRoot
            for val in nums[1:]:
                cur.right = TreeNode(val)
                cur = cur.right
            return newRoot
        values = inOrderTraversal(root)
        values.sort
        return newBST(values)
        



            