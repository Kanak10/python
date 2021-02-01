d = {1 : "Arpit Sahu", 2 : "Harshjay Gupta", 3 : "Kanak Gupta", 4 : "Shubhham Choudary"}
cname = {5 : "Benaam"}

#print dictionary
print(d)

#The fromkeys() method returns a dictionary with the specified keys and the specified value.
l = [1,2,3,4]
l2 = "Arpit Sahu"
dic = dict.fromkeys(l, l2)#the keys are different but the value is same for all keys. #syntax = dict.fromkeys(keys, value) 
print(dic)

#The get() method returns the value for the specified key if key is in dictionary.
print(d.get(2))#syntax = dict.get(key[, value]) 

#The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
print(d.items())

#The keys() method returns a view object that displays a list of all the keys in the dictionary
print(d.keys())

#The values() method returns a view object that displays a list of all the values in the dictionary.
print(d.values())

#The update() method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.
d.update(cname)
print(d)

#The Python popitem() method removes and returns the last element (key, value) pair inserted into the dictionary.
print(d.popitem())

#The setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
print(d.setdefault(4, "Shubhham Choudary"))#syntax = dict.setdefault(key[, default_value])

#The pop() method removes and returns an element from a dictionary having the given key.
print(d.pop(4))#syntax = dictionary.pop(key[, default])

#clear dictionary
print(d.clear())#clear method used to clear the dictionary

point = {'x':4,'y':-5}
print('{x} {y}'.format(**point))