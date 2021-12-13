def last_early(my_str):
    lastletter = my_str[0:-2].__contains__(my_str[-1])
    return lastletter
print(last_early("aviv"))