# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        current_sum = 0

        if root.left and not root.left.left and not root.left.right:
            current_sum += root.left.val
            left = 0
        else:
            left = self.sumOfLeftLeaves(root.left)

        right = self.sumOfLeftLeaves(root.right)

        return current_sum + left + right
        