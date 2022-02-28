"""
step 1 pick empty square
step 2 try all numbers, find one that works
step 3 repeat
step 4 when blocked, backtrack
"""

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True  # complete
    else:
        row, col = find

    for i in range(1, 10):
        if valid(sudoku, i, (row, col)):
            sudoku[row][col] = i

            if solve(sudoku):
                return True

        sudoku[row][col] = 0  # backtrack

    return False


def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')

        for j in range(len(sudoku[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')  # end='' avoid the line break

            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + ' ', end='')


def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return i, j  # row, col

    return None


def valid(sudoku, picked_number, position):
    # check row
    for i in range(len(sudoku[0])):
        if sudoku[position[0]][i] == picked_number and position[1] != i:  # position[1] is the inserted position
            return False

    # check column
    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == picked_number and position[0] != i:  # position(0, 1) -> position[column] [row]
            return False

    # check box
    box_x = position[1] // 3
    box_y = position[0] // 3  # what box we are in. 0,0 first, 0,1 second etc...

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):  # what box we are in *3 to have the index
            if (sudoku[i][j]) == picked_number and (i, j) != position:
                return False

    return True


print_sudoku(board)
solve(board)
print('__________________________________')
print_sudoku(board)
