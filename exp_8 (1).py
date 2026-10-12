# Facts: father(father, child)
facts = [
    ("a", "b"),
    ("a", "c"),
    ("b", "d"),
    ("b", "e"),
    ("c", "f")
]

# Check father relationship
def is_father(x, y):
    return (x, y) in facts
# brother(X, Y)
# X and Y are brothers if they have the same father
def brother(x, y):
    if x == y:
        return False
    for father, child in facts:
        if child == x:
            father_x = father
            if (father_x, y) in facts:
                return True
    return False
# cousin(X, Y)
# X and Y are cousins if their fathers are brothers
def cousin(x, y):
    for f1, child1 in facts:
        if child1 == x:
            for f2, child2 in facts:
                if child2 == y and brother(f1, f2):
                    return True
    return False
# grandson(X, Y)
# X is grandson of Y if Y is father of X's father
def grandson(x, y):
    for f, child in facts:
        if child == x:
            if (y, f) in facts:
                return True

    return False

# descendent(X, Y)
# X is a direct or indirect descendant of Y
def descendent(x, y):
    if (y, x) in facts:
        return True

    for father, child in facts:
        if father == y:
            if descendent(x, child):
                return True

    return False

print("Query: brother(X,Y)")
for x in ["a", "b", "c", "d", "e", "f"]:
    for y in ["a", "b", "c", "d", "e", "f"]:
        if brother(x, y):
            print("X =", x, ", Y =", y)

print("\nQuery: cousin(X,Y)")
found = False

for x in ["a", "b", "c", "d", "e", "f"]:
    for y in ["a", "b", "c", "d", "e", "f"]:
        if cousin(x, y):
            print("X =", x, ", Y =", y)
            found = True

if not found:
    print("No answers")

print("\nQuery: grandson(X,Y)")
for x in ["a", "b", "c", "d", "e", "f"]:
    for y in ["a", "b", "c", "d", "e", "f"]:
        if grandson(x, y):
            print("X =", x, ", Y =", y)

print("\nQuery: descendent(X,Y)")
for x in ["a", "b", "c", "d", "e", "f"]:
    for y in ["a", "b", "c", "d", "e", "f"]:
        if descendent(x, y):
            print("X =", x, ", Y =", y)