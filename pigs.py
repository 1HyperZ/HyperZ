stones_for_all_pigs = input("Enter three digits: ")
stones_for_pig_1 = int(stones_for_all_pigs)*0.01
stones_for_pig_1 = int(stones_for_pig_1)
stones_for_pig_2_0 = int(stones_for_all_pigs) % 100
stones_for_pig_2 = int(stones_for_pig_2_0) // 10
stones_for_pig_3 = int(stones_for_pig_2_0) % 10
print("Stones for Pig 1:", stones_for_pig_1)
print("Stones for Pig 2:", stones_for_pig_2)
print("Stones for Pig 3:", stones_for_pig_3)