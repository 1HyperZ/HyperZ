def count_chars(my_str):
    dict_m = {}
    aviv = []
    mynew_str = my_str.replace(' ', '')
    for x in mynew_str:
        if x not in aviv:
            dict_m[x] = my_str.count(x)

        aviv.append(x)
    return dict_m

magic_str = "abra cadabra"
print(count_chars(magic_str))