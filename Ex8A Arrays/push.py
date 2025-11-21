# A program to run a game 2048
# Vincent T Mukwevo MKWVIN004
# 17/04/2024

def push_up (grid):
   """merge grid values upwards"""
   for column in range (4):
         if  grid[2][column] == grid[3][column]:
              grid[2][column]  += (grid[3][column])
              grid[3][column] = 0
         elif grid[1][column] == grid[2][column]:
              grid[1][column] += (grid[2][column])
              grid[2][column] = 0
         if grid[0][column] == grid[1][column]:
              grid[0][column] += (grid[1][column])
              grid[1][column] = 0
        
         if  grid[0][column] == 0:
              grid[0][column] = (grid[1][column])
              grid[1][column] = 0
         if  grid[1][column] == 0:
              grid[1][column] = (grid[2][column])
              grid[2][column] = 0
         if  grid[2][column] == 0:
              grid[2][column] = (grid[3][column])
              grid[3][column] = 0
   return(grid) 
     
def push_down (grid):
      """merge grid values downwards"""
      for column in range (4):
         if grid[3][column] == grid[2][column]:
              grid[3][column] += (grid[2][column])
              grid[2][column] = 0
         if grid[2][column] == grid[1][column]:
              grid[2][column] += (grid[1][column])
              grid[1][column] = 0
         if  grid[1][column] == grid[0][column]:
              grid[1][column] += (grid[0][column])
              grid[0][column] = 0
         if  grid[3][column] == 0:
              grid[3][column] = (grid[2][column])
              grid[2][column] = 0
         if  grid[2][column] == 0:
              grid[2][column] = (grid[1][column])
              grid[1][column] = 0
         if  grid[1][column] == 0:
              grid[1][column] = (grid[0][column])
              grid[0][column] = 0
         if  grid[2][column] == 0:
              grid[2][column] = (grid[1][column])
              grid[1][column] = 0
     
      return(grid) 
   

def push_left (grid):
    """merge grid values left"""
    for row in range (4):
         if grid[row][0] == grid[row][1]:
              grid[row][0] += (grid[row][1])
              grid[row][1] = 0
         if grid[row][1] == grid[row][2]:
              grid[row][1] += (grid[row][2])
              grid[row][2] = 0
         if  grid[row][2] == grid[row][3]:
              grid[row][2] += (grid[row][3])
              grid[row][3] = 0
         if  grid[row][0] == 0:
              grid[row][0] = (grid[row][1])
              grid[row][1] = 0
         if  grid[row][1] == 0:
              grid[row][1] = (grid[row][2])
              grid[row][2] = 0
         if grid[row][2] == 0:
              grid[row][2] = (grid[row][3])
              grid[row][3] = 0
         if  grid[row][1] == 0:
              grid[row][1] = (grid[row][2])
              grid[row][2] = 0
 
    return(grid) 

def push_right (grid):
   for row in range (4):
         if (grid[row][3]) == grid[row][2]:
              grid[row][3] += (grid[row][2])
              grid[row][2] = 0
         if  grid[row][2] == grid[row][1]:
              grid[row][2] += (grid[row][1])
              grid[row][1] = 0
         if  grid[row][1] == grid[row][0]:
              grid[row][1] += (grid[row][0])
              grid[row][0] = 0
         if  grid[row][3] == 0:
              grid[row][3] = (grid[row][2])
              grid[row][1] = 0
         if  grid[row][2] == 0:
              grid[row][2] = (grid[row][1])
              grid[row][1] = 0
         if  grid[row][1] == 0:
              grid[row][1] = (grid[row][0])
              grid[row][0] = 0
         if  grid[row][2] == 0:
              grid[row][2] = (grid[row][1])
              grid[row][1] = 0

   return(grid) 