# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = {}

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            if node.val in counter:
                counter[node.val] += 1
            else:
                counter[node.val] = 1
            dfs(node.right)
        
        dfs(root)

        counter_sorted = dict(sorted(counter.items(), key = lambda x: x[1], reverse = True))
        res = []
        mode = list(counter_sorted.values())[0]
        for key, val in counter_sorted.items():
            if val == mode:
                res.append(key)
        
        return res