# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        # print(root.val, key)
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key == root.val:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            current = root.right
            while current.left:
                current = current.left
            root.val = current.val
            root.right = self.deleteNode(root.right, current.val)
        
        return root

        