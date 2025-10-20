# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        prev = None
        one = None
        two = None

        def inorder(curr):
            nonlocal prev, one, two
            if not curr:
                return
            
            inorder(curr.left)
            if (prev is not None and prev.val > curr.val):
                if one is None:
                    one = prev
                two = curr
            prev = curr
            inorder(curr.right)
        
        inorder(root)
        temp = one.val
        one.val = two.val
        two.val = temp