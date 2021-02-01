"""
Lists are just like dynamic sized arrays, declared in other languages (vector in C++ and ArrayList in Java).
Lists need not be homogeneous always which makes it a most powerful tool in Python.
A single list may contain DataTypes like Integers, Strings, as well as Objects.
Lists are mutable, and hence, they can be altered even after their creation.
List in Python are ordered and have a definite count.
The elements in a list are indexed according to a definite sequence and the indexing of a list is done with 0 being the first index.
Each element in the list has its definite place in the list, which allows duplicating of elements in the list, 
with each element having its own distinct place and credibility.
Note- Lists are a useful tool for preserving a sequence of data and further iterating over it.
"""
from typing import get_origin


grocery = ["Harpic" , "Vim bar" , "Dettol" , "Rice" , "Noodles" , "Sugar"]

#print list
print(grocery)

#print item usin ndex value
print(grocery[4]+"\n")

#print using for loop
for i in grocery:
    print(i)
print("\n")

n = [4,8,6,2,1,8,15,45,45,12,48,54,]

#The index() method returns the index of the specified element in the list.
print(grocery.index("Sugar"))

#The append() method adds an item to the end of the list.
grocery.append("Vegetable oil")
print(grocery)

#The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
g = ["Bodylotion", "Hair oil"]
grocery.extend(g)
print(grocery)

#The list insert() method inserts an element to the list at the specified index.
grocery.insert(3,"Shampoo")
print(grocery)

#The remove() method removes the first matching element (which is passed as an argument) from the list.
grocery.remove("Shampoo")
print(grocery)

#The count() method returns the number of times the specified element appears in the list.
print(grocery.count("Rice"))

#The pop() method removes the item at the given index from the list and returns the removed item.
print(grocery.pop(5))

#The reverse() method reverses the elements of the list.
grocery.reverse()
print(grocery)

#The sort() method sorts the elements of a given list in a specific ascending or descending order.
#syntax = list.sort(key=..., reverse=...), sorted(list, key=..., reverse=...)
print(sorted(grocery))

employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

def get_name(employee):
    return employee.get('Name')

def get_age(employee):
    return employee.get('age')

def get_salary(employee):
    return employee.get('salary')

employees.sort(key=get_name)
print(employees, end='\n\n')

employees.sort(key=get_age)
print(employees, end='\n\n')

employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')

#The copy() method returns a shallow copy of the list.
print(grocery.copy())

#The clear() method removes all items from the list.
print(grocery.clear())