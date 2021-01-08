#Part A
#Reads in a file containing a sudoku grid and returns the contents of the file as a Python-readable table.
'''Input: a file name file name, where the file contains n lines, and each line contains n entries separated by
commas. Each entry will either be a positive integer, or the letter ‘x’.'''
'''Output: a table represented as a nested list, where each entry in the orignal file is an element in the table,
and all numbers have been converted to integers.'''

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
#Determines whether a particular value can be entered at a particular location in a valid grid, while maintaining validity.
'''Input: a nested list grid, that represents an n × n sudoku grid; each item in the inner list is either an integer, 
or the string ‘x’; a positive integer num, where 0 < num ≤ n; and two non-negative integers r and c that represent the row 
and column that num will be inserted, where 0 ≤ r, c < n. You may assumegrid[r][c]==‘x’.'''
'''Output: a boolean True if the insertion is valid; otherwise False. For the insertion to be valid, it must result
in a grid that does not contain duplicate numbers in any row, any column, or any subgrid.'''

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

#Part E
#Finds the solution for the given sudoku.
'''Input: a file name file name, where the file contains n lines, and each line contains n entries separated 
by commas. Each entry will either be a positive integer, or the letter ‘x’.'''
'''Output: a nested list representing a completed sudoku grid. You may assume the file given will always 
containexactly one valid solution.'''

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
