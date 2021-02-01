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

#The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.
print(mystr.isalnum())#return False because user string have space in between

#The isalpha() method returns True if all characters in the string are alphabets. If not, it returns False.
print(mystr.isalpha())#return False because all character are not alphabet there is space in betwen

#The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.
print(mystr.endswith("Kanak", 7, 16))#"endswith" function is used to check the last charater. #Syntax = str.endswith(suffix[, start[, end]])

#The string count() method returns the number of occurrences of a substring in the given string.
print(mystr.count("a"))#used to count the character. #Syntax = string.count(substring, start=..., end=...)

#The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
print(mystr.find("a"))#used to find any character. #Syntax = str.find(sub[, start[, end]] )

#The string lower() method converts all uppercase characters in a string into lowercase characters and returns it.
print(mystr.lower())#used to convert string in lowercase

#The string upper() method converts all lowercase characters in a string into uppercase characters and returns it.
print(mystr.upper())#used to convert string in uppercase

#The replace() method returns a copy of the string where all occurrences of a substring is replaced with another substring.
print(mystr.replace("is", "are"))#Syntax = str.replace(old, new [, count]) 

#In Python, the capitalize() method converts first character of a string to uppercase letter and lowercases all other characters, if any.
print(mystr.capitalize())#capitilize first letter of string

#The casefold() method is an aggressive lower() method which converts strings to case folded strings for caseless matching.
'''
The casefold() method removes all case distinctions present in a string. It is used for caseless matching, i.e. ignores cases when comparing.
For example, the German lowercase letter ß is equivalent to ss. However, since ß is already lowercase, the lower() method does nothing to it. 
But, casefold() converts it to ss.
'''
print(mystr.casefold())

#The center() method returns a string which is padded with the specified character.
print(mystr.center(34, "*"))#syntax = string.center(width[, fillchar])

#The expandtabs() method returns a copy of string with all tab characters '\t' replaced with whitespace characters until the next multiple of tabsize parameter.
str = "My\tName\tis\tKanak\tGupta."
print(str.expandtabs(3))#syntax = string.expandtabs(tabsize)

#The string encode() method returns encoded version of the given string.
print(mystr.encode(encoding='UTF-8',errors='strict'))

#The string format() method formats the given string into a nicer output in Python.
print("Hello {} Myself {} Gupta and My {} is {age}".format("Everyone", "Kanak", "age", age = 19))

#The index() method returns the index of a substring inside the string (if found). If the substring is not found, it raises an exception.
print(mystr.index("is"))#syntax = str.index(sub[, start[, end]] )

#The isdecimal() method returns True if all characters in a string are decimal characters. If not, it returns False.
'''
The superscript and subscripts are considered digit characters but not decimals. 
If the string contains these characters (usually written using unicode), isdecimal() returns False.
Similarly, roman numerals, currency numerators and fractions are considered numeric numbers (usually written using unicode) but not decimals. 
The isdecimal() also returns False in this case.
'''
str = "7634"
print(str.isdecimal())

#The isdigit() method returns True if all characters in a string are digits. If not, it returns False.
'''
In Python, superscript and subscripts (usually written using unicode) are also considered digit characters.
Hence, if the string contains these characters along with decimal characters, isdigit() returns True.
The roman numerals, currency numerators and fractions (usually written using unicode) are considered numeric characters but not digits.
The isdigit() returns False if the string contains these characters.
'''
print(str.isdigit())

#The isnumeric() method returns True if all characters in a string are numeric characters. If not, it returns False.
'''
In Python, decimal characters (like: 0, 1, 2..), digits (like: subscript, superscript), and characters having Unicode numeric value property
(like: fraction, roman numerals, currency numerators) are all considered numeric characters.
'''
print(str.isnumeric())

#The isidentifier() method returns True if the string is a valid identifier in Python. If not, it returns False.
str = "hey"
print(str.isidentifier())
str = "del"
print(str.isidentifier())
str = "45hey"
print(str.isidentifier())

#The islower() method returns True if all alphabets in a string are lowercase alphabets. 
#If the string contains at least one uppercase alphabet, it returns False.
print(mystr.islower())

#The string isupper() method returns whether or not all characters in a string are uppercased or not.
print(mystr.isupper())

#The isprintable() methods returns True if all characters in the string are printable or the string is empty. If not, it returns False.
print(mystr.isprintable())

#The isspace() method returns True if there are only whitespace characters in the string. If not, it return False.
str = "  "
print(mystr.isspace())
print(str.isspace())

#The istitle() returns True if the string is a titlecased string. If not, it returns False.
str = "Python Is Good Language"
print(str.istitle())
print(mystr.istitle())

#The join() string method returns a string by joining all the elements of an iterable, separated by a string separator.
st = ","
str = "1234"
print(st.join(str))#syntax = string.join(iterable)

#The string ljust() method returns a left-justified string of a given minimum width.
print(str.ljust(7, "0"))#syntax = string.ljust(width[, fillchar])

#The string rjust() method returns a right-justified string of a given minimum width.
print(str.rjust(8, "0"))#syntax = string.rjust(width[, fillchar])

#The string swapcase() method converts all uppercase characters to lowercase and 
#all lowercase characters to uppercase characters of the given string, and returns it.
print(mystr.swapcase())

#The lstrip() method returns a copy of the string with leading characters removed (based on the string argument passed).
str = "33334$$$%&%^^ My name is Kanak Gupta."
print(str.lstrip("34$%&%^ "))

#The rstrip() method returns a copy of the string with trailing characters removed (based on the string argument passed).
str = "My name is Kanak Gupta.33334$$$%&%^^ "
print(str.rstrip("34$%&%^ "))

#The strip() method returns a copy of the string by removing both
#the leading and the trailing characters (based on the string argument passed).
str = "33334$$$%&%^^ My name is Kanak Gupta.33334$$$%&%^^ "
print(str.strip("34$%&%^ "))

#The partition() method splits the string at the first occurrence of the argument string and 
#returns a tuple containing the part the before separator, argument string and the part after the separator.
print(mystr.partition("is"))

#The string maketrans() method returns a mapping table for translation usable for translate() method.
str = "abcdefghijklmnopqrstuvwxyz"
st = "abcdefghijklmnopqrstuvw"
print(str.maketrans(st, mystr))

#The rpartition() splits the string at the last occurrence of the argument string and returns a tuple containing the part the before separator, 
#argument string and the part after the separator.
str = "I am Kanak Gupta.I am here to learn Python."
print(str.rpartition("am"))#see the last ocurrence of seprator

#The string translate() method returns a string where each character is mapped to its corresponding character in the translation table.
str = "abcdefghijklmnopqrstuvwxyz"
st = "abcdefghijklmnopqrstuvw"
t = str.maketrans(st, mystr)
print(str.translate(t))

#The replace() method returns a copy of the string where all occurrences of a substring is replaced with another substring.
str = "I am Kanak Gupta.I am here to learn Python."
print(str.replace("am", "are", 4))

#The rindex() method returns the highest index of the substring inside the string (if found).
#If the substring is not found, it raises an exception.
print(str.rfind("am"))

#The split() method breaks up a string at the specified separator and returns a list of strings.
print(mystr.split(" ",60))

#The rsplit() method splits string from the right at the specified separator and returns a list of strings.
print(mystr.rsplit(" "))

#The splitlines() method splits the string at line breaks and returns a list of lines in the string.
str = "My\nName\nis\nKanak\nGupta"
print(mystr.splitlines())
print(str.splitlines(True))

#The zfill() method returns a copy of the string with '0' characters padded to the left.
print(mystr.zfill(40))

#The format_map() method is similar to str.format(**mapping) except that str.format(**mapping) 
# creates a new dictionary whereas str.format_map(mapping) doesn't.
'''
The format_map(mapping) is similar to str.format(**mapping) method.
The only difference is that str.format(**mapping) copies the dict whereas str.
format_map(mapping) makes a new dictionary during method call.
This can be useful if you are working with a dict subclass.
'''
point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

#The title() method returns a string with first letter of each word capitalized; a title cased string.
print(mystr.title())

#The isascii() method returns True if the string is empty or all characters in the string are ASCII.
print(mystr.isascii())