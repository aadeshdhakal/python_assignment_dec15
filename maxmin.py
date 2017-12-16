my_list = [4, 2, 4, 0, 2, 4, 5, 7, 8, 9, 23, 8, 5, 4, 2, 2, 34, 4, 45]
count = len(my_list)

min_num = my_list[0]
max_num = my_list[0]
for x in my_list:
    if x < min_num:
        min_num = x
    if x > max_num:
        max_num = x

print("The minimum number is {} and the maximum number is {}.".format(min_num, max_num))

