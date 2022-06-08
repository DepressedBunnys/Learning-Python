print("GBF Bot")
#\n to create a new line
print("GBF\nBot")
#\" to add a quoatation mark 
print("GBF \"Bot\"")
#Creating a string variable
phrase = "GBF Bot"
print(phrase)
#Concatination
print(phrase + " under GBF")

#Functions
print(phrase.lower()) #Lower cases the string
print(phrase.upper()) #Upper cases the string
print(phrase.isupper()) #Returns true if the entire thing is upper case
print(phrase.upper().isupper()) #Returns true
print(len(phrase)) #Returns the length of the string
print(phrase[0]) #Gets the first letter of the string, [index]
#Indexing on strings starts with 0
print(phrase.index("G")) #Returns the index of the G : 0, This also words with words, it will 
#give where the word starts
#Parameter: value that you give into a function
print(phrase.replace("Bot", "Inc")) #Replace Bot with Inc, first parameter is 
#the word to be replaced, second parameter is the word to be replaced to 

#GBF Bot
#GBF
#Bot
#GBF "Bot"
#GBF Bot
#GBF Bot under GBF
#gbf bot
#GBF BOT
#False
#True
#7
#G
#0
#GBF Inc
