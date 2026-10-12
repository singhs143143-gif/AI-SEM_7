from collections import deque

# BFS function
def bfs(jug1, jug2, target):
    visited = set()
    queue = deque()

    # Initial state (0,0)
    queue.append((0, 0, []))

    while queue:
        x, y, path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        # Check if target is reached
        if x == target or y == target:
            print("Solution Path:")
            for state in path:
                print(state)
            return

        # Possible next states
        next_states = [
            (jug1, y),              # Fill Jug1
            (x, jug2),              # Fill Jug2
            (0, y),                 # Empty Jug1
            (x, 0),                 # Empty Jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour Jug1 -> Jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour Jug2 -> Jug1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    print("No solution found.")

# Driver code
jug1 = 4
jug2 = 3
target = 2

bfs(jug1, jug2, target)