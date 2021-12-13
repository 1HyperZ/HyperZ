def seven_boom(end_number):
    aviv = []
    for x in range(end_number + 1):
        if x == 0:
            aviv.append("BOOM!")
        elif x % 7 == 0:
            aviv.append("BOOM!")
        elif '7' in str(x):
            aviv.append("BOOM!")
        else:
            aviv.append(x)
    print(aviv)


print(seven_boom(17))

print("mof")