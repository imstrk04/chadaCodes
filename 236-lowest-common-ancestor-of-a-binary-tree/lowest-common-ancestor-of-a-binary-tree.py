# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node):
            if node == None or node == p or node == q:
                return node
            
            left = lca(node.left)
            right = lca(node.right)

            if not left:
                return right
            elif not right:
                return left
            else:
                return node
            
            return node
        
        return lca(root)