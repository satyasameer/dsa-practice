# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return (0, True)
            
            left_height, left_balanced = dfs(root.left)
            right_height, right_balanced = dfs(root.right)

            diff = abs(left_height - right_height)
            current_height = max(left_height, right_height) + 1
            current_balanced = (diff <= 1) and left_balanced and right_balanced

            return (current_height, current_balanced)
        
        _, balanced = dfs(root)
        return balanced