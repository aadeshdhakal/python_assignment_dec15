full_name = input("Enter your full name: ")
name = full_name.split()
count = len(name)

if count == 2:
    first_name, last_name = name
    print("first_name is {}".format(first_name))
    print("last_name is {}".format(last_name))
if count == 3:
    first_name, mid_name, last_name = name
    print("first_name is {}".format(first_name))
    print("mid_name is {}".format(mid_name))
    print("last_name is {}".format(last_name))


