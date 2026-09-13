# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## DFS
        ## use a stack and add root to stack
        ## pop it, then add its children, keeping track of depth as well
        ## continue while stack

        stack = [[root, 1]]
        depth = 0
        res = 0
        while stack:
            curr, depth = stack.pop()
            if curr:
                res = max(res, depth)
                stack.append([curr.left, depth + 1])
                stack.append([curr.right, depth + 1])
        return res





        