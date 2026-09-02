# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        diam = lheight + rheight
        '''
        self.res = 0
        
        def dfs(node):
            if not node.left and not node.right:
                return 0
            
            lh = rh = 0
            if node.left:
                lh = 1 + dfs(node.left)
            if node.right:
                rh = 1 + dfs(node.right)
            
            self.res = max(self.res, lh + rh)
            return max(lh, rh)

        dfs(root)
        return self.res