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


