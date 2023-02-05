# sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


# Accesss set items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# add set items

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)



thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# remove set items

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")                # if "banana" doesn't exist it will error
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")               # if "banana" doesn't exist it will not error
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #  random
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) error

# loop sets
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


# join two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


# Method	                                Description
# add()	                                    Adds an element to the set
# clear()	                                Removes all the elements from the set
# copy()	                                Returns a copy of the set
# difference()	                            Returns a set containing the difference between two or more sets
# difference_update()	                    Removes the items in this set that are also included in another, specified set
# discard()	                                Remove the specified item
# intersection()	                        Returns a set, that is the intersection of two other sets
# intersection_update()	                    Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                            Returns whether two sets have a intersection or not
# issubset()	                            Returns whether another set contains this set or not
# issuperset()	                            Returns whether this set contains another set or not
# pop()	                                    Removes an element from the set
# remove()	                                Removes the specified element
# symmetric_difference()	                Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	            inserts the symmetric differences from this set and another
# union()	                                Return a set containing the union of sets
# update()	                                Update the set with the union of this set and others