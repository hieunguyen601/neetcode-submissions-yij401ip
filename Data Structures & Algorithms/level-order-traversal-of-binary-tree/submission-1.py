# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque([(root, 0)])
        levels = []
        while queue:
            node, level_num = queue.popleft()
            if len(levels) == level_num:
                levels.append([node.val])
            else:
                levels[level_num].append(node.val)

            if node.left is not None:
                queue.append((node.left, level_num + 1))
            if node.right is not None:
                queue.append((node.right, level_num + 1))
        return levels
            