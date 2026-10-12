# Mini-Max Algorithm

import math

# Mini-Max function
def minimax(depth, nodeIndex, isMax, values, height):

    # Base case: leaf node reached
    if depth == height:
        return values[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        )

# Leaf node values
values = [3, 5, 2, 9, 12, 5, 23, 23]

# Height of the tree
height = int(math.log2(len(values)))

# Find the optimal value
result = minimax(0, 0, True, values, height)

print("The optimal value is:", result)