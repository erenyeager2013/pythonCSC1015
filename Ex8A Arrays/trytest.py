# goofing
import util
grid = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
grid_copy = util.create_grid([])

for row in range(4):
          lis = (grid[row])
          for column in range (4):
               grid_copy[row][column] = (lis.pop())

print(grid_copy)