# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []

        res = []
        bfs = deque([root])
        while bfs:
            res.append(bfs[-1].val) 
            for _ in range(len(bfs)):
                cur = bfs.popleft()
                if cur.left:
                    bfs.append(cur.left)
                if cur.right:
                    bfs.append(cur.right)
            print([x.val for x in bfs])
        return res