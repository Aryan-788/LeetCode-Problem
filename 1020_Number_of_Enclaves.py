'''
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.'''

class Solution:
  WATER = 0
  LAND = 1

  def numEnclaves(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])

    for i in range(n):
      self.sink_island(i, 0, grid)
      self.sink_island(i, m - 1, grid)

    for j in range(m):
      self.sink_island(0, j, grid)
      self.sink_island(n - 1, j, grid)

    return sum(map(sum, grid))

  @classmethod
  def sink_island(cls, row: int, col: int, grid: List[List[int]]):
    if grid[row][col] == cls.LAND:
      grid[row][col] = cls.WATER
      if row > 0:
        cls.sink_island(row - 1, col, grid)
      if row < len(grid) - 1:
        cls.sink_island(row + 1, col, grid)
      if col < len(grid[0]) - 1:
        cls.sink_island(row, col + 1, grid)
      if col > 0:
        cls.sink_island(row, col - 1, grid)

        
