def cube(list_1):
    count = len(list_1)
    list_2 = []
    for x in range(count):
        c = list_1[x] ** 3
        list_2.append(c)
    return list_2


list_0 = [1, 2, 4, 4, 3, 5, 6]
print(cube(list_0))

