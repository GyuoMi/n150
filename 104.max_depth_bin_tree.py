# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # can remove base case for iter dfs by just setting res = 0
        # we'd return 0 since the "if node" wouldn't run and we just get back 0 
        if not root: 
            return 0
        # recursive dfs
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # bfs
        # level = 0
        # q = deque([root])
        # while q:
        #
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #
        #     level += 1
        # return level

        # iterative dfs
        stack = [[root, 1]]
        res = 1

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        right res



