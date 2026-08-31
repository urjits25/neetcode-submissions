# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, cmin, cmax):
            if not root:
                return True
            
            return cmin < root.val < cmax and dfs(root.left, cmin, root.val) and dfs(root.right, root.val, cmax)

        return dfs(root, float("-inf"), float("inf"))