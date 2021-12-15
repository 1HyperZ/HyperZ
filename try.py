numbers = []
count = 0
min = 100
max = 0
while count < 6:
    count += 1
    numbers.append(int(input("enter a number with two digits: ")))
for x in numbers:
    if x < min:
        min = x
for x in numbers:
    if x > max:
        max = x
print(min, max)



