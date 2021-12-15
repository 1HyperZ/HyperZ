sum = 0
for x in range(10):
    grades = int(input("enter grade"))
    sum = sum + grades
average = sum // 10
if average > 50:
    print("fail")
elif 80 > average > 50:
    print("ok")
elif average > 80:
    print("excellent")
