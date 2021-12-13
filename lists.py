def are_lists_equal(list1, list2):
    if sorted(list1) == sorted(list2):
        print("true")
    else:
        print("False")


are_lists_equal(list1 = [0.6, 1, 2, 3], list2 = [3, 2, 0.6, 1])
