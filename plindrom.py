word = input('Enter a word: ')
word_without_space = word.strip()
if word_without_space == word_without_space:
    print('OK')
else:
    print("NOT")