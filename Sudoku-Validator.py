import numpy as np
import math
import sys  
def isinRange(board,N):  
  # Traverse board[][] array
  for i in range(0, N):
    for j in range(0, N): 
      # Check if board[i][j]
      # lies in the range
      if ((board[i][j] <= 0) or
          (board[i][j] > N)):
        return False   
  return True
  
# Function to check if the solution of sudoku puzzle is valid or not
def isValidSudoku(board,N):
  S=int(math.sqrt(N))
  # Check if all elements of board[][] and stores value in the range[1, 9]
  if (isinRange(board,N) == False):
    return False
  # Stores unique value from 1 to N
  unique = [False] * (N + 1)
 
  # Traverse each row of the given array
  for i in range(0, N):
     
    # Initialize unique[] array to false
    for m in range(0, N + 1):
      unique[m] = False
 
    # Traverse each column of row
    for j in range(0, N):
      Z = board[i][j]
      # Check if current row stores duplicate value
      if (unique[Z] == True):
        return False
      unique[Z] = True
 
  # Traverse each column 
  for i in range(0, N):
     
    # Initialize unique[]  array to false
    for m in range(0, N + 1):
      unique[m] = False
 
    # Traverse each row of column
    for j in range(0, N):
      Z = board[j][i]
 # Check if current column stores duplicate value
      
      if (unique[Z] == True):
        return False
      unique[Z] = True
 
  # Traverse sub grid in board[][] array
  for i in range(0, N - S, S):
     
    # j stores first column of each 3 * 3 block
    for j in range(0, N - S, S):
       
      # Initialize unique[]
      # array to false
      for m in range(0, N + 1):
        unique[m] = False
 
      # Traverse current block
      for k in range(0, S):
        for l in range(0, S):
           
          # Stores row number of current block
          X = i + k
 
          # Stores column number of current block
          Y = j + l
 
          # Stores the value of board[X][Y]
          Z = board[X][Y]
 
          # Check if current block stores duplicate value
          if (unique[Z] == True):
            return False
           
          unique[Z] = True
           
  # If all conditions satisfied
  return True
# Driver Code
if __name__ == '__main__':
  print("Enter the Dimensions of Sudoku")
  R = int(input())
  C = int(input())

# For printing the matrix
  text_file = np.loadtxt('Sudo.txt', dtype=int)
  matrix=np.array(text_file).reshape(R,C)
  print(matrix)
  if (isValidSudoku(matrix,N=R)):
    print("Valid")
  else:
    print("Not Valid") 