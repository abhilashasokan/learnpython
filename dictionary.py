# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)


thisdict["year"] = 2018
print(thisdict["year"])

# Loop Through a Dictionary
print("**************************")
for x in thisdict:
  print(x + " --> " + str(thisdict[x]))

# Dictionary Length
print("length of Dictionary is "+str(len(thisdict)))

# Adding Items
thisdict["color"] = "red"
print(thisdict)

# Removing Items
# del thisdict["model"]
# print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)


