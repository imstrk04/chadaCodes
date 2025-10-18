# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # better O(N) approach
        count = 0
        prefix = {0:1}

        def dfs(node, curSum):
            nonlocal count
            if not node:
                return
            
            curSum += node.val

            count += prefix.get(curSum - targetSum, 0)

            prefix[curSum] = prefix.get(curSum, 0) + 1

            dfs(node.left, curSum)
            dfs(node.right, curSum)

            prefix[curSum] -= 1
        
        dfs(root, 0)
        return count