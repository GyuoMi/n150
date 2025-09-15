# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         def inorder(node):
#             if not node:
#                 return
            
#             inorder(node.leftj)
#             res.append(node.val)
#             inorder(node.right)
        
#         inorder(root)
#         return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(root):
            if not root:
                return []

            # this line mirrors the inorder traversal stack by first going left, visiting the root, then going right
            return dfs(root.left) + [root.val] + dfs(root.right)

        return dfs(root)
