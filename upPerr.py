word = input('Please enter a string: ')
half_num = len(word)//2
half1 = (word[:half_num])
half2 = (word[half_num:].upper())
print(half1 + half2)


