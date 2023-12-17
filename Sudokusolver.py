board = [                                               # Lists inside a list
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo):
    find = find_empty(bo)
    if not find:                                        # If there is not 0, the board is completed already, return True to exit the function
        return True                                     # if not = return None on find_empty()
    else:                                               # empty was found
        row, col = find                                 # find means the value returned by find_empty()

    for i in range(1,10):
        if valid(bo, i, (row, col)):                    # (row, col) = position of the empty  
            bo[row][col] = i                            # trying 1-9, if i is valid, put i in the empty position

            if solve(bo):                               # recursion, keep trying until we find the solution = no empty = return True, or 1-9 are both not valid = return False
                return True                             # if solve(bo) returned True = no empty
                                                  # else = solve(bo) returned False (not valid)
            bo[row][col] = 0                        # if we cannot finish the solution, reset the value

    return False                                        # if no valid, return false


def valid(bo, num, pos):                                # bo = board, num = number, pos = (row, col)
    # Check row
    for i in range(len(bo[0])):                         # len(board[0]) = len(board) = 9
        if bo[pos[0]][i] == num and pos[1] != i:        # pos = (row, col), pos[0] = row, pos[1] = col, works like a List
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:        # "pos[0] != i" to make sure that we dont check the position we just inserted thing into
            return False

    # Check box
    box_x = pos[1] // 3                                 # // = integer division, e.g.: 5 /
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):               # e.g. range(0,5) = '0,1,2,3,4', ending value not included
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(bo):
    for i in range(len(bo)):                            # rows ofr board
        if i == 3 or i == 6:                            # i starting from 0, i = 0 to 8 in this function
            print("- - - - - - - - - - - -  ")

        for j in range(len(bo[0])):                     # columns of each row
            if j == 3 or j == 6:
                print(" | ", end="")                    # No new line

            if j == 8:                                  # 9th number
                print(bo[i][j])                         # Make a new line
            else:                                       # deal with special case first, else is majority
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print("________________________")
print_board(board)