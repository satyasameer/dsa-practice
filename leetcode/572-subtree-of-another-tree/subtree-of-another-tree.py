# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        
        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)

        return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        if left:
            return True
        right = self.isSubtree(root.right, subRoot)

        return left or right