# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            rightSide = None
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node:
                    rightSide = node # finally we will have right most node in this after for loop ends
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide:
                res.append(rightSide.val)
    
        return res