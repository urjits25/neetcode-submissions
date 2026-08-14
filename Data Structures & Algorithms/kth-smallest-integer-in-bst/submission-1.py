# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        For a BST, kth smallest integer is the kth element during inorder traversal
        Inorder: L Par R

        maintain global var with value of current node
        count down from k to 1

        inorder(cur)
            inorder(cur.left)
            self.k -= 1
            self.res = cur.val
            if self.k == k: 
                return self.res
            inorder(cur.right)
        
        inorder(root)
        '''
        self.res = None
        self.k = k
        def inorder(cur):
            if cur.left and self.res is None:
                inorder(cur.left)
            
            if self.k == 0:
                return 

            if self.k == 1:
                self.res = cur.val
            self.k -= 1

            if cur.right and self.res is None:
                inorder(cur.right)
        
        inorder(root)
        return self.res