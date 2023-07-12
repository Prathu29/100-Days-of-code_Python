# PYTHON LIST

marks = [3, 5, 6, "prathu", True, 4, 7, 8, 9, 1]
# print(marks)
# print(type(marks))

# print(marks[-3]) #Negative index
# print(marks[len(marks)-3]) #change it to positive index
# print(marks[5-3]) #positive index
# print(marks[2]) #positive index


# if "6" in marks:
#     print("Yes")
# else:
#     print("No")


# if "rath" in "prathu":
#     print("YES")
# else:
#     print("No")


# print(marks[1:8:2])
# print(marks[1:8:3])

# print(marks[1:])


lst = [i*i for i in range(4)]
print(lst)


lst = [i*i for i in range(10) if i%2 == 0]
print(lst)