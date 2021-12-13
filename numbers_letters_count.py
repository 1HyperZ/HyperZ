def numbers_letters_count(my_str):
    int = 0
    all= 0
    for x in my_str:
        if x.isnumeric():
            int=+1
        else:
            all =+1

    print([int, all])


print(numbers_letters_count("Python 3.6.3"))