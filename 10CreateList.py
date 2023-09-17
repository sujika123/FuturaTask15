# Write a python program to create a list and use the following functions-
# •
# append() and extend()
# •
# len()

#  append

print("append")
list1 = [10, 12, 13, 17]

# appending multiple values
list1.append(20)
list1.append(22)
list1.append(25)
print(list1)


#  extend

print("extend")
list2 = ['a','b','c',5,15]
list1.extend(list2)
print(list1)


# len

print("len")
print("Length of the list is ",len(list1))