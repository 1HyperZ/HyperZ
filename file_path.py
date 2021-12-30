path = input("enter path: ")
action = input("enter action(sort, rev or last: ")
aviv = []
with open(path, 'r') as file:
    if action == "sort":
        for line in file:
            for word in line.split():
                if word not in aviv:
                    aviv.append(word)
        print(sorted(aviv))
    elif action == "rev":
        for line in file:
            print(line[::-1])
    if action == "last":
        num = input("enter number of last lines to read: ")
        lines = file.readlines()
        last_lines = lines[-int(num):]
        print(last_lines)
    file.close()


