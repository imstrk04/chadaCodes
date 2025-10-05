# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        
        def getHeight(node, maxi):
            if node is None:
                return 0
            
            leftHeight = getHeight(node.left, maxi)
            rightHeight = getHeight(node.right, maxi)

            self.maxi = max(self.maxi,leftHeight+rightHeight)

            return 1 + max(leftHeight, rightHeight)
        
        getHeight(root, float('-inf'))

        return self.maxi