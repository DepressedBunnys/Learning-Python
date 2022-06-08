friends = ["Kevin", "Katie", "Maddy", "Richard", "Hassan"]
#This is an array that contains 5 items
#We can add any data type to the array, boolean, number, string etc.

print(friends) # Gives ["Kevin", "Katie", "Maddy", "Richard", "Hassan"]
print(friends[2]) #Will give Maddy, we used indexing, just like strings, array's index start from 0
print(friends[-2]) #Will also give Katie, this starts indexing from the back so 0 = -1
print(friends[1:]) #Will give everything after index 1, Katie, Maddy, Richard, Hassan
print(friends[1:3]) #Will give everything from 1 to 2 but not including 3
friends[1] = "Lalia" #Updated Katie to Lalia
print(friends)
