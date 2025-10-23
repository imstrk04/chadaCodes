# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        maxVal = 0
        def inorder(node):
            nonlocal maxVal
            if not node:
                return node
            
            inorder(node.right)
            node.val += maxVal
            maxVal = node.val
            inorder(node.left)
        
        inorder(root)
        return root