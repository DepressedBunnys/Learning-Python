#Building a basic calculator that adds 2 numbers
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

result = first_number + second_number

print(result)
#This won't give the answer that we want, it added 2 strings together since by default input is a
#string EG. first_number = 5, second_number = 10, result = 510, so we must convert string to number

result = int(first_number) + int(second_number) #Converts strings to integer number aka whole number
print(result) #Gives 15, but will give an error if we use a whole number
#So here we use float
result = float(first_number) + float(second_number)
print(result)
