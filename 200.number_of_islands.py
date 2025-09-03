# DFS solution
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0

#         rows, cols = len(grid), len(grid[0])
#         num_islands = 0

#         def dfs(row, col):
#             if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
#                 return

#             grid[row][col] = '0' # Mark as visited
#             dfs(row + 1, col) # Down
#             dfs(row - 1, col) # Up
#             dfs(row, col + 1) # Right
#             dfs(row, col - 1) # Left

#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] == '1':
#                     num_islands += 1
#                     dfs(row, col)

#         return num_islands

# BFS solution
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         rows, cols = len(grid), len(grid[0])
#         visit = set()
#         islands = 0

#         def bfs(r, c):
#             q = collections.deque()
#             visit.add((r,c))
#             q.append((r,c))
            
            # while q:
                # if we change popleft to just pop, this will now act as a dfs
                # since it pops the most recent element (popright) instead of the first
                # iterative instead of recursive

#                 row, col = q.popleft()
#                 dirs = [[1,0], [-1, 0], [0,1], [0, -1]]

#                 for dr, dc in dirs:
#                     r, c = row + dr, col + dc
#                     if (r in range(rows) and 
#                         c in range(cols) and 
#                         grid[r][c] == "1" and 
#                         (r, c) not in visit):
#                         q.append((r,c))
#                         visit.add((r,c))

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r, c) not in visit:
#                     bfs(r, c)
#                     islands += 1
#         return islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        par = [i for i in range(rows * cols)]
        rank = [1] * (rows * cols)
        count = sum(grid[r][c] == '1' for r in range(rows) for c in range(cols))

        def find(i):
            res = i
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(i, j):
            nonlocal count
            p1, p2 = find(i), find(j)
            if p1 == p2:
                return

            count -= 1
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '0':
                    continue

                current_idx = r * cols + c

                for dr, dc, in [(1, 0), (0, 1)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        neighbour_idx = nr * cols + nc
                        union(current_idx, neighbour_idx)

        return count