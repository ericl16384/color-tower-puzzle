# Game is called 36 Cube


board_obstacles = [
    [5, 4, 1, 2, 0, 3],
    [1, 3, 0, 5, 2, 4],
    [2, 0, 3, 1, 4, 5],
    [4, 5, 2, 3, 1, 0],
    [3, 1, 4, 0, 5, 2],
    [0, 2, 5, 4, 3, 1],
]

grid = []
for y in range(6):
    grid.append([0]*6)



# sneaky trick that we had to look up :)
board_obstacles[2][3], board_obstacles[4][3] = board_obstacles[4][3], board_obstacles[2][3]
grid[2][3] = 2
grid[4][3] = 3




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

# for i in range(6):
#     assert list_product(board_spaces[i]) == six_factorial
#     assert list_product([row[i] for row in board_spaces]) == six_factorial


for row in board_spaces:
    print(row)
print()



# https://www.geeksforgeeks.org/sudoku-backtracking-7/
# Backtracking


def print_grid(height_map, grid):
    for y, row in enumerate(grid):
        line = ""
        for x, v in enumerate(row):
            line += str(6 - height_map[y][x])
            line += ".ROYGBP"[v]
            line += " "
        print(line)



def move_is_safe(height_map, remaining_pieces, grid, row, col, color):

    # Check if we find the same color
    # in the similar row , we
    # return false
    for x in range(6):
        if grid[row][x] == color:
            return False

    # Check if we find the same color in
    # the similar column , we
    # return false
    for x in range(6):
        if grid[x][col] == color:
            return False
    
    # check if height for color is valid
    if not remaining_pieces[color-1][height_map[row][col]]:
        return False

    return True

current_best_score = 0
# current_best_grid = []

def solve_puzzle(height_map, remaining_pieces, grid, row, col):
    global current_best_score
    # print_grid(height_map, grid)
    # # print(row, col)
    # print()
    # for i, color in enumerate(remaining_pieces):
    #     line = ""
    #     line += ".ROYGBP"[i+1]
    #     for j, h in enumerate(color):
    #         if h:
    #             line += str(6 - j)
    #         else:
    #             line += " "
    #     print(line)
    # input()
    # print()

    # check if finished puzzle
    if row == 6 - 1 and col == 6:
        return True
    
    # check if finished row
    if col == 6:
        row += 1
        col = 0
    
    # recurse if cell is finished
    if grid[row][col] > 0:
        return solve_puzzle(height_map, remaining_pieces, grid, row, col + 1)
    
    for color in range(1, 6+1):
        if move_is_safe(height_map, remaining_pieces, grid, row, col, color):
            grid[row][col] = color
            remaining_pieces[color-1][height_map[row][col]] = False

            if solve_puzzle(height_map, remaining_pieces, grid, row, col + 1):
                return True

            if row * 6 + col + 1 > current_best_score:
                current_best_score = row * 6 + col + 1
                # current_best_grid = []
                # for row in grid:
                #     current_best_grid.append(row.copy())
                print("score", current_best_score)
                print_grid(height_map, grid)
                print()
                # input()
            # print("score", row * 6 + col)
            # print_grid(height_map, grid)
            # print()
        
            # assumption was wrong, remove value
            # also revert remaining height for color
            grid[row][col] = 0
            remaining_pieces[color-1][height_map[row][col]] = True
            # print("backtrack")
    
    return False

# print_grid(grid)
heights_remaining = []
for i in range(6):
    heights_remaining.append([True]*6)

import time
start_time = time.time()
solve_puzzle(board_obstacles, heights_remaining, grid, 0, 0)
end_time = time.time()

print("FINISHED")
print_grid(board_obstacles, grid)

print()
print("seconds elapsed", end_time - start_time)
# print(grid)