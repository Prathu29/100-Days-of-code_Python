# String methods


#Strings are immutable
a = "Prathu"
b = "glitch, you are insane!!!"
c = "hello how are you" 
print(len(a))
print(a.upper()) #this does not changes the existing string insted it creates a new string because srtings are immutable
print(a.lower())
print(b.rstrip("!"))#removes ant traling characters
print(a.replace("Prathu","Glitch"))#replaces all occurances of string with another string
print(c.split(" "))#splits the given string at the specified instance and returns the seperated strings
print(b.capitalize())#capatal