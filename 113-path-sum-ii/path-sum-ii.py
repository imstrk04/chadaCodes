# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        res, path = [],[]
        def dfs(node, curSum):

            if not node:
                return
            
            curSum += node.val
            path.append(node.val)

            if not node.left and not node.right and curSum == targetSum:
                res.append(path.copy())
            
            dfs(node.left, curSum)
            dfs(node.right, curSum)

            path.pop()
        
        dfs(root, 0)

        return res