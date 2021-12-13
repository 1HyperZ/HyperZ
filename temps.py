temp_with = input("Insert the temperature you would like to convert: ")
if temp_with[-1] == 'c':
    temp_without = temp_with.replace('c', '')
    temp_result = (float(temp_without) * 9) / 5 + 32
    print("The temperature in Ferrante is: ", temp_result, 'F')
elif temp_with[-1] == 'F':
    temp_without = temp_with.replace('F', '')
    temp_result = (float(temp_without) - 32) * 5 / 9
    print("The temperature in Ferrante is: ", temp_result, 'C')
elif temp_with[-1] == 'C':
    temp_without = temp_with.replace('C', '')
    temp_result = (float(temp_without) * 9) / 5 + 32
    print("The temperature in Celsius is: ", temp_result, 'C')
elif temp_with[-1] == 'f':
    temp_without = temp_with.replace('f', '')
    temp_result = (float(temp_without) - 32) * 5 / 9
    print("The temperature in Celsius is: ", temp_result, 'C')
else:
    print("Error: you didn't write F or C in the end")