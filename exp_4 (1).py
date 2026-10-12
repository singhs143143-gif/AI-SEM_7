# Single Player Game - 8 Puzzle using Heuristic (Misplaced Tiles)

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Heuristic function: Count misplaced tiles
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1
    return count

# Display puzzle
def display(state):
    for row in state:
        print(row)
    print()

# Current puzzle state
state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

print("Initial State:")
display(state)

h = heuristic(state)
print("Heuristic Value (Misplaced Tiles):", h)

if h == 0:
    print("Goal State Reached!")
else:
    print("Goal State Not Reached.")