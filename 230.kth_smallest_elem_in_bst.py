# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         res = []
#         def dfs(node):
#             if not node:
#                 return
            
#             dfs(node.left)
#             res.append(node.val)
#             dfs(node.right)

#         dfs(root)
#         return res[k - 1]

# OPTIMAL since we dont traverse entire tree every time, even if k=1
# we can stop early


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            # go left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1 # decrement k for every node we visit/process
            if k == 0:
                return curr.val

            # move to right subtree
            curr = curr.right
