def shift_left(my_list):
    a = my_list[0]
    b = my_list[1]
    c = my_list[2]
    my_list[0] = b
    my_list[1] = c
    my_list[2] = a
    print(my_list)

shift_left(['monkey', 2.0, 1])