Task: The department you work for has received a project that displays the solved sudoku puzzles in a digital environment. 

Write a Python code to print out the given sudoku puzzle matrix in the following format.
Given format :
sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

Desired output format :
- - - - - - - - - - - - - - -
0  0  0  | 0  6  4  | 0  0  0
7  0  0  | 0  0  0  | 3  9  0
8  0  0  | 0  0  0  | 0  0  0
- - - - - - - - - - - - - - -
0  0  0  | 5  0  2  | 0  6  0
0  8  0  | 4  0  0  | 0  0  0
3  5  0  | 6  0  0  | 0  7  0
- - - - - - - - - - - - - - -
0  0  2  | 0  0  0  | 1  0  3
0  0  1  | 0  5  9  | 0  0  0
0  0  0  | 0  0  0  | 7  0  0
- - - - - - - - - - - - - - -


__________________________________________________


print(*'-------------')
for i in sudoku[0:3]:
    print(*i[0:3], ' | ', *i[3:6], ' | ', *i[6:9])
print(*'-------------')
for i in sudoku[3:6]:
    print(*i[0:3], ' | ', *i[3:6], ' | ', *i[6:9])
print(*'-------------')
for i in sudoku[6:9]:
    print(*i[0:3], ' | ', *i[3:6], ' | ', *i[6:9])
print(*'-------------')
