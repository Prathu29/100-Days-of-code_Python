# TUPLES IN PYTHON

tup = (1, 2, 76, 245, 32, "hello", True)

print(type(tup))
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])


if 76 in tup:
    print("YES")
tup1 = tup[1:4]  # tup1 -> this is a new tuple
print(tup1)
