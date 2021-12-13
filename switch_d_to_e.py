sentence = input('Please enter a string:')
s = sentence[0]
s2 = sentence[1:]
s3 = s2.replace('d', 'e', 100)
print(s + s3)