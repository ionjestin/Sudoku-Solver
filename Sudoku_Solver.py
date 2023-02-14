grid=[[0,6,9,0,0,0,8,0,2],
      [0,0,8,0,3,2,0,0,6],
      [5,0,0,0,0,0,1,0,0],
      [0,0,5,0,0,0,7,0,8],
      [9,0,0,0,1,0,0,2,0],
      [7,2,0,8,0,0,0,6,0],
      [0,0,7,3,0,6,4,0,9],
      [6,0,4,0,7,1,0,0,0],
      [0,0,0,0,0,9,0,0,0]]

import numpy as np
def possible(y,x,n):
    global grid
    for i in range(9):
        if grid[y][i]==n:
            return False
    for i in range(9):
        if grid[i][x]==n:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j]==n:
                return False
    return True
c=0
def solve():
    global c
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                for n in range(1,10):
                    if possible(y,x,n):
                        c+=1
                        grid[y][x]=n
                        solve()
                        grid[y][x]=0
                return
    print(np.matrix(grid))
solve()

