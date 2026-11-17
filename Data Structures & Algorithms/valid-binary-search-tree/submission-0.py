# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, minimum, maximum = stack.pop()

            if not(minimum < node.val < maximum):
                return False
            
            if node.left is not None:
                stack.append((node.left, minimum, node.val))
            if node.right is not None:
                stack.append((node.right, node.val, maximum))
            
        return True