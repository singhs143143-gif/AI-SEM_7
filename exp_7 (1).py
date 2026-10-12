# Facts: father(father_name, child_name)

facts = [
    ("Mohan", "Ram"),
    ("Ram", "Shyam"),
    ("Ram", "Sita"),
    ("Suresh", "Mohan")
]

# Function to check whether X is the grandfather of Z
def is_grandfather(x, z):
    for father1, child1 in facts:
        if father1 == x:
            for father2, child2 in facts:
                if father2 == child1 and child2 == z:
                    return True
    return False


# Test
x = "Mohan"
z = "Shyam"

if is_grandfather(x, z):
    print(x, "is the grandfather of", z)
else:
    print(x, "is not the grandfather of", z)