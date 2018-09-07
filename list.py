numbers = ["Sam", "Poco"]
friends = ["Aparna", "Teena", "Sarith", "Jake"]
print(friends[1:])
print("**************************")
friends.extend(numbers)
print(friends)
print("**********Append****************")
friends.append("Creed")
print(friends)
print("***********Insert***************")
friends.insert(0,"Maddy")
print(friends)
print("***********Remove***************")
friends.remove("Maddy")
print(friends)
print("***********Pop - Removes the last ***************")
friends.pop()
print(friends)
print("***********Sort All***************")
friends.sort()
print(friends)
print("***********Remove All***************")
friends.clear()
print(friends)

# friends.reverse() // To reverse a list
# friends.copy() // To make a copy of a list