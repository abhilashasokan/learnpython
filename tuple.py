# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
# ------------------------------------------------------------------------------------------------------------
# Creation of tuple
fruits = ("apple", "banana", "cherry")
print(fruits[0])
print(fruits[1])


# * Tuples are fixed size in nature whereas lists are dynamic.
# * You can't add elements to a tuple. Tuples have no append or extend method.
# * You can't remove elements from a tuple. Tuples have no remove or pop method.
# * You can find elements in a tuple, since this doesn’t change the tuple.
# * You can also use the in operator to check if an element exists in the tuple.
# * Tuples are faster than lists. If you're defining a constant set of values and all you're ever going to do with it is iterate through it, use a tuple instead of a list.
# * It makes your code safer if you “write-protect” data that does not need to be changed.
