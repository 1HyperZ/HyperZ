def are_files_equal(file1, file2):
    file1_open = open(file1, 'r')
    file2_open = open(file2, 'r')
    aviv = []
    gilad = []
    for line1 in file1_open:
        aviv.append(line1)
    for line2 in file2_open:
        gilad.append(line2)
    return aviv == gilad
print(are_files_equal(r"D:\vacation.txt", r"D:\work.txt"))