s = set([5,4,7,8,4,1,421,5,4,2,8])

print(s)

#print Type of s
print(type(s))

#The set add() method adds a given element to a set.
#If the element is already present, it doesn't add any element.
s.add(55)
print(s)

#The remove() method removes the specified element from the set.
s.remove(421)
print(s)

#The copy() method returns a shallow copy of the set.
s1 = s.copy()
print(s1)

#
print(s1.clear())

#The discard() method removes a specified element from the set (if present).
'''
The discard() method removes the specified element from the set.
However, if the element doesn't exist, the set remains unchanged; you will not get an error.
'''
print(s.discard(421))

#The pop() method removes an arbitrary element from the set and returns the element removed.
print(s.pop())

#The Python set update() method updates the set, adding items from other iterables.
s1 = {"Kanak", "Nanni", "Tanshu", "Harsh"}
s.update(s1)
print(s)
s.clear()
s1.clear()

s = {5,4,8,7,6}
s1 = {2,1,3,4,5,6}

#The intersection() method returns a new set with elements that are common to all sets.
print(s.intersection(s1))

#The difference() method returns the set difference of two sets.
print(s.difference(s1))
print(s)

#The intersection_update() updates the set calling intersection_update() method with the intersection of sets.
s.intersection_update(s1)
print(s)

s = {5,4,8,7,6}
#The difference_update() updates the set calling difference_update() method with the difference of sets.
s.difference_update(s1)
print(s)

#The isdisjoint() method returns True if two sets are disjoint sets. If not, it returns False.
print(s.isdisjoint(s1))

#The issubset() method returns True if all elements of a set are present in another set (passed as an argument). If not, it returns False.
print(s.issubset(s1))

s = {5,4,8,7,6}
#The Python set union() method returns a new set with distinct elements from all the sets.
print(s.union(s1))

#The Python symmetric_difference() method returns the symmetric difference of two sets.
print(s.symmetric_difference(s1))
print(s^s1)

#The symmetric_difference_update() method finds the symmetric difference of two sets and updates the set calling it.
print(s.symmetric_difference_update(s1))