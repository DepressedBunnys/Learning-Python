#Functions relating to arrays
numbers = ['1', '3', '8', '11', '15', '18', '18', '17']
friends = ["Kevin", "Katie", "Maddy", "Richard", "Hassan"]

print(friends.append("Adam")) #Adds Adam to the end of the friends array
print(friends.extend(numbers)) #Adds both arrays to each other
print(friends.insert(1, "Maria")) #Adds Maria to position 1
print(friends.remove("Kevin")) #Removes Kevin from the array
print(friends.clear()) #Empties the array
print(friends.pop()) #Will remove the last element from the array
print(friends.index("Kevin")) #Gives the index of a certain element, if it doesn't exist it will return
#an error
print(numbers.count("18")) #Returns the amount of times the number 18 was repeated
print(numbers.sort()) #Sorts the array in ascending order
print(numbers.reverse()) #Sorts the array in descending order
friends_two = friends.copy() #Will copy the friends array
print(friends_two)
