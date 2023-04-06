'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and
a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.   
'''

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        def dfs(r, c):
            grid[r][c] = 2
            is_closed = True
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                if nr >= 0 and nr < m and nc >= 0 and nc < n:
                    if grid[nr][nc] == 0:
                       is_closed &= dfs(nr, nc)
                else:
                    is_closed = False
            return is_closed
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        res += 1
        return res
