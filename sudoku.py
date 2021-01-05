###Task 2
#Part A
def grid_from_file(file_name):
    f = open(file_name)
    myfile = f.readlines()
    f.close()
    alist = []
    blist = []
    for a in myfile:
        alist.append(a.strip())
    for b in range(len(alist)):
        blist.append(alist[b].split(","))
        for c in range(len(blist[b])):
            if blist[b][c] != "x":
               blist[b][c] = int(blist[b][c])
    return(blist)

#Part B
def valid_entry(grid , num , r , c):
    for a in grid[r]:
        if num == a:
           return(False)
    for b in grid:
        if num == b[c]:
           return(False)
    subg = []
    nsqr = int(len(grid) ** (0.5))
    sr = (r // nsqr) * nsqr
    sc = (c // nsqr) * nsqr
    for d in range(sr , sr + nsqr):
        for e in range(sc , sc + nsqr):
            subg.append(grid[d][e])
    for f in subg:
        if num == f:
           return(False)
    return(True)

#Part C
from copy import deepcopy
def grids_augmented_in_row(grid , num , r):
    if num in grid[r]:
       return([grid])
    M = []
    for c in range(len(grid)):
        if grid[r][c] == "x":
           aBool = valid_entry(grid , num , r , c)
           if aBool == True:
              mygrid = deepcopy(grid)
              mygrid[r][c] = num
              M.append(mygrid)
    return(M)

#Part D
def grids_augmented_with_number(grid , num , a = 0 , m = 0):
    if a == 0:
       m = len(grid)
       N = [deepcopy(grid)]
    else:
        N = grid
        
    if a == m:
       return(N)
    n = len(N)
    b = 0
    M = []
    while b < n:
          M += grids_augmented_in_row(N[b] , num , a)
          b += 1
    N = M
    a += 1
    return(grids_augmented_with_number(N , num , a , m))

#Part E
def compeleted(file):
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j] == "x":
               return(False)
    return(True)

def step(file):
    for i in range(len(file) - 1 , - 1 , - 1):
        for j in range(len(file[i]) - 1 , - 1 , - 1):
            if file[i][j] == "x":
               a = i
               b = j
    res = []
    for num in range(1 , len(file) + 1):
        if valid_entry(file , num , a , b) == True:
           f  = deepcopy(file)
           f[a][b] = num
           res.append(f)
    return(res)

def backtracking(part):
    if compeleted(part) == True:
       return(part)
    else:
        res = []
        for i in step(part):
            res += backtracking(i)
        return(res)
    
def solve_sudoku(file_name):
    file = grid_from_file(file_name)
    return(backtracking(file))
