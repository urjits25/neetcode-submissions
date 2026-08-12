# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    '''
    - iterate through all the nodes of parent 
    - if parent.root matches subtree.root, we check if they're the same tree
        - if yes, early exit, return true
        - if no, continue traversing the parent
    '''
    def isSameTree(self, root, subr):
        if not root and not subr:
            return True
        if not root or not subr:
            return False
        
        return root.val == subr.val and \
            self.isSameTree(root.left, subr.left) and \
            self.isSameTree(root.right, subr.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        bfs_q = [root]
        while bfs_q:
            new_bfs_q = []
            for cur in bfs_q:
                if cur.val == subRoot.val:
                    if self.isSameTree(cur, subRoot):
                        return True
                if cur.left: new_bfs_q.append(cur.left)
                if cur.right: new_bfs_q.append(cur.right)
            bfs_q = new_bfs_q
        return False
