# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []
        while stack:
            current = stack.pop()
            if current:
                stack.append(current.left)
                stack.append(current.right)
                result.append(current.val)
            # print(stack)
        
        return list(reversed(result))

        #if root is None:
        #    return []
        # 
        #left = self.postorderTraversal(root.left)
        #right = self.postorderTraversal(root.right)
        #
        #return left + right + [root.val]