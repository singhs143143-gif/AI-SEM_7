import heapq

# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 1,
    'G': 0
}

def astar(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], 0, start, [start]))
    visited = set()

    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)

        if current == goal:
            print("Shortest Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(priority_queue,
                               (new_f, new_g, neighbor, path + [neighbor]))

    print("No path found.")

# Driver code
astar('A', 'G')