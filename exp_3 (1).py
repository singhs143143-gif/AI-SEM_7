# DFS for Water Jug Problem

def dfs(jug1, jug2, target):
    visited = set()

    def solve(x, y, path):
        if (x, y) in visited:
            return False

        visited.add((x, y))
        path.append((x, y))

        # Check if target is reached
        if x == target or y == target:
            print("Solution Path:")
            for state in path:
                print(state)
            return True

        # Generate all possible next states
        next_states = [
            (jug1, y),   # Fill Jug1
            (x, jug2),   # Fill Jug2
            (0, y),      # Empty Jug1
            (x, 0),      # Empty Jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour Jug1 -> Jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour Jug2 -> Jug1
        ]

        for nx, ny in next_states:
            if solve(nx, ny, path.copy()):
                return True

        return False

    if not solve(0, 0, []):
        print("No solution found.")

# Driver code
jug1 = 4
jug2 = 3
target = 2

dfs(jug1, jug2, target)