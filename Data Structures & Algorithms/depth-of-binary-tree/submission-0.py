# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs depth
        if not root:
            return 0
        depth = 0
        bfs = deque([root])
        while bfs:
            depth += 1
            for _ in range(len(bfs)):
                cur = bfs.popleft()
                if cur.left: bfs.append(cur.left)
                if cur.right: bfs.append(cur.right)
        return depth