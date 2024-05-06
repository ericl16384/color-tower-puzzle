# Game is called 36 Cube


board_obstacles = (
    (5, 4, 1, 2, 0, 3),
    (1, 3, 0, 5, 2, 4),
    (2, 0, 3, 1, 4, 5),
    (4, 5, 2, 3, 1, 0),
    (3, 1, 4, 0, 5, 2),
    (0, 2, 5, 4, 3, 1),
)

board_spaces = []
for row in board_obstacles:
    board_spaces.append([])
    for item in row:
        board_spaces[-1].append(6 - item)


def list_product(arr):
    out = 1
    for x in arr:
        out *= x
    return out
six_factorial = 1*2*3*4*5*6

for i in range(6):
    assert list_product(board_spaces[i]) == six_factorial
    assert list_product([row[i] for row in board_spaces]) == six_factorial


for row in board_spaces:
    print(row)
print()



# https://www.geeksforgeeks.org/sudoku-backtracking-7/
# Backtracking


def print_grid(grid):
    for row in grid:
        line = ""
        for v in row:
            line += ".ROYGBP"[v]
            line += " "
        print(line)

grid = []
for y in range(6):
    grid.append([0]*6)
# grid[0][1] = 4

def move_is_safe(grid, row, col, num):

    # Check if we find the same num
    # in the similar row , we
    # return false
    for x in range(6):
        if grid[row][x] == num:
            return False

    # Check if we find the same num in
    # the similar column , we
    # return false
    for x in range(6):
        if grid[x][col] == num:
            return False

    return True

def solve_puzzle(grid, row, col):
    # check if finished puzzle
    if row == 6 - 1 and col == 6:
        return True
    
    # check if finished row
    if col == 6:
        row += 1
        col = 0
    
    todo

print_grid(grid)