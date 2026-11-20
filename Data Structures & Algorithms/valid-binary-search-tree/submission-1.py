# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            current, minimum, maximum = stack.pop()
            if not(minimum < current.val < maximum):
                return False
            
            if current.left is not None:
                stack.append((current.left, minimum, current.val))
            if current.right is not None:
                stack.append((current.right, current.val, maximum))
        return True