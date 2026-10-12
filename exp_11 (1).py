from collections import deque

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def get_moves(state):
    moves = []
    zero_position = state.index(0)
    row = zero_position // 3
    col = zero_position % 3

    if row > 0:
        moves.append(zero_position - 3)

    if row < 2:
        moves.append(zero_position + 3)

    if col > 0:
        moves.append(zero_position - 1)

    if col < 2:
        moves.append(zero_position + 1)

    return moves

def swap(state, i, j):
    new_state = list(state)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return tuple(new_state)

def solve(start):
    queue = deque()

    queue.append((start, []))

    visited = set()

    visited.add(start)

    while queue:

        state, path = queue.popleft()

        if state == GOAL:
            return path + [state]

        zero_position = state.index(0)

        for move in get_moves(state):

            new_state = swap(state, zero_position, move)

            if new_state not in visited:

                visited.add(new_state)

                queue.append(
                    (new_state, path + [state])
                )

    return None
def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])

    print()


# Initial state
start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)
solution = solve(start)
if solution:
    print("Solution found!\n")
    for state in solution:
        print_puzzle(state)
else:
    print("No solution found.")