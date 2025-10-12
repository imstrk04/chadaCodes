# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def inorder(node):
            if node.left:
                inorder(node.left)
            res.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        for i in range(len(res)-1):
            if res[i+1] <= res[i]:
                return False
            
        return True