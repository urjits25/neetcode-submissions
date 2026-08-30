# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # recursion
        # if p < cur and cur > q: return cur

        if root.val == p.val or root.val == q.val:
            return root
        
        if p.val > q.val: 
            q, p = p, q
        
        if p.val < root.val < q.val:
            return root
        
        if q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)