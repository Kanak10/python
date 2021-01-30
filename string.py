mystr = "My Name is Kanak Gupta."

#to print mystr
print(mystr)

#Print from index 0 to 5
print(mystr[0:5])

#print length of string
print(len(mystr))

#print string by using slicing
print(mystr[0:23])

#print string by giving value out of index
print(mystr[0:74])

#print by escaping a letter
print(mystr[0:14:2])

#Example of slicing
print(mystr[:])
print(mystr[0:])
print(mystr[:23])
print(mystr[0::2])
print(mystr[::])

#example of negative silicing
print(mystr[-4:-2])
print(mystr[-13:])
print(mystr[:-13])
print(mystr[-3:-20:-2])

#string function
print(mystr.isalnum())#return False because user string have space in between
print(mystr.isalpha())#return False because all character are not alphabet there is space in betwen
print(mystr.endswith("Gupta."))#"endswith" function is used to check the last charater
print(mystr.count("a"))#used to count the character
print(mystr.find("a"))#used to find any character
print(mystr.lower())#used to convert string in lowercase
print(mystr.upper())#used to convert string in uppercase
print(mystr.replace("is", "are"))
print(mystr.capitalize())#capitilize first letter of string
print(mystr.casefold())
print(mystr.center())






























