# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0
        def dfs(node, maxNode):
            if not node:
                return
            if node.val >= maxNode:
                self.goodNodes += 1
                
            maxNode = max(maxNode, node.val)
            dfs(node.left, maxNode)
            dfs(node.right, maxNode)
            
        dfs(root, root.val)

        return self.goodNodes