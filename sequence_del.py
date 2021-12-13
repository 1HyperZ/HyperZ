def sequence_del(my_str):
    new_str = ""
    last_letter = " "
    for x in my_str:
        if x != last_letter:
            new_str = new_str + x
            last_letter = x
        else:
            pass
    print(new_str)


sequence_del("Heeyyy   yyouuuu!!!")