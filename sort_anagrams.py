def sort_anagrams(list_of_strings):
    newlist = []
    for x in list_of_strings:
        for y in list_of_strings:
            if y not in newlist:
                if sorted(x) == sorted(y):
                    newlist.append([y])
    return newlist

list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
print(sort_anagrams(list_of_words))
