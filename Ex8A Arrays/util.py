# A module for manipulating 2-dimensional arrays of size 4x4.
# Vincent T Mukwevo  MKWVIN004
# 16/04/2024
import copy
def create_grid(grid):
    """create a 4x4 array of zeroes within grid"""
    Row = []
    for i in range(4):
         grid.append(Row)
         Row.clear()
         for h in range (4):
             Row.append(0)
    return(grid)
    
def print_grid (grid):
    grid1 = copy_grid(grid)
    print('+--------------------+')
    for row in range (4):
        if row >= 1:
          print('|')
        for column in range(4):
           if column == 0:
            print('|', end = '')
           if (grid1[row][column]) == 0: (grid1[row][column]) = ' '
           print( '{0: <5.5s}'.format(str( grid1[row][column])),end = '')
    print('|')
    print('+--------------------+')

def check_lost (grid):
     # function to check if gameover by iterating over each element to check for legal moves
     """return True if there are no 0 values and there are no adjacent values that are equal; otherwise False"""
     for row in range (3):
         for column in range (3):
          if (grid[row][column] == grid[row][column+1])  :
              return False
          if row >=1 and (grid[row][column] == grid[row-1][column]):
                     return False
          if row <= 2 and (grid[row][column] == grid[row+1][column]):
                     return False
          if (grid[row][column] == 0) or (grid[3][3] == 0):
                 return False
     return True


def check_won (grid):
     # function to check if game won by checking for the target value if made 
     """return True if a value>=32 is found in the grid; otherwise False"""
     for row in range (4):
         for column in range (4):
             if grid[row][column] >= 32:
                 return True
     return False
     

def copy_grid (grid):
     """return a copy of the given grid"""
     grid_copy = copy.deepcopy(grid)
    
     return(grid_copy)

def grid_equal (grid1, grid2): 
    # function to check if a move was made by cheching if grids are equal
    """check if 2 grids are equal - return boolean value"""
    if grid1 == grid2:
        return True
    else:
        return False
    