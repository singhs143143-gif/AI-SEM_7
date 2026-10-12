from itertools import permutations
# Distance between cities
distance = {
    ('A', 'B'): 10,
    ('A', 'C'): 15,
    ('A', 'D'): 20,

    ('B', 'A'): 10,
    ('B', 'C'): 35,
    ('B', 'D'): 25,

    ('C', 'A'): 15,
    ('C', 'B'): 35,
    ('C', 'D'): 30,

    ('D', 'A'): 20,
    ('D', 'B'): 25,
    ('D', 'C'): 30
}


cities = ['A', 'B', 'C', 'D']

start = 'A'

other_cities = [city for city in cities if city != start]

minimum_distance = float('inf')
best_route = None


# Generate all possible routes
for route in permutations(other_cities):

    complete_route = (start,) + route + (start,)

    total_distance = 0

    for i in range(len(complete_route) - 1):

        from_city = complete_route[i]
        to_city = complete_route[i + 1]

        total_distance += distance[
            (from_city, to_city)
        ]

    if total_distance < minimum_distance:

        minimum_distance = total_distance
        best_route = complete_route

print("Best Route:", " -> ".join(best_route))
print("Minimum Distance:", minimum_distance)